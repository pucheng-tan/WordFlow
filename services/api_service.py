import os
import firebase_admin
from firebase_admin import credentials
#from google.cloud import firestore
from firebase_admin import firestore
from datetime import datetime

# Some helpful docs: 
# General best practices:
# https://firebase.google.com/docs/firestore/best-practices 
# Adding Data: 
# https://cloud.google.com/firestore/docs/manage-data/add-data
# Stuff for pagination (not implemented yet):
# https://firebase.google.com/docs/firestore/query-data/query-cursors 
# Queries (getting data): 
# https://firebase.google.com/docs/firestore/query-data/queries 
# Ordering and limiting data (implemented): 
# https://firebase.google.com/docs/firestore/query-data/order-limit-data 
# Transactions (doing things in batches- all succeed or none do) 
# https://cloud.google.com/firestore/docs/manage-data/transactions

class API:
    """Direct interface with the API.
    Usage:
        get, get_all: use to retrieve data from the database
        post: use to save data from the database

        get_last_statement: for debugging purposes, will return a string of previous query

    Raises:
        TypeError, ValueError, probably AttributeError
    """
    __instance = None

    _db = None
    _last_statement = ""

    # _projectID = "cmpt370-group2"   
    # firebase_config = {
    #     'apiKey': "AIzaSyDg_L6PD2cbSSFUTEpET56VOVKJaGWm5Nc",
    #     'authDomain': "cmpt370-group2.firebaseapp.com",
    #     'databaseURL': "https://cmpt370-group2.firebaseio.com",
    #     'projectId': "cmpt370-group2",
    #     'storageBucket': "cmpt370-group2.appspot.com",
    #     'messagingSenderId': "985070142874",
    #     'appId': "1:985070142874:web:8d5d49ddeaea00890be623",
    #     'measurementId': "G-YDBCLJ6R7X"
    # }

    @staticmethod
    def get_api():
        if API.__instance == None:
            API()
        return API.__instance

    @staticmethod
    def _get_db():
        API._last_statement = "db"
        return API._db


    def __init__(self):
        # this class needs to be singleton, following tutorial from here: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
        # if (API._db is not None):
        #     raise Exception("This class is a singleton!")
        # else:
        #     cred = credentials.ApplicationDefault()
        #     firebase_admin.initialize_app(cred, {
        #     'projectId': API._projectID,
        #     })
        # API._db = firestore.client()

        if API.__instance != None:
            raise Exception("This class is a singleton! Call static get_instance() instead of constructor")
        else:
            # TODO: This is not how credentials should be setup.
            # If this is ever called more than once, the initialize_app gives an error because it is only ever meant to be called once!
            # The JSON is credentials for a service account that's actually not supposed to go into a public repository.
            if not firebase_admin._apps:
                cred = credentials.Certificate(
                    './cmpt370-group2-firebase-adminsdk-lno8j-3910eb45cf.json'
                )
                firebase_admin.initialize_app(cred)
            API._db = firestore.client()
            API.__instance = self

    def get(self, path, where_clauses=None, order_by=None, limit=None):
        """ Returns data from following a specific path.
        Raises: TypeError with Invalid query message. Will return the query as interpreted as a message.
        Args:
            - path: string in format of "parent_collection/doc_id/child_collection/doc_id"
                # extraneous "/" will be eliminated
                # if using a where clause, path should end with a collection
            - where_clauses: list of where clauses to filter by
                [field, operator, value]
                operators: <, <=, ==, >, >=, array_contains, array_contains_any, in, string_starts
                all comparisons (<, <=, >, >=, string_starts) MUST BE ON THE SAME FIELD
            - limit: Max number of entries to return
            - order_by: [{field_name: is_ascending}]
                # is_ascending should be True for ascending, else False
                # this also checks for the existance of a field
                # can order by multiple fields
                # cannot order query by fields with == or "in" where clause
        Usage: 
            - To get a specific document by its reference, just use path, end with doc id
            - To get all documents in a subcollection, use path and end with collection
            - To get filtered results: end with collection, and use where_clauses/order_by/limit
            - if you want to look across subcollections in multiple parents, use get_all() instead
        Returns:
            - if a specific document is referenced, dict of data with "id" = doc_id added
            - else {id: doc, id2: doc2,...}
        """
        # start with instance of firestore client
        query = self._get_db()

        try: 
            # point the query down the path, then do filtering operations
            query = self._get_path(query, path)       
            query = self._filter_query(query, where_clauses, order_by, limit)

            # then pull the data and turn it into a dictionary
            return self._to_dict(query)
        except:
            raise TypeError("Invalid query: ", self.get_last_statement())

    def get_all(self, collection_name, where_clauses, order_by=None, limit=None):
        """ Returns data from subcollections across multiple parents.
        Args:
            - collection_name: name of the subcollections to look at
            - where_clauses: list of where clauses to filter by
                [field, operator, value]
                operators: <, <=, ==, >, >=, array_contains, array_contains_any, in, string_starts
                all comparisons (<, <=, >, >=, string_starts) MUST BE ON THE SAME FIELD
            - limit: Max number of entries to return (positive integer)
            - order_by: [{field_name: is_ascending}] 
                # is_ascending should be True for ascending, else False
                # this also checks for the existance of a field
                # can order by multiple fields
                # if where clauses use <, <=, >, >= operators, must first order on same field
                # cannot order query by fields with == or "in" where clause

        Usage: 
            - Many UserProfiles have child History collections. 
              Put History as collection_name to look at all History subcollections.
            - where_clauses are required so as to not pull all the data
            - commonly searched subcollections should have a path attribute so that
              searches for History items within a UserProfile within a School can be
              filtered by the school
        """
        # start with the firestore client and the collection group
        query = self._get_db().collection_group(collection_name)
        API._last_statement += ".collection_group(" + collection_name + ")"

        # this stuff is the same for get and get_all: use helper function to filter
        query = self._filter_query(query, where_clauses, order_by, limit)
        return self._to_dict(query)

    def _get_path(self, query, path_string):
        """Takes the path string and adds it onto the query
        """
        q = query

        # filter out any blank items caused by extraneous "/" characters
        split_path = list(filter(lambda item: item, path_string.split("/")))
        
        # collections is the path divided by two and rounded down
        num_collections = len(split_path) // 2

        # for each collection, add the collection and the document to query
        for i in range(0, num_collections):
            collection_index = i * 2
            document_index = collection_index + 1
            collection = split_path[collection_index]
            document = split_path[document_index]

            API._last_statement += ".collection(" + collection + ").document(" + str(document) + ")"
            q = q.collection(collection).document(document)
        
        # if there's a last collection without a document, add that collection
        if len(split_path) % 2 == 1:
            collection = split_path[-1]
            API._last_statement += ".collection(" + collection + ")"
            q = q.collection(collection)

        return q


    def _filter_query(self, query, where_clauses=None, order_by=None, limit=None):
        """ Helper function calls all the filter stuff on the query.
        Does a bit of validation as well on where_clauses and order_by.        
        """        

        if where_clauses:
            # for validating operators
            comparisons = ["<", ">", "<=", ">=", "string_starts"]
            all_operators = comparisons + ["==", "array_contains", "in", "array_contains_any"]

            # do some basic validation on each clause
            for clause in where_clauses:
                # look for wrong types and wrong length lists                
                if not isinstance(clause, list) or len(clause) != 3:
                    raise TypeError("Invalid query", str(clause) + " is not a valid where clause. Format is ['field', 'operator', value]")
                # look for valid operator
                if clause[1] not in all_operators:
                    raise ValueError("Invalid query", str(clause[1]) + " is not a valid operator. Valid operators are " + str(all_operators))

            # all of the where clauses that use comparisons
            where_compare = list(filter(lambda where: where[1] in comparisons, where_clauses))
            # and all of the fields those qhere clauses apply to, specifically
            where_fields = list(map(lambda where: where[0], where_compare))

            # all those where_fields need to be first in the order_by, so add it if it's not first:
            if len(where_fields) > 0 and order_by:
                # Firestore says to only use comparison operators on the same field, so only looking at first
                where_field = where_fields[0]
                order_compare = list(filter(lambda order_clause: order_clause == where_field, order_by))
                if len(order_compare) == 0:
                    order_by.insert(0, {where_field: True})

            query = self._get_where_clauses(query, where_clauses)

        if order_by:
            query = self._get_order_by(query, order_by)

        if limit:
            query = self._get_limit(query, limit)

        return query
    
    def _get_where_clauses(self, query, where_clauses):
        """Process where clauses to add them to the query
        """
        # Loop through and append each to the query
        q = query

        # deal with "string starts with" issues
        for clause in where_clauses:
            
            # custom behaviour! use string comparison to search text, as not a Firestore option
            # ie: if we're looking for string starting with "S/X/U/", like "S/X/U/doc_id"
            # they'll all be below "S/X/U/~" and above "S/X/U/ " because ASCII values
            # pretty snazzy, but unfortunately it is case-sensitive
            if clause[1] == "string_starts":
                API._last_statement += ".where(" + clause[0] + " between '" + clause[2] + " ' and '" + clause[2] + "~')"
                q = q.where(clause[0], "<=", clause[2] + "~").where(clause[0], ">=", clause[2] + " ")                
            else:
                API._last_statement += ".where(" + clause[0] + clause[1] + str(clause[2]) + ")"
                q = q.where(clause[0], clause[1], clause[2])
            
        return q

    def _get_limit(self, query, limit): 
        """ Adds limit to query
        """     
        if limit < 0:
            raise ValueError("Query limit cannot be negative")

        API._last_statement += ".limit(" + str(limit) + ")"
        return query.limit(limit)

    def _get_order_by(self, query, order_by):
        """ Does the order_by. 
        Validation has been handled at this point in respect to where clauses
        """
        q = query

        for order in order_by:
            field = list(order.keys())[0]
            direction = 'ASCENDING' if order[field] else 'DESCENDING'
            API._last_statement += ".order_by(" + field + ", direction=" + direction + ")"
            q = q.order_by(field, direction=direction)
        return q


    def post(self, path, data, merge=True):
        """ Sets the given data following the path.
        Args:
            path: "collection/doc_id/collection/doc_id"
                - can end with collection instead of doc_id
                - id from data will be grabbed and added on if it exists
                - but the id from the path will override the one in data if they differ
            data: the object to be recorded, in a dictionary format
                - store the id in an id attribute in the object,
                    - will look at existing document, or will create using that id
                    - if no id in data or path, will create auto-id
                - can have attributes of the following data types: 
                  {string, boolean, number (stores as double), datetime, array (list), None, nested object}
                - Access nested object fields with object.attribute format with merge=True to avoid overwriting the whole object
                https://firebase.google.com/docs/firestore/manage-data/add-data#custom_objects
            merge: (default True) if set to false, posts will overwrite, even blanks will overwrite existing data!
                the existing data. If true, it will do updates and add fields to existing data
        Returns:
            {"document": {"id": <the id>, "path": <path/to/document/without/id>}, 
             "result": {update_time {seconds: x, nanos: y}}}    
             for success. An exception will be raised for failure.    
        """        
        query = self._get_db()
        query = self._get_path(query, path)

        # if path doesn't lead to a document, it's time to create one
        if "DocumentReference" not in str(type(query)):
            # either use the id from the document, or auto a new one
            doc_id = "" if not "id" in data else data["id"]
            API._last_statement += ".document(" + doc_id + ")"
            if doc_id:
                query = query.document(doc_id)
            else:
                query = query.document()

        API._last_statement += ".set(" + str(data) + ", merge=" + str(merge) + ")"
        result = query.set(data, merge=merge) 
        # by default returns update_time {seconds: x, nanos: y}
        document = {
            "id": query.id,
            "path": query.path,       
        }
        return {"document": document, "result": result}

    def post_bulk(self, data, overwrite=False):
        """This is possible but it is not yet implemented
        """   
        pass
    

    def get_last_statement(self):
        """ Returns a string representation of the last statement as it was constructed.
        Use this for debugging.
        """
        return API._last_statement

    def _to_dict(self, query):
        """ Does the actual get/stream from firestore
        If it's a single DocumentReference, adds the id into the return object
        But doesn't if it's multiple because multiple is already {id: doc, id2: doc2...}
        """
        doc_type = str(type(query))

        data = None
        if "DocumentReference" in doc_type:
            data = query.get()
            doc_id = data.id
            data = data.to_dict()
            data["id"] = doc_id
        if "CollectionReference" in doc_type or "Query" in doc_type or "CollectionGroup" in doc_type:
            data = query.stream()
            data = {doc.id: doc.to_dict() for doc in data}
        # this shouldn't ever happen, but just in case...
        if data is None:
            raise TypeError("Invalid query", "expecting DocumentReference CollectionReference or Query, got " + doc_type, self.get_last_statement())
        
        return data


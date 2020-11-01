# from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# HERE IS USEFUL INFORMATION FOR ACCESSING THE API

# https://stackoverflow.com/questions/49579693/how-do-i-get-documents-where-a-specific-field-exists-does-not-exists-in-firebase
# When you want to put in a where clause of "field exists", use order_by. Above is javascript, so they say orderBy, but same thing otherwise.

class APIService:
    """Direct interface with the API
    Usage:
        get: use to retrieve data from the database
        post: use to save data from the database
    """

    _db = None

    def __init__(self):
        # this class needs to be singleton, following tutorial from here: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
        if (APIService._db is not None):
            raise Exception("This class is a singleton!")
        else:
            # TODO: This is not how credentials should be setup. 
            # If this is ever called more than once, the initialize_app gives an error because it is only ever meant to be called once!
            # The JSON is credentials for a service account that's actually not supposed to go into a public repository.
            cred = credentials.Certificate('PoC/services/cmpt370-group2-firebase-adminsdk-lno8j-3910eb45cf.json')
            firebase_admin.initialize_app(cred)
            APIService._db = firestore.client()

    @staticmethod
    def get_db():
        if APIService._db == None:
            APIService()
        return APIService._db

    def temp(self):
        data = APIService.get_db().collection("Schools").document("o2lTSAI6X4yGdIZ0huB9").collection("UserProfiles").collection_group("History")
        return self.to_dict(data)

    def to_dict(self, data, is_document=False):
        # https://stackoverflow.com/questions/52984107/how-to-convert-firestore-query-response-to-json-using-python
        if is_document:
            d = data.get()
            d = d.to_dict()
        else:
            d = data.stream()
            d = {doc.id: doc.to_dict() for doc in d}
        return d

    def get(self, params):
        #TODO: This function needs to do some thinking to know which functions to call to get the full query
        # data = self._get_collection(params['collection'], params['where']).stream()
        query = self.get_db()
        group = False
        for collection in params:
            # check for invalid collection name
            if not isinstance(collection, str):
                raise TypeError("Bad query", str(collection) + " where string value expected (collection name)")

            where = params[collection]
            query = self._get_collection(collection, where, query, group)

            # The purpose of this "group" bit is to "skip" a collection if we're looking at a collection group the next layer down
            # so, if Schools --> User Profiles --> History but we want to filter by school and not UserProfiles (but maybe History)
            # group will be set false at UserProfiles and there won't be a .collection for it.
            # But then, when we go to History next, group will be true, and we will look at the collection_group History within the school
            # and can filter from there however we want
            # if group:
            
            # group = True if not where else False
            # if not group:
                # query = self._get_collection(collection, where, query, group)        
        last_query = list(params.values())[-1]
        is_document = "reference" in last_query
        return self.to_dict(query, is_document)        

    def _get_collection(self, collection, where, query, group=False):
        q = query
    
        if not group:
            q = q.collection(collection)
        else:
            # looks for multiple matching subcollections. ie: if collection is "History" and group is True, will search History collections of all users
            q = q.collection_group(collection) 

        if where:
            q = self._get_where_clause(q, where)

        return q



    def _get_subcollection(self, document_query):
        #getting subcollections of a document
        return document_query.collections()

    # TODO: This is definitely not done and probably poorly thought out
    def _get_where_clause(self, query, where):
        q = query
        
        # Two types of "where" to expect: actual where clauses, and document references.
        # There can be multiple where clauses, so they must be looped through
        # https://cloud.google.com/firestore/docs/query-data/queries#compound_queries see here for restrictions
        try:
            if "where" in where:
                for clause in where["where"]:
                    if "exists" in clause:
                        q = q.order_by(clause[0])
                    else:
                        q = q.where(clause[0], clause[1], clause[2])
            # otherwise we'll be looking at a specific document #TODO how do we find multiple documents? I don't know!
            else:
                q = q.document(where["reference"])
        except Exception as e:
            raise TypeError("Bad query", str(where) + " where list value expected (where clauses) ", str(e))

        return q

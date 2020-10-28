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
        if (self._db is None):
            # TODO: This is not how credentials should be setup. 
            # If this is ever called more than once, the initialize_app gives an error because it is only ever meant to be called once!
            # The JSON is credentials for a service account that's actually not supposed to go into a public repository.
            cred = credentials.Certificate('PoC\services\cmpt370-group2-firebase-adminsdk-lno8j-3910eb45cf.json')
            firebase_admin.initialize_app(cred)
            self._db = firestore.client()

    def get_db(self):
        return self._db

    def temp(self):
        data = self.get_db().collection("Schools").document("o2lTSAI6X4yGdIZ0huB9").collection("UserProfiles").collection_group("History")
        return self.to_dict(data)

    def to_dict(self, json):
        # https://stackoverflow.com/questions/52984107/how-to-convert-firestore-query-response-to-json-using-python
        data = json.stream() # this is where we should check if it's a document reference because you can't do .stream() on those.    
        return {doc.id: doc.to_dict() for doc in data}

    def get(self, params):
        #TODO: This function needs to do some thinking to know which functions to call to get the full query
        # data = self._get_collection(params['collection'], params['where']).stream()
        query = self.get_db()
        group = False

        for collection in params:
            where = params[collection]

            # The purpose of this "group" bit is to "skip" a collection if we're looking at a collection group the next layer down
            # so, if Schools --> User Profiles --> History but we want to filter by school and not UserProfiles (but maybe History)
            # group will be set false at UserProfiles and there won't be a .collection for it.
            # But then, when we go to History next, group will be true, and we will look at the collection_group History within the school
            # and can filter from there however we want
            # if group:
            query = self._get_collection(collection, where, query, group)
            # group = True if not where else False
            # if not group:
                # query = self._get_collection(collection, where, query, group)        

        return self.to_dict(query)        

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
        if "where" in where:
            for clause in where["where"]:
                # convention here is to enter as where: {"field_name", "exists"} to check for non-blanks.
                # actually need to use order_by to get that!
                if "exists" in clause:
                    q = q.order_by(clause[0])
                else:
                    q = q.where(clause[0], clause[1], clause[2])
            return q
        # otherwise we'll be looking at a specific document #TODO how do we find multiple documents? I don't know!
        if "reference" in where and where["reference"]:
            q = q.document(where["reference"])

        return q

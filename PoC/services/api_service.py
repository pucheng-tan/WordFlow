# from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# HERE IS USEFUL INFORMATION FOR ACCESSING THE API

# https://stackoverflow.com/questions/49579693/how-do-i-get-documents-where-a-specific-field-exists-does-not-exists-in-firebase
# When you want to put in a where clause of "field exists", use order_by. Above is javascript, so they say orderBy, but same thing otherwise.

class APIService:

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

    def to_dict(self, json):
        # https://stackoverflow.com/questions/52984107/how-to-convert-firestore-query-response-to-json-using-python
        return {doc.id: doc.to_dict() for doc in json}

    def get(self, params):
        #TODO: This function needs to do some thinking to know which functions to call to get the full query
        data = self._get_collection(params['collection'], params['where']).stream()
        return self.to_dict(data)
        
    def _get_document(self, documentID, query):
        return query.document(documentID)

    def _get_collection(self, collection, filter=None, query=None, group=False):
        q = query
        if query is None:
            q = self.get_db()

        if not group:
            q = q.collection(collection)
        else:
            # looks for multiple matching subcollections. ie: if collection is "History" and group is True, will search History collections of all users
            q = q.collection_group(collection) 

        if filter is not None:
            q = self._get_where_clause(q, filter)

        return q



    def _get_subcollection(self, document_query):
        #getting subcollections of a document
        return document_query.collections()

    # TODO: This is definitely not done and probably poorly thought out
    def _get_where_clause(self, query, filter):
        q = query
        # standard: "field", "op_string", "value" (3)
        # combination: "field" is between "value1" and "value2" (inclusive or exclusive)
        # exists: "field" is not null
        # does not exist: "field" is empty. NOTE: not the same as null

        switcher = {
            1: filter, # where field is null
            2: lambda x: x.order_by(filter[0]), # where field is not null
            3: lambda x: x.where(filter[0], filter[1], filter[2]), # where field <operator> value
            4: filter, # where field <operator> value and <operator> value
            5: filter  # where field <operator> value OR <operator> value
        }
        whereFunc = switcher.get(len(filter))
        return whereFunc(q)

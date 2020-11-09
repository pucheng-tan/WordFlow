import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class APIService:
    """Direct interface with the API
    Usage:
        get: use to retrieve data from the database
        post: use to save data from the database
    """

    WHERE_CLAUSE = "where"
    SEARCH_ALL = "all"
    EXISTS = "exists"
    _db = None
    _projectID = "cmpt370-group2"
    
    # Web API key = "AIzaSyDg_L6PD2cbSSFUTEpET56VOVKJaGWm5Nc"

    def __init__(self):
        # this class needs to be singleton, following tutorial from here: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
        # if (APIService._db is not None):
        #     raise Exception("This class is a singleton!")
        # else:
        #     cred = credentials.ApplicationDefault()
        #     firebase_admin.initialize_app(cred, {
        #     'projectId': APIService._projectID,
        #     })
        # APIService._db = firestore.client()

        if (APIService._db is not None):
            raise Exception("This class is a singleton!")
        else:
            # TODO: This is not how credentials should be setup.
            # If this is ever called more than once, the initialize_app gives an error because it is only ever meant to be called once!
            # The JSON is credentials for a service account that's actually not supposed to go into a public repository.
            cred = credentials.Certificate(
                'PoC/services/cmpt370-group2-firebase-adminsdk-lno8j-3910eb45cf.json'
            )
            firebase_admin.initialize_app(cred)
            APIService._db = firestore.client()


    def get(self, path, where_clauses=None):
        query = self._get_db()
        # path = {"Schools": TEST_SCHOOL_ID, "UserProfiles": TEST_USER_ID, "History": APIService.WHERE_CLAUSE}
        # path_2 = ({"History": APIService.SEARCH_ALL}, [["UserProfile", "==", "BMSoKUzVnRYn103t2Oi6Nacv9X03"], ["AssignmentID", "exists"]], "2020101513091234"),
        keys = list(path.keys())
        for collection in path:
            if path[collection] not in [APIService.WHERE_CLAUSE, APIService.SEARCH_ALL]:
                query = query.collection(collection).document(path[collection])
            else:
                # Todo: Figure out decision tree 
                pass

        if path[keys[-1]] == APIService.SEARCH_ALL:
            query = query.collection_group(keys[-1])

        if path[keys[-1]] == APIService.WHERE_CLAUSE:
            query = query.collection(keys[-1])
            query = self._get_where_clauses(query, where_clauses)
        
        return self._to_dict(query, where_clauses == None)


    def post(self, params):
        return 0



    @staticmethod
    def _get_db():
        if APIService._db == None:
            APIService()
        return APIService._db

    
    def _get_where_clauses(self, query, where_clauses):
        # Loop through and append each to the query
        q = query
        for clause in where_clauses:
            if APIService.EXISTS in clause:
                q = q.order_by(clause[0])
            else:
                q = q.where(clause[0], clause[1], clause[2])

        return q

    def _to_dict(self, query, is_document):
        if (is_document):
            return query.get().to_dict()
        else:
            data = query.stream()
            data = {doc.id: doc.to_dict() for doc in data}
            return data
        
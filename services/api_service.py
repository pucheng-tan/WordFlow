import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class APIService:

    WHERE_CLAUSE = "where"
    SEARCH_ALL = "all"

    def __init__(self):
        pass

    def get(self, path, where_clause=None):
        return 0

    def post(self, params):
        return 0
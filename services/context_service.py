class ContextService:

    __instance = None


    _user_privilege = None 
    _user_uid = None
    _school_id = None
    _token = None

    def __init__(self):
        if ContextService.__instance != None:
            raise Exception("This class is a singleton! Call static get_instance() instead of constructor")
        else: 
            ContextService.__instance = self

    @staticmethod
    def get_instance():
        if ContextService.__instance == None:
            ContextService()
        return ContextService.__instance

    def get_school_id(self):
        return self._school_id

    def get_user_privilege(self):
        return self._user_privilege 

    def get_user_uid(self):
        return self._user_uid

    #when the user authenticates, we need their user id, their privilege, and their school.
    def set_user(self, privilege_level, user_uid, school_id, token=None):
        self._user_privilege = privilege_level
        self._user_uid = user_uid
        self._school_id = school_id
        self._token = token

    def reset_context(self):
        self._user_privilege = None
        self._user_uid = None
        self._school_id = None
        self._token = None
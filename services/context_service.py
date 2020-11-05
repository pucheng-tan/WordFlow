class ContextManager:

    _user_privilege = None # super-admin
    _user_uid = None
    _school_id = None

    # Make sure this gets made at a singleton
    # def __init__():


    def get_school(self):
        return "o2lTSAI6X4yGdIZ0huB9"

    def get_user_privilege(self):
        return self._user_privilege 

    #when the user authenticates, we need their user id, their privilege, and their school.
    def set_user(self, privilege_level, user_uid, school_id):
        # check to make sure that it is valid first. Can be 0: super-admin, 1: admin, 2: standard user
        self._user_privilege = privilege_level
        self._user_uid = user_uid
        self._school_id = school_id
from application_management import ApplicationManagement
from user_service import UserService

PRIVILEGE = {"standard": 2, "admin": 1, "super_admin": 0}

class UserManagement(ApplicationManagement):

    _service = UserService()

    # used in the Firestore UserProfile:
    _USER_PROFILE_FIELDS = ["id", "display_name", "email", "privilege_level"]
    # used for the actual authentication
    _USER_AUTH_FIELDS = ["email", "uid", "password", "phone"]

    def create_auth_user(self, email, password=None, display_name=None):
        """ Creates the user in Firebase *only*.
        Unless this is the school's first user, probably use create_school_user instead
        """
        user_data = {
            "email": email,
            "password": password,
            "display_name": display_name
        }
        if self._validate_user(user_data):
            user_result = self._service.create_user(user_data)
            user_data["id"] = user_result.uid
            del user_data["password"]
            return user_data
        else:
            return False

    def create_user_profile(self, email, uid, privilege_level=None, display_name=None, ):
        user_data = {
            "id": uid,
            "email": email,
            "privilege_level": privilege_level,
            "display_name": display_name
        }
        school_id = self._context.get_school_id()
        if self._validate_user(user_data):
            user_result = self._service.create_user_profile(user_data, school_id)
            return user_data
        else:
            return False

    def create_school_user(self, email, school_id, privilege_level=None, password=None, display_name=None):
        # validate the user
        user_data = {
            "email": email,
            "display_name": display_name,
            "privilege_level": privilege_level
        }
        

        # create it
        pass

    def login(self, email, password, school_id):
        # do the auth call,
        current_user = self._service.login(email, password, school_id)

        if current_user:
            # and then set the context service
            privilege_level = current_user["privilege_level"]
            user_uid = current_user["id"]
            UserManagement._context.set_user(privilege_level, user_uid, school_id)

    def invite_user(self, user):
        print(str(type(UserManagement._context)))
        school_id = UserManagement._context.get_school_id()

        return school_id

    def update_privilege(self, user, privilege_level):
        pass

    def remove_user(self):
        pass

    @staticmethod
    def _validate_user(user):
        """ Makes sure user has fields for UserProfile
        Not very thorough. Will also make sure that the user has a valid privilege level.
        Defaults to standard.
        """
        for field in UserManagement._USER_PROFILE_FIELDS:
            if field not in user:
                user[field] = None
        # set default for user privilege. We're going with standard...
        if user["privilege_level"] not in PRIVILEGE.values():
            user["privilege_level"] = PRIVILEGE["standard"]

        return user
        
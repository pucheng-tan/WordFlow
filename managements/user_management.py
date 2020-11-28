from managements.application_management import ApplicationManagement
from services.user_service import UserService

PRIVILEGE = {"standard": 2, "admin": 1, "super_admin": 0}


class UserManagement(ApplicationManagement):
    """
    NOTE ABOUT HANDLING ERRORS:
    - this is not really a level for "debugging"- we don't want the client to see memory locations and stuff,
      see examples for format but try to send clients *just* enough information that they know what's going on,
      but not enough to hack your system.
    - Errors are returned in the format of {"error": "<error message>"} and shouldn't be exception message
    """

    _service = UserService()

    # used in the Firestore UserProfile:
    _USER_PROFILE_FIELDS = {"email": ["required|id"], "id": ["required"], "display_name": [], "privilege_level": ["required|id"]}
    # used for the actual authentication
    _USER_AUTH_FIELDS = {"email": ["required"], "id": [], "password": ["required|id"], "phone": [], "display_name": []}

    def create_auth_user(self, email, password=None, display_name=None):
        """ Creates the user for auth purposes *only*.
        Unless this is the school's first user, probably use create_school_user instead
        Returns: the user object with email, display_name, and id attributes
        """
        # what is being sent to Firestore
        user_data = {
            "email": email,
            "password": password,
            "display_name": display_name
        }
        # validate user then create their auth account
        valid_user = self._validate_user(user_data, UserManagement._USER_AUTH_FIELDS)        
        if valid_user:
            user_result = self._service.create_user(valid_user)
            # grab the id and wipe the password
            valid_user["id"] = user_result.uid
            del valid_user["password"]
            return valid_user
        else:
            # NOTE: Catch this with "if 'error' in result: display_message(result['error'])"
            {"error": "Failed to create user credentials"}

    def create_user_profile(self, email, uid, privilege_level=PRIVILEGE["standard"], display_name=None, ):
        """ Creates the user profile in the database with default standard privilege level
        """
        user_data = {
            "id": uid,
            "email": email,
            "privilege_level": privilege_level,
            "display_name": display_name
        }

        print(user_data)

        result = {"error": "Failed to create user profile"}
        # the school_id is whatever the current user's school is
        school_id = self._context.get_school_id()

        # if the user is valid, and the create profile works, result is just the user_data created above,
        # otherwise it'll stay an error
        valid_user = self._validate_user(user_data, UserManagement._USER_PROFILE_FIELDS)
        try:
            if valid_user:
                response = self._service.create_user_profile(valid_user, school_id)
                if response["id"] == uid:
                    result = user_data
        except:
            pass
        return result


    def create_school_user(self, email, school_id, privilege_level=PRIVILEGE["standard"], password=None, display_name=None):
        """Create both an auth account and a user profile.
        Returns the user object, or False on failure
        Import PRIVILEGE to use PRIVILEGE["standard" | "admin" | "super_admin"]- default to standard

        """
        try:
            # the auth and user profile funcs both validate user so don't bother here too
            # do the auth first
            auth_user = self.create_auth_user(email, password, display_name)

            # and then do the profile
            user_data = self.create_user_profile(email, auth_user["id", privilege_level, display_name])          
        except:
            # return the user object else an error message. TODO: Make the error message better
            user_data = {"error": "Failed to create user"}
        return user_data

    def login(self, email, password, school_id):
        """ Authenticates the user to the school. Also sets the app's context
        """
        # do the auth call,
        current_user = self._service.login(email, password, school_id)

        # return current_user
        if "user" in current_user:
            user_profile = current_user["user"]
            # and then set the context service
            privilege_level = user_profile["privilege_level"]
            user_uid = user_profile["id"]
            # set the context once the user has successfully logged in
            UserManagement._context.set_user(privilege_level, user_uid, school_id, email, current_user["token"])
            result = user_profile
        else:
            # if there's no user in the result, there'll be an error instead
            result = current_user
        return result

    def logout(self):
        UserManagement._context.reset_context()
        # TODO: There is more to this function than just resetting the context

    def invite_user(self, user):
        pass

    def update_privilege(self, user, privilege_level):
        pass

    def remove_user(self):
        pass

    @staticmethod
    def _validate_user(user, fields):
        """ Makes sure user has fields for UserProfile
        Not very thorough. Will also make sure that the user has a valid privilege level.
        Defaults to standard.
        """
        for field in fields:
            if field not in user:
                user[field] = None
        # set default for user privilege. We're going with standard...
        # if user["privilege_level"] not in PRIVILEGE.values():
        if "privilege_level" in fields and user["privilege_level"] not in PRIVILEGE.values():
            user["privilege_level"] = PRIVILEGE["standard"]

        return user

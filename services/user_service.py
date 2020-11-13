import firebase_admin
from firebase_admin import auth

from api_service import API
from user import User

class UserService:
    """ Perform user-specific tasks, including authentication
    """

    api = None

    PRIVILEGE = {"standard": 2, "admin": 1, "super_admin": 0}

    # used in the Firestore UserProfile:
    _user_profile_fields = ["id", "display_name", "email", "privilege_level"]
    # used for the actual authentication
    _user_auth_fields = ["email", "uid", "password", "phone"]

    def __init__(self):
        if not UserService.api:
            UserService.api = API.get_api()

    def create_user(self, user, school_id):
        """ Creates the user in Firebase and also a UserProfile for that user
        User must be added to a school.
        """
        # do all the validation
        user = self._validate_user(user)

        # Create the user,
        password = user["password"] if "password" in user else None
        phone = user["phone"] if "phone" in user else None

        try:
          user_result = auth.create_user(display_name=user["display_name"], email=user["email"], password=password, phone_number=phone)  
        except auth.EmailAlreadyExistsError:
            # this is the case where the user already exists at another school (probably)
            # we're going to assume they're new to the school.
            user_result = auth.get_user_by_email(user["email"])
        # except:
        #     raise TypeError("Invalid query", "something went wrong")

        # if that is successful, create the UserProfile.
        user["id"] = user_result.uid
        data = {attribute:user[attribute] for attribute in UserService._user_profile_fields}
        # data = {
        #     "id": user_result.uid,
        #     "display_name": display_name,
        #     "email": email,
        #     "privilege_level": user["privilege_level"]
        # }
        # create a path to the appropriate school
        path = "Schools/" + school_id + "/UserProfiles"
        result = UserService.api.post(path, data)
        return result

    def _validate_user(self, user):
        """ Makes sure user has fields for UserProfile
        Not very thorough. Will also make sure that the user has a valid privilege level.
        Defaults to standard.
        """
        for field in self._user_profile_fields:
            if field not in user:
                user[field] = None
        # set default for user privilege. We're going with standard...
        if user["privilege_level"] not in UserService.PRIVILEGE.values():
            user["privilege_level"] = UserService.PRIVILEGE["standard"]

        return user

    def login(self, email, password, school_id):
        return False
    
    def logout(self, email):
        return False

    def invite_user(self, user, school_id):
        return False

    def invite_users_bulk(self, users, school_id):
        return False

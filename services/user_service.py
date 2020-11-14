import firebase_admin
from firebase_admin import auth

from api_service import API
from user import User

class UserService:
    """ Perform user-specific tasks, including authentication
    """
    _api = None

    def __init__(self):
        if not UserService._api:
            UserService._api = API.get_api()

    def create_user(self, user, school_id=None):
        """Does the work of creating the user in auth.
        If the user already exists, will return an instance of that user.
        """
        email = user["email"]
        password = user["password"]
        display_name = user["display_name"]

        try:
            user_result = auth.create_user(display_name=display_name, email=email, password=password)
        except auth.EmailAlreadyExistsError:
            # TODO: This ain't right
            user_result = auth.get_user_by_email(email)

        return user_result

    def create_user_profile(self, user, school_id):
        """ Creates the user profile in database.
        It needs the school_id to know where to nest it.
        User must already exist in auth.
        """
        path = "Schools/" + school_id + "/UserProfiles/" + user["id"]
        result = UserService._api.post(path, user) 
        return result["document"]

    def login(self, email, password, school_id):
        return False
    
    def logout(self, email):
        return False

    def invite_user(self, user, school_id):
        return False

    def invite_users_bulk(self, users, school_id):
        return False

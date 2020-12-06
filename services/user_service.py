import firebase_admin
from firebase_admin import auth
import requests
import json

from services.api_service import API


class UserService:
    """ Perform user-specific tasks, including authentication
    """
    _api = None

    def __init__(self):
        if not UserService._api:
            UserService._api = API.get_api()

    def create_user(self, user):
        """Does the work of creating the user in auth.
        If the user already exists, will return an instance of that user.
        """
        email = user["email"]
        password = user["password"]
        display_name = user["display_name"]

        try:
            auth_result = auth.create_user(display_name=display_name, email=email, password=password)
            user_result = {"uid": auth_result.uid}
        except auth.EmailAlreadyExistsError:
            user_result = self.__login(email, password)
        except ValueError as e:
            if "email" in str(e):
                user_result = {"error": "Invalid email format"}
            elif "password" in str(e):
                user_result = {"error": "Password must be at least 6 characters long"}

        return user_result

    def create_user_profile(self, user, school_id):
        """ Creates the user profile in database.
        It needs the school_id to know where to nest it.
        User must already exist in auth.
        """
        path = "Schools/" + school_id + "/UserProfiles/" + user["id"]
        result = UserService._api.post(path, user) 
        return result["document"]

    def __login(self, email, password):
        """ Authenticates the user.
        Should not be used outside of this module as most logins should be with a school.
        """
        # https://firebase.google.com/docs/reference/rest/auth
        url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDg_L6PD2cbSSFUTEpET56VOVKJaGWm5Nc"
        result_json = requests.post(
            url=url,
            data={'email': email, 'password': password, 'returnSecureToken': True}
        )
        # format the response to a dict
        result = json.loads(result_json.text)
        # error will be received if bad password, account not found... probably more
        if "error" in result:
            login_result = {"error": "Failed to authenticate"}
        
        else: 
            # this is the user's UID
            uid = result["localId"]
            # not sure what to do with this but it may come in handy later
            token = {
                "idToken": result["idToken"],
                "refreshToken": result["refreshToken"],
                "expiresIn": result["expiresIn"]
            }
            login_result = {"uid": uid, "token": token}
        
        return login_result

    def login(self, email, password, school_id):
        # authenticate the user, get their uid and login token
        login = self.__login(email, password)
        uid = login["uid"]
        token = login["token"]

        # then check to make sure that the user belongs to the school
        path = "Schools/" + school_id + "/UserProfiles/" + uid
        user_profile = UserService._api.get(path)
        if user_profile:
            login_result = {"user": user_profile, "token": token}
        else:
            login_result = {"error": "No user at school"}
        return login_result
    
    def logout(self, email):
        return False

    def signup(self, email, password):
        user = auth.get_user_by_email(email)
        auth.update_user(user.uid, password=password)

    def generate_verification_link(self, user_email):
        link = auth.generate_email_verification_link(user_email)
        return link

    def invite_users_bulk(self, users, school_id):
        return False

    def generate_password_reset_link(self, user_email):
        link = auth.generate_password_reset_link(user_email)
        return link

    def is_verified(self, user_email):
        verified = False
        user = auth.get_user_by_email(user_email)
        if user.email_verified:
            verified = True
        return verified

    def get_user_document(self, user_id, school_id):
        """Gets the user's information from the api.

        Args:
            user_id: The id of the user.
            school_id: The id of the school.

        Returns:
            Returns a dictionary with the user's information.
        """
        path = "Schools/" + school_id + "/UserProfiles/" + user_id

        user_document = UserService._api.get(path)

        return user_document

    def update_user_profile(self, user_id, school_id, data):
        """Replaces the user's old data with the new data for the field or
        creates it if it doesn't exist.

        Args:
            user_id: The id of the user whose profile is being updated.
            school_id: The id of the school.
            data: A dictionary containing a key of the string of the field in
            the profile to be updated or created and the value to place in that
            field.

        Returns:
            Returns a boolean value. True if the user_profile was successfully
            updated to be the value in data. False if it was not.
        """
        path = "Schools/" + school_id + "/UserProfiles/" + user_id
        UserService._api.post(path, data)

        user_profile = UserService._api.get(path)

        success = True
        for field in data:
            if user_profile[field] != data[field]:
                success = False

        return success

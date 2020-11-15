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
        # otherwise, there should be the information that we want in the result
        else: 
            # this is the user's UID
            uid = result["localId"]
            # not sure what to do with this but it may come in handy later
            token = {
                "idToken": result["idToken"],
                "refreshToken": result["refreshToken"],
                "expiresIn": result["expiresIn"]
            }
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

    def invite_user(self, user, school_id):
        # link = auth.generate_email_verification_link(user["email"])
        return False

    def invite_users_bulk(self, users, school_id):
        return False

    def reset_password(self, user):
        # link = auth.generate_password_reset_link(user["email"])
        return False

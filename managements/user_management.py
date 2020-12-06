from managements.application_management import ApplicationManagement
from services.user_service import UserService

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PRIVILEGE = {"standard": 2, "admin": 1, "super_admin": 0}

PORT = 465  # For SSL
SENDER_MAIL = "wordflow2020@gmail.com"
PASSWORD = "fc8Zspv84phbT8J"

# Create a secure SSL context
CONTEXT = ssl.create_default_context()


class UserManagement(ApplicationManagement):
    """
    NOTE ABOUT HANDLING ERRORS:
    - this is not really a level for "debugging"- we don't want the client to
    see memory locations and stuff,
      see examples for format but try to send clients *just* enough information
      that they know what's going on,
      but not enough to hack your system.
    - Errors are returned in the format of {"error": "<error message>"} and
    shouldn't be exception message
    """

    _service = UserService()

    # used in the Firestore UserProfile:
    _USER_PROFILE_FIELDS = {
        "email": ["required|id"],
        "id": ["required"],
        "display_name": [],
        "privilege_level": ["required|id"]
    }
    # used for the actual authentication
    _USER_AUTH_FIELDS = {
        "email": ["required"],
        "id": [],
        "password": ["required|id"],
        "phone": [],
        "display_name": []
    }

    def create_auth_user(self, email, password=None, display_name=None):
        """ Creates the user for auth purposes *only*.
        Unless this is the school's first user, probably use create_school_user
        instead
        Returns: the user object with email, display_name, and id attributes
        """
        # what is being sent to Firestore
        user_data = {
            "email": email,
            "password": password,
            "display_name": display_name
        }
        # validate user then create their auth account
        valid_user = self._validate_user(user_data,
                                         UserManagement._USER_AUTH_FIELDS)
        if valid_user:
            user_result = self._service.create_user(valid_user)

            # grab the id and wipe the password
            try:
                # if the create/login was success, will have uid
                valid_user["id"] = user_result["uid"]
            except Exception as e:
                # this would be the case where they try to create the same user
                # but at a different school, but use the wrong password
                return {"error": str(e)}
            del valid_user["password"]
            return valid_user
        else:
            # NOTE: Catch this with "if 'error' in result: display_message(result['error'])"
            return {"error": "Failed to create user credentials"}

    def create_user_profile(
        self,
        email,
        uid,
        privilege_level=PRIVILEGE["standard"],
        display_name=None,
    ):
        """ Creates the user profile in the database with default standard
        privilege level
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
        valid_user = self._validate_user(user_data,
                                         UserManagement._USER_PROFILE_FIELDS)
        try:
            if valid_user:
                response = self._service.create_user_profile(
                    valid_user, school_id)
                if response["id"] == uid:
                    result = user_data
        except:
            pass
        return result

    def create_school_user(self,
                           email,
                           privilege_level=PRIVILEGE["standard"],
                           password=None,
                           display_name=None):
        """Create both an auth account and a user profile.
        Returns the user object, or False on failure
        Import PRIVILEGE to use PRIVILEGE["standard" | "admin" | "super_admin"]- default to standard

        """
        try:
            # the auth and user profile funcs both validate user so don't bother here too
            # do the auth first
            auth_user = self.create_auth_user(email, password, display_name)

            # and then do the profile
            user_data = self.create_user_profile(email, auth_user["id"],
                                                 privilege_level, display_name)

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
            UserManagement._context.set_user(privilege_level, user_uid,
                                             school_id, email,
                                             current_user["token"])
            result = user_profile
        else:
            # if there's no user in the result, there'll be an error instead
            result = current_user
        return result

    def logout(self):
        UserManagement._context.reset_context()
        # TODO: There is more to this function than just resetting the context

    def signup(self, email, password):
        """
        Finishes setting up the invited user's account.

        Args:
            email: The invited user's email.
            password: The invited user's password.

        Return:
             Returns True if the account was successfully set up, otherwise
             sends a string stating why the account wasn't successfully set up.
        """
        try:
            verified = UserManagement._service.is_verified(email)
            if verified:
                UserManagement._service.signup(email, password)
                result = True
            else:
                result = ("Email is not verified. Please verify your email to"
                          " sign up.")
        except Exception as e:
            result = str(e)
        return result

    def update_current_user_profile(self, new_field_value, new_field):
        """Updates the user who is logged in's profile.

        Args:
            new_field_value: The updated information for the field.
            new_field: A string of the field being updated.
        """
        user_id = UserManagement._context.get_user_uid()
        school_id = UserManagement._context.get_school_id()
        name_data = {new_field: new_field_value}

        UserManagement._service.update_user_profile(user_id, school_id,
                                                    name_data)

    def update_privilege(self, user, new_privilege_level):
        """Change the privilege of the user.

        Args:
            user: A dictionary of information of the user whose privilege is
            being changed.
            new_privilege_level: The new privilege level of the user.
        """
        user_id = user["id"]
        school_id = UserManagement._context.get_school_id()
        new_privilege = PRIVILEGE[new_privilege_level]
        privilege_data = {"privilege_level": new_privilege}

        if user["privilege_level"] == new_privilege:
            message = ("Privilege level failed. User already has this level of"
                       " privilege!")
        else:
            updated = UserManagement._service.update_user_profile(
                user_id, school_id, privilege_data)
            if updated:
                message = ("Change successful! The privilege level of the user"
                           " has been changed to " + new_privilege_level + "!")
            else:
                message = "Change failed."
        return message

    def remove_user(self):
        pass

    @staticmethod
    def _validate_user(user, fields):
        """ Makes sure user has fields for UserProfile
        Not very thorough. Will also make sure that the user has a valid
        privilege level.
        Defaults to standard.
        """
        for field in fields:
            if field not in user:
                user[field] = None
        # set default for user privilege. We're going with standard...
        # if user["privilege_level"] not in PRIVILEGE.values():
        if "privilege_level" in fields and user[
                "privilege_level"] not in PRIVILEGE.values():
            user["privilege_level"] = PRIVILEGE["standard"]

        return user

    def get_logged_in_user_profile(self):
        """Gets the profile of the logged in user."""

        user_id = UserManagement._context.get_user_uid()
        school_id = UserManagement._context.get_school_id()

        user_profile = UserManagement._service.get_user_document(
            user_id, school_id)

        return user_profile

    def send_invite_email(self, user):
        """Sends the user an invite email containing an email verification link.

        Args:
            user: A dictionary containing information of the user that the
            invite email is being sent to.

        Returns:
             Returns True if the email was successfully sent, otherwise returns
             a string stating why the email wasn't successfully sent.
        """
        try:
            receiver_mail = user["email"]
            school_id = UserManagement._context.get_school_id()

            link = UserManagement._service.generate_verification_link(
                receiver_mail)

            message = MIMEMultipart("alternative")
            message["Subject"] = "Email Verification"
            message["From"] = SENDER_MAIL
            message["To"] = receiver_mail

            verification_text = ("""
            Hello,

            You have been registered in school: """ + school_id + """
            Follow this link to verify your email address: """ + link + """
            Afterwards sign up to finish setting up your account and log in to
            get started.
            If you're not sure why you've received this, you can ignore this
            email.

            Thank you,
            Word Flow
            """)

            email_body = MIMEText(verification_text, 'plain')
            message.attach(email_body)

            with smtplib.SMTP_SSL("smtp.gmail.com", PORT,
                                  context=CONTEXT) as server:
                server.login(SENDER_MAIL, PASSWORD)

                server.sendmail(SENDER_MAIL, receiver_mail,
                                message.as_string())
            email_sent = True
        except Exception as e:
            email_sent = str(e)
        return email_sent

    def send_reset_password_email(self):
        """Sends the user who is logged in an email containing a reset password
        link.

        Returns:
            Returns True if the email was successfully sent, otherwise returns a
            string stating why the email wasn't successfully sent.
        """
        try:
            receiver_mail = self._context.get_user_email()

            link = UserManagement._service.generate_password_reset_link(
                receiver_mail)

            message = MIMEMultipart("alternative")
            message["Subject"] = "Email Verification"
            message["From"] = SENDER_MAIL
            message["To"] = receiver_mail

            verification_text = ("""
            Hello,

            Follow this link to reset your password: """ + link + """
            If you're not sure why you've received this, you can ignore this
            email.

            Thank you,
            Word Flow
            """)

            email_body = MIMEText(verification_text, 'plain')
            message.attach(email_body)

            with smtplib.SMTP_SSL("smtp.gmail.com", PORT,
                                  context=CONTEXT) as server:
                server.login(SENDER_MAIL, PASSWORD)

                server.sendmail(SENDER_MAIL, receiver_mail,
                                message.as_string())
            email_sent = True
        except Exception as e:
            email_sent = str(e)

        return email_sent

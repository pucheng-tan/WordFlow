import requests
from firebase_admin import auth, db
from firebase_admin.auth import UserRecord

from initialize_firebase_admin import app

# I am running this from the "Authentication" folder fyi
# DOCS: https://firebase.google.com/docs/reference/admin/python/
# TUTORIAL: https://medium.com/better-programming/user-management-with-firebase-and-python-749a7a87b2b6


def delete_user(email):
    # Getting a user by their email
    existing_user = auth.get_user_by_email(email)
    # Deleting a user by their user id
    auth.delete_user(existing_user.uid)


def auth_user(email, password):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDg_L6PD2cbSSFUTEpET56VOVKJaGWm5Nc"
    x = requests.post(url=url,
                      data={
                          'email': email,
                          'password': password,
                          'returnSecureToken': True
                      })
    print(x.text)
    # TODO: Truthiness doesn't work this way in python.
    result = False if x.text.error else True
    print(result)

    if result:
        user = auth.get_user_by_email(email)
        print(user.email)
    else:
        print("Nope!")


if __name__ == "__main__":
    email = "test2@test.com"
    # user_id = "1234588"
    password = "bad2_password"
    user_type = "super-admin"

    try:
        # Creating a user with an email and a password- different parameters are available!
        new_user = auth.create_user(email=email, password=password)

        print(new_user.email)
        print('Firebase successfully created a new user with email: ' +
              new_user.email + 'and user id:' + new_user.uid)
        pass
    except auth.EmailAlreadyExistsError as identifier:
        print(identifier)
        auth_user(email, password)
        # delete_user(email)
        pass

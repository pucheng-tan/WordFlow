import firebase_admin
from firebase_admin import credentials

cred = firebase_admin.credentials.Certificate(
    './python-admin/cmpt370-group2-firebase-adminsdk-lno8j-b5a0b9573b.json')
app = firebase_admin.initialize_app(cred)
# app = firebase_admin.initialize_app()

if __name__ == "__main__":
    print(app)

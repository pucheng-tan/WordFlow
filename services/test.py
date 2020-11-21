# from api_service import API
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
# from firebase_admin import auth
# from datetime import datetime, timezone
# from user import User, PrivilegeLevel
from challenge_service import ChallengeService

# JUST A TEMPORARY FILE USED FOR EXPERIMENTATION WITH API STUFF
# DON'T MIND ME
# api = API()
# db = API._get_db()
service = ChallengeService()

SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"
TEST_SCHOOL_ID = SCHOOL_ID
CLASSROOM_ID = "uWkea95OBZ1d94kaPThK"
USER_ID = "BMSoKUzVnRYn103t2Oi6Nacv9X03"
TARA_USER_ID = "kUJrBZtlYJeU8ZLAFFcm4dAJVBt2"
email = "pucheng@hotmail.yea"

def get_challenge_content():
    content = service.get_challenge_content(0, 0)
    print(content)

get_challenge_content()
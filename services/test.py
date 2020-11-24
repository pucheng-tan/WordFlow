
from challenge_service import ChallengeService


# # JUST A TEMPORARY FILE USED FOR EXPERIMENTATION WITH API STUFF
# # DON'T MIND ME
service = ChallengeService()

# SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"
# TEST_SCHOOL_ID = SCHOOL_ID
# CLASSROOM_ID = "uWkea95OBZ1d94kaPThK"
# USER_ID = "BMSoKUzVnRYn103t2Oi6Nacv9X03"
# TARA_USER_ID = "kUJrBZtlYJeU8ZLAFFcm4dAJVBt2"
# email = "pucheng@hotmail.yea"

def get_challenge_content():
    content = service.get_challenge_content(0, 0)
    print(content)


def interpret_text_content():
    data = {'8v6jRhTybexEPrqEQvVl': {'text_content': 'Once upon a time there was standard content', 'index': 0, 'CharCount': 34}}
    content = list(data.values())[0]["text_content"]
    print(content)

def get_max_index():
    max = service.get_mode_count(0)
    print(max)

get_max_index()
# interpret_text_content()

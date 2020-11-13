import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from user_service import UserService
from datetime import datetime, timezone

from user import PrivilegeLevel as PRIV
user_service = UserService()

TEST_SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"
TEST_POST_SCHOOL_ID = "Test_Post_School"
TEST_CLASSROOM_ID = "uWkea95OBZ1d94kaPThK"
TEST_USER_ID = "BMSoKUzVnRYn103t2Oi6Nacv9X03"
TEST_USER_ID_SUPER = "kUJrBZtlYJeU8ZLAFFcm4dAJVBt2"
TEST_USER_ID_ADMIN = "mCj2ZrYMbbeRpYp3aRof9EjfKkg1"
TEST_DATE = datetime(2020, 10, 30, tzinfo=timezone.utc)# November 1

@pytest.mark.api_call
@pytest.mark.parametrize("user, school_id", [
    ({
        "email": "test_post_user@test.caaaa",
        "password": "Pass123!",
        "display_name": "Test Post User",
        "privilege_level": PRIV.standard
    }, TEST_POST_SCHOOL_ID)
])
def test_create_user(user, school_id, json_metadata):
    result = user_service.create_user(user, school_id)
    uid = result["document"]["id"]
    path = result["document"]["path"]
    expected_path = "Schools/" + TEST_POST_SCHOOL_ID + "/UserProfiles/" + uid
    assert path == expected_path

# @pytest.mark.xfail
# @pytest.mark.api_call
# @pytest.mark.parametrize("user, school_id", [])
# def test_invite_user(user, school_id, json_metadata):
#     result = user_service.invite_user(user, school_id)

# @pytest.mark.xfail
# @pytest.mark.api_call
# @pytest.mark.parametrize("school, users", [])
# def test_invite_user_bulk(school, users, json_metadata):
#     result = user_service.invite_users_bulk(users, school)

# @pytest.mark.xfail
# @pytest.mark.api_call
# @pytest.mark.parametrize("email, password, school_id", [])
# def test_login_user(email, password, school_id, json_metadata):
#     result = user_service.login(email, password, school_id)

# @pytest.mark.xfail
# @pytest.mark.api_call
# @pytest.mark.parametrize("email", [])
# def test_logout_user(email, json_metadata):
#     result = user_service.logout(email)
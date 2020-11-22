import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from user_service import UserService
from datetime import datetime, timezone

user_service = UserService()

TEST_SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"
TEST_POST_SCHOOL_ID = "Test_Post_School"
TEST_CLASSROOM_ID = "uWkea95OBZ1d94kaPThK"
TEST_USER_ID = "BMSoKUzVnRYn103t2Oi6Nacv9X03"
TEST_USER_ID_SUPER = "kUJrBZtlYJeU8ZLAFFcm4dAJVBt2"
TEST_USER_ID_ADMIN = "mCj2ZrYMbbeRpYp3aRof9EjfKkg1"
TEST_DATE = datetime(2020, 10, 30, tzinfo=timezone.utc)# November 1

METADATA_ID = "UserService"

PRIV = {"standard": 2, "admin": 1, "super_admin": 0}

@pytest.mark.api_call
@pytest.mark.parametrize("user, expected_result, detail", [
    ({
        "email": "completely_new_email@test.ca",
        "password": "Val1d_Pa$$word",
        "display_name": "Completely New User"
    }, True, "A completely new user"),
    ({
        "email": "completely_new_email@test.ca",
        "password": "Val1d_Pa$$word",
        "display_name": "ExistingUser"
    }, True, "A user which already exists"),
    ({
        "email": "completely_new_email@test.ca",
        "password": "Val1d_Pa$$word",
        "display_name": "Completely New User"
    }, True, "Display name omitted- should still work"),
    ({
        "email": "completely_new_email.ca",
        "password": "Val1d_Pa$$word",
        "display_name": "Completely New User"
    }, "Invalid email format", "invalid email- not a proper email format"),
    ({
        "email": "test111@test.ca",
        "password": "12345",
        "display_name": "Invalid user"
    }, "Password must be at least 6 characters long", "invalid password- password too short")
])
def test_create_user(user, expected_result, detail, json_metadata):
    json_metadata["id"] = "UT " + METADATA_ID + ".1"
    json_metadata["description"] = "Creating the user auth account: " + detail

    # no matter what, the password should not be returned

    # if success expected, should have id

    # otherwise, should be an error returned

    result = user_service.create_user(user)

    if expected_result == True:
        assert result.email == user["email"]
        assert result.display_name == user["display_name"]
        assert hasattr(result, "uid")
    else:
        assert result["error"] == expected_result

@pytest.mark.api_call
@pytest.mark.parametrize("user, school_id", [
    ({
        "id": "1234",
        "email": "test_post_user@test.caaaa",
        "password": "Pass123!",
        "display_name": "Test Post User",
        "privilege_level": PRIV["standard"]
    }, TEST_POST_SCHOOL_ID)
])
def test_create_user_profile(user, school_id, json_metadata):
    json_metadata["id"] = "UT " + METADATA_ID + ".2"
    json_metadata["description"] = "Creating the user profile"
    result = user_service.create_user_profile(user, school_id)
    uid = result["id"]
    path = result["path"]
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
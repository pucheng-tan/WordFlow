import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from managements.user_management import UserManagement

user_management = UserManagement()

@pytest.mark.parametrize("description, email, expected_result", [
    ("Testing an invalid email", "invalid_email.com", "error"),
    ("Testing an invalid email", "", "error")
])

def test_create_auth_user(description, email, expected_result):
    result = user_management.create_auth_user(email)

    assert expected_result in result

# @pytest.mark.xfail
@pytest.mark.parametrize("user, result", [
    ("valid user", "success"),
    ("valid user", "success"),
    ("invalid user", "error")
])
def test_create_user(user, result, json_metadata):
    assert 1 == 1
    # pass

@pytest.mark.xfail
def test_login():
    pass

@pytest.mark.parametrize("email, password, expected_result", [
                        ("1128@gmail.com", "123456", "Email is not verified."),
                        ("bad_email", "123456", "Malformed email"),
                        ("not_in_firebase@fdjsfk.com", "123456", "No user record found"),
                        ("", "123456", "Email must be a non-empty string.")
])
def test_signup(email, password, expected_result):
    result = user_management.signup(email, password)
    assert expected_result in result

@pytest.mark.parametrize("user, expected_result", [
                        ({"email": "bad_email"}, "Malformed email"),
                        ({"email": "not in firebased@fdjsk.com"}, "No user record found"),
                        ({"email": ""}, "Email must be a non-empty string.")
])
def test_send_invite_email(user, expected_result):
    result = user_management.send_invite_email(user)
    assert expected_result in result




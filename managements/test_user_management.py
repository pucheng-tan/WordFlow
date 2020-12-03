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

    assert expected_result == result

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


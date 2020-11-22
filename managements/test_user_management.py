import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from managements.user_management import UserManagement
from managements.challenge_management import ChallengeManagement
from datetime import datetime, timezone

management = ChallengeManagement()

def test_challenge_management():
    result = management.get_random_challenge_content(0)
    assert result == ""

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
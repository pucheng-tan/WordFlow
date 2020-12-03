import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from managements.challenge_management import ChallengeManagement

# # @pytest.mark.xfail
# @pytest.mark.parametrize("user, result", [
#     ("valid user", "success"),
#     ("valid user", "success"),
#     ("invalid user", "error")
# ])
# def test_create_user(user, result, json_metadata):
#     assert 1 == 1
#     # pass

# @pytest.mark.xfail
# def test_login():
#     pass

@pytest.mark.default
def test_get_challenge_from_different_modes():
    assert ChallengeManagement(0) != ChallengeManagement(1)
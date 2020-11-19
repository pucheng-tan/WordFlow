import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from managements.user_management import UserManagement
from datetime import datetime, timezone

@pytest.mark.xfail
@pytest.mark.parametrize("user, result", [
    ("valid user", "success"),
    ("valid user", "success"),
    ("invalid user", "error")
])
def test_create_user(user, result, json_metadata):
    pass

@pytest.mark.xfail
def test_login():
    pass
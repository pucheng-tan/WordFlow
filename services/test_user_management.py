import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from user_management import UserManagement
from datetime import datetime, timezone

@pytest.mark.parametrize("user, result", [
    ("valid user", "success"),
    ("valid user", "success"),
    ("invalid user", "error")
])
def test_create_user():
    pass

def test_login():
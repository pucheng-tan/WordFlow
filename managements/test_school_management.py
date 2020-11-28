import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from school_management import SchoolManagement
from datetime import datetime, timezone

school_management = SchoolManagement()

TEST_SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"
TEST_POST_SCHOOL_ID = "Test_Post_School"
TEST_CLASSROOM_ID = "uWkea95OBZ1d94kaPThK"
TEST_USER_ID = "BMSoKUzVnRYn103t2Oi6Nacv9X03"
TEST_USER_ID_SUPER = "kUJrBZtlYJeU8ZLAFFcm4dAJVBt2"
TEST_USER_ID_ADMIN = "mCj2ZrYMbbeRpYp3aRof9EjfKkg1"
TEST_DATE = datetime(2020, 10, 30, tzinfo=timezone.utc)# November 1

METADATA_ID = "SchoolManagement"

PRIV = {"standard": 2, "admin": 1, "super_admin": 0}

@pytest.mark.parametrize("school_name, owner_uid", [
                        (TEST_SCHOOL_ID, TEST_USER_ID_SUPER),
                        ])
def test_create_school(school_name, owner_uid, json_metadata):
    result = school_management.create_school(school_name, owner_uid)

    assert result["error"] == "School already exists!"
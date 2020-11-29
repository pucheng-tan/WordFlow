import pytest

from services import school_service

school_service = school_service.SchoolService()

TEST_SCHOOL_ID = "3p1U6xAvKic1RvXMl5nJ"

@pytest.mark.api_call
@pytest.mark.parametrize("test_school_id,privilege_level,expected_result", [
        ("Usask", 0, 1),
        ("Usask", 1, 0),
        ("Usask", 2, 0),
        ("3p1U6xAvKic1RvXMl5nJ", 0, 2),
        ("3p1U6xAvKic1RvXMl5nJ", 1, 2),
        ("3p1U6xAvKic1RvXMl5nJ", 2, 6)])

def test_get_user_documents_by_privilege(test_school_id, privilege_level, expected_result):
    user_documents = school_service.get_user_documents_by_privilege(test_school_id, privilege_level)

    assert(len(user_documents) == expected_result)

    for user in user_documents:
        assert(user_documents[user]["privilege_level"] == privilege_level)

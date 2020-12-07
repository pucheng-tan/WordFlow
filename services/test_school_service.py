import pytest

from services import school_service

# mock = mock_api
school_service = school_service.SchoolService()
# school_service._api = mock

# TEST_SCHOOL_ID = "3p1U6xAvKic1RvXMl5nJ"

@pytest.mark.api_call
@pytest.mark.parametrize("test_school_id,privilege_level,expected_result", [
        ("Usask", 0, 1),
        ("Usask", 1, 0),
        ("Usask", 2, 1),
        ("Mock_School", 0, 4),
        ("Mock_School", 1, 4),
        ("Mock_School", 2, 8)])

def test_get_user_documents_by_privilege(test_school_id, privilege_level, expected_result, mock_api):
    school_service._api = mock_api
    user_documents = school_service.get_user_documents_by_privilege(test_school_id, privilege_level)

    assert(len(user_documents) == expected_result)

    for user in user_documents:
        assert(user_documents[user]["privilege_level"] == privilege_level)
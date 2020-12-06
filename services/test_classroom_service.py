import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata
from services import classroom_service

classroom_service = classroom_service.ClassroomService()

METADATA_ID = "ClassroomService"
TEST_SCHOOL_ID = "3p1U6xAvKic1RvXMl5nJ"


@pytest.mark.api_call
def test_get_classroom_list(json_metadata):
    json_metadata["id"] = "UT " + METADATA_ID + ".1"
    json_metadata["description"] = "Get a list of classrooms"

    school_id = "test_school"
    first_page_names = ["class_1", "class_2"]
    second_page_names = ["class_3"]

    # getting a list of classrooms when we expect to get 2 pages worth back 
    limit = 2
    start_at = " "
    first_page = classroom_service.get_classrooms(school_id, limit, start_at)

    assert len(first_page) == limit
    for classroom in first_page.values():
        assert classroom["name"] in first_page_names

    # get the second page back
    # get the name of the last item in the list
    start_at = (list(first_page.values()))[-1]["name"]
    second_page = classroom_service.get_classrooms(school_id, limit, start_at)

    assert len(second_page) <= limit
    for classroom in second_page.values():
        assert classroom["name"] in second_page_names

def test_get_classroom_list_when_none_exist(json_metadata):
    json_metadata["id"] = "UT " + METADATA_ID + ".2"
    json_metadata["description"] = "Empty list is returned when the first classroom has not been made"

    school_id = "Test_Post_School"

    classrooms = classroom_service.get_classrooms(school_id, 3, " ")
    
    assert not classrooms
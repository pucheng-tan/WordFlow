import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from firebase_admin import firestore
from api_service import APIService
from datetime import datetime, timezone

api = APIService()

TEST_SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"
TEST_CLASSROOM_ID = "uWkea95OBZ1d94kaPThK"
TEST_USER_ID = "BMSoKUzVnRYn103t2Oi6Nacv9X03"
TEST_DATE = datetime(2020, 10, 30, tzinfo=timezone.utc)# November 1



# test valid get queries
@pytest.mark.api_call
@pytest.mark.parametrize("path, where_clause, expected_reference", [
    ({"Schools": TEST_SCHOOL_ID, "UserProfiles": TEST_USER_ID, "History": APIService.WHERE_CLAUSE}, [["Mode", "==", "0"]], "2020101513071234"),
    ({"History": APIService.SEARCH_ALL}, [["UserProfile", "==", "BMSoKUzVnRYn103t2Oi6Nacv9X03"], ["AssignmentID", "exists"]], "2020101513091234"),
    ({"Schools": TEST_SCHOOL_ID, "Classrooms": APIService.WHERE_CLAUSE}, [["Members", "array_contains", TEST_USER_ID]], "uWkea95OBZ1d94kaPThK"),
    ({"Schools": TEST_SCHOOL_ID, "Classrooms": TEST_CLASSROOM_ID}, [], TEST_CLASSROOM_ID),
])
def test_get_valid(path, where_clause, expected_reference, json_metadata):
    json_metadata['id'] = "UT API.1"
    json_metadata['description'] = "Testing various valid 'get' queries with the API"
    
    # Parameters:
    # 1. path: Schools (School X), User Profiles (Pucheng), History. Where: [Date Completed > Nov 1st midnight, Mode == 0, UserProfile in [doc ref: "/Schools/x school/UserProfiles/pucheng"]]
    # ["DateCompleted", ">", TEST_DATE],,   ["Duration", "in", [120]]
    # 2. path: Collection Group: History. Where: [UserProfile == "pucheng"]
    # 3. path: Schools (School X), Classrooms. Where: [Members array-contains pucheng]
    # 4. path: Schools (School X), Classroms (X Classroom). 
    
    # perform the query
    pytest.set_trace()
    results = api.get(path, where_clause)

    # if there is a where clause, results will come back in a list
    if len(where_clause) > 0:
        results = list(results)
        assert len(results) == 1
        document_reference = results[0].reference

    else:
        document_reference = results.reference

    assert document_reference == expected_reference

    
# test invalid get queries
@pytest.mark.api_call
@pytest.mark.parametrize("path, where_clause", [
    ({"Schools": TEST_SCHOOL_ID, "UserProfiles": TEST_USER_ID, "History": APIService.WHERE_CLAUSE}, ["Mode", "==", 0]),
    ({"History": APIService.SEARCH_ALL}, []),
    ({0: TEST_SCHOOL_ID}, [])
])
def test_get_invalid(path, where_clause, json_metadata):
    json_metadata['id'] = "UT API.2"
    json_metadata['description'] = "Testing 'get' queries return expected errors with invalid params"

    # 1. Invalid because where clause should be in a [[]]
    # 2. Invalid because SEARCH_ALL requires a where clause
    # 3. Invalid because collection name must be string

    with pytest.raises(TypeError, match="Invalid query"):
        api.get(path, where_clause)

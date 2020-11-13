import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata

from api_service import API
from datetime import datetime, timezone

api = API.get_api()

TEST_SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"
TEST_POST_SCHOOL_ID = "Test_Post_School"
TEST_CLASSROOM_ID = "uWkea95OBZ1d94kaPThK"
TEST_USER_ID = "BMSoKUzVnRYn103t2Oi6Nacv9X03"
TEST_USER_ID_SUPER = "kUJrBZtlYJeU8ZLAFFcm4dAJVBt2"
TEST_USER_ID_ADMIN = "mCj2ZrYMbbeRpYp3aRof9EjfKkg1"
TEST_DATE = datetime(2020, 10, 30, tzinfo=timezone.utc)# November 1

# test valid get queries
@pytest.mark.api_call
@pytest.mark.parametrize("params, expected_references", [
    # for optional fields: try different valid-type values that evaluate to false ([], 0, "", None)
    ({
        "path": "Schools/" + TEST_SCHOOL_ID + "/UserProfiles/" + TEST_USER_ID + "/History/",
        "where_clauses": [["DateCompleted", ">", TEST_DATE], ["Mode", "==", 0], ["Duration", "in", [120]]],
        "limit": None,
        "order_by": [],
        "meta": "History of specific user: filter with <, ==, and in"
    }, ["2020101513071234"]), # params0: PASS
    ({
        "collection_name": "History",
        "where_clauses": [["UserProfile", "string_starts", "Schools/" + TEST_SCHOOL_ID]],
        "limit": 0,
        "order_by": [{"AssignmentID": True}],
        "meta": "get_all for History collection: filter by the school, sort ascending the assignment ID. Test that passing in a sort which should be incompatible with the where clauses is handled gracefully"
    }, ["2020101513091234"]), # params1: PASS
    ({
        "path": "/Schools/" + TEST_SCHOOL_ID + "/Classrooms/",
        "where_clauses": [["Members", "array_contains", "Schools/" + TEST_SCHOOL_ID + "/UserProfiles/" + TEST_USER_ID]],
        "limit": 0,
        "order_by": None,
        "meta": "filter collection by array contains specified document reference"
    }, ["uWkea95OBZ1d94kaPThK"]), # params2: TypeError
    ({
        "path": "Schools/" + TEST_SCHOOL_ID + "/Classrooms/" + TEST_CLASSROOM_ID,
        "where_clauses": [],
        "limit": 0,
        "order_by": None,
        "meta": "get a specific document by its path/reference"
    }, [TEST_CLASSROOM_ID]), # params3: PASS
    ({
        "path": "Schools/" + TEST_SCHOOL_ID + "/UserProfiles",
        "where_clauses": None,
        "limit": None,
        "order_by": [{"DisplayName": False}],
        "meta": "get all documents in a collection with a descending sort"
    }, [TEST_USER_ID, TEST_USER_ID_ADMIN, TEST_USER_ID_SUPER]) # params4: PASS
])
def test_get_valid(params, expected_references, json_metadata):
    json_metadata['id'] = "UT API.1"
    json_metadata['description'] = "Testing various valid 'get' queries with the API: " + params["meta"]
       
    where_clauses = params["where_clauses"]
    limit = params["limit"]
    order_by = params["order_by"]

    actual_results_count = 0

    # perform the query. Different call if there is a "path" parameter
    if "path" in params: # get
        path = params["path"]
        results = api.get(path, where_clauses, order_by, limit)        

    else: # get_all 
        collection_name = params["collection_name"]
        results = api.get_all(collection_name, where_clauses, order_by, limit)

    # single result
    if "id" in results:
        results = [results["id"]]
        # this may look like an assumption, but the "id" would break if it's not 1
        actual_results_count = 1

    # multiple results
    else:
        results = list(results)
        actual_results_count = len(results)
    
    # verify that the right number of results came back
    assert actual_results_count == len(expected_references)

    # and then verify that the expected results are all in the returns
    for reference in expected_references:
        assert reference in results
    

# test invalid get queries
@pytest.mark.api_call
@pytest.mark.parametrize("params", [
    # Invalid data but with valid types
    ({
        "path": "Schools/" + TEST_SCHOOL_ID + "/UserProfiles/" + TEST_USER_ID,
        "collection_name": "History",
        "where_clauses": None,
        "limit": -1,
        "order_by": {},
        "meta": "invalid limit"
    }),
    ({
        "collection_name": "History",
        "where_clauses": ["Mode", "==", 0],
        "limit": 0,
        "order_by": {},
        "meta": "where clause should be nested"
    }),
    ({
        "path": "Schools" + TEST_SCHOOL_ID,
        "collection_name": "UserProfiles",
        "where_clauses": [["PrivilegeLevel", ">", 0], ["DisplayName", "string_starts",]],
        "limit": None,
        "order_by": None,
        "meta": ""
    })
])
def test_get_invalid(params, json_metadata):
    json_metadata['id'] = "UT API.2"
    json_metadata['description'] = "Testing 'get' queries return expected errors with invalid params: " + params["meta"]
    
    where_clauses = params["where_clauses"]
    limit = params["limit"]
    order_by = params["order_by"]

    # all of them are invalid queries and should throw that exception
    with pytest.raises(TypeError, match="Invalid query"):
        if "path" in params:
            path = params["path"]
            api.get(path, where_clauses, order_by, limit)
        else:
            collection_name = params["collection_name"]
            api.get_all(collection_name, where_clauses, order_by, limit)

@pytest.mark.api_call
def test_post_valid(json_metadata):
    json_metadata['id'] = "UT API.3"
    json_metadata['description'] = "Testing 'post' queries with all the datatypes available"
    # TODO: There needs to be a setup that kills this collection or a mock setup
    
    path = "Albatross/AlbatrossID/Bat/BatID/Capybara/"
    data = {
            "id": "CapybaraID", 
            "Boolean": True, 
            "Date": TEST_DATE, 
            "Number": 3.14159, 
            "Array": [5, False, "cheese"], 
            "None": None, 
            "object": {
                "Dog": 6, 
                "Emu": {
                    "Fox": [1, 2, 3]
                }
            }
        }
    # post it, grab the id and the path from the post results
    result = api.post(path, data)
    document_id = result["document"]["id"]
    document_path = result["document"]["path"]

    # path and id should be as given
    assert document_id == data["id"]
    assert document_path == path + document_id

    # try getting the object, the object should be the same as what was posted
    get_result = api.get(document_path)
    assert get_result == data



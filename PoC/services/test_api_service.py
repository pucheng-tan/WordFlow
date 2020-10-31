import pytest
import warnings
from pytest_jsonreport.plugin import JSONReport, json_metadata

from api_service import APIService

# ALL THIS WALL OF TEXT IS INFO ABOUT PYTEST

# Documentation and stuff
# pytest marks: https://docs.pytest.org/en/stable/mark.html
# pytest assertions: https://docs.pytest.org/en/stable/assert.html

# CREATING TESTS:

    # Test file names must start with "test_"
    # Test file names should generally be in the format test_file_being_tested.py
    # Use json_metadata to report more information about tests (NOTE: json_metadata has to be passed into the function!)
    # json_metadata['id'] = "<test type> <issue>.<number>"
    # test type = IT, UT, ET (integration, unit, end-to-end test)
    # issue = the issue in GitLab
    # number = give them numbers
    # json_metadata['description'] = use to give short summary of purpose, coverage of test, reference a requirement it tests

# MARKING TESTS:

    # parametrize: use to run tests multiple times with different parameters
    # xfail: use to mark a test as not completely written
    # api_call: use to mark test as one that makes call to external api
    # fixture: use to mark a function as a fixture that is used by other tests 
        # ex: if several functions use the same value in the tests, mark it as a fixture and use the name as a variable
        # it didn't like it when I tried to make the api a fixture, so it seems there are limitations

# RUNNING TESTS: 

    # Test single file: pytest <file_name>
    # OR:
    # Test all files in directory (and subdirectories): pytest <file_path>

    # Useful switches:
    # Verbose = -v: "pytest test_path -v"
    # Marks = -m <args>: "pytest test_path -m api_call" run only tests marked with api_call
        # OR: "pytest test_path -m "not api_call"" to exclude tests marked with api_call. "" around not and the mark name
        # https://docs.pytest.org/en/stable/example/markers.html for further examples
        # Create a custom mark by adding it to the pytest.ini file located in the top level of the repository
    # Keyword(??) = -k <args>: "pytest test_path -k get_collection" runs test with "get collection" in the name of the test

# LOGGING TEST RESULTS:

    # pytest's file logging does not record the passes, so use external plugin: https://pypi.org/project/pytest-json-report/
    # running pytest will generate a log (this is set in pytest.ini, and configured in conftest)
        # a file .report.json will be generated with results in group2
        # It has a "success" field that checks that the test was run at the root, there are no warnings, and everything passed.
        # If you run into bugs with that, check out conftest.py, possibly the pytest.ini

# to-do list of planned test coverage. Once it is to-done, it is documentation of test coverage
""" Test API Service: verify functions in base API service class
Test Coverage:
    Integration:
    - "get" functionality using queries with:
        - collection, document reference, single where clause
        - TODO: collection_group, composite where clauses, "array contains" where clause, order_by, limit
    - TODO: "post" functionality is more simple: set documents in collections and subcollections, update, delete
    Units:
    - TODO: functions will be added to this list as the functions and the tests are written
    NOTE:
    - tests are written with current database values in mind, which are example data. Adding real values will affect tests.
"""

api = APIService()

@pytest.mark.api_call # Use custom mark to be able to filter tests run based on conditions. This one makes an api call.
@pytest.mark.parametrize("collection, where", [("Schools", [["Name", "==", "X School"]]), ("Schools", [["Name", "exists"]])])
def test_get_collection_valid(collection, where, json_metadata):
    json_metadata['id'] = "IT API.1"
    json_metadata['description'] = "valid query will retrieve valid results"

    # NOTE on the metadata: IT = "Integration Test", Unit Test would be UT. "API" refers to the issue, which for this has not been created
    # adding it to the json_metadata outputs it to the report

    params = {collection: {"where": where}}
    schools = api.get(params)
    list_schools = list(schools.values())

    assert len(list_schools) == 1
    assert list_schools[0]["Name"] == "X School"

    warnings.warn("this test will break when we add another school")


@pytest.mark.api_call
@pytest.mark.parametrize("collection, where", [(3, "invalid where clause"), ("valid_collection_name", 4)])
def test_get_collection_invalid(collection, where, json_metadata):
    json_metadata['id'] = "IT API.2"
    json_metadata['description'] = "invalid queries of wrong data types will raise the expected Exceptions"

    # NOTE This is where we are *expecting* an Exception. For the test to pass, the process must raise a TypeError exception, 
    # and the message must match the regex pattern (can be a simple string like in this case)
    with pytest.raises(TypeError, match="Bad query"):
        params = {collection: {"where": where}}
        api.get(params)

@pytest.mark.api_call
@pytest.mark.parametrize("collection, where", [("Schools", [["Name", "==", "lkjdsafnlaqk346q9y"]])])
def test_get_collection_no_result(collection, where, json_metadata):
    json_metadata['id'] = "IT API.3"
    json_metadata['description'] = "valid query not pointing to an existing document will return empty result"
    
    params = {collection: {"where": where}}
    result = api.get(params)
    
    assert result == {}

    warnings.warn("we'll want a mock here")

@pytest.mark.xfail
def test_get_where_clause(json_metadata):
    json_metadata['id'] = "UT API.1"
    json_metadata['description'] = "pass in data to the _get_where_clause function, see if result is as expected without API call"
    pass

@pytest.mark.xfail
def test_get_subcollection():
    """
    NOTE: Use xfail mark when the test hasn't been completely written yet.
        - it will be listed either as "xfailed" or "xpassed" in test summary
        - so, testing is not done if you still have xfail or xpass in test summary
    XFAIL: expected to fail
        - these tests are still run, but without any traceback reported when it fails
        - this one has an assert that makes it fail, so it is listed as "xfailed" in summary
        - other tests have no content, so do not actually fail. They are listed as "xpassed" in summary
    """
    # use pytest.fail to fail a test with a given message
    pytest.fail("this test hasn't been written yet, so it's marked with xfail. It will be counted towards xpass results in summary, and not actually ran")
    pass

@pytest.mark.xfail
def test_get_reference_by_field():
    pass

@pytest.mark.xfail
def test_limit():
    pass

@pytest.mark.xfail
def test_order_by():
    pass

@pytest.mark.xfail
def test_combination():
    pass

@pytest.mark.xfail
def test_post():
    pass

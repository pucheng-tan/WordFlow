import pytest
import warnings
import requests
import json
from _test_base_class import TestBaseClass
from api_service import APIService

# Testing the API Service Class 

# Areas to cover: 
# 1. Get use cases: getting data from the database using different types of queries
    # a. Correct queries return data as expected
    # b. Incorrect queries return the expected type of Exception and appropriate error message
    # c. Queries with no results, return no results
    # d. Different query types: collection, document, collection_group, where clauses (single, composite, <= types and array contains), order_by, and limit 

# TODO LIST: 
# 1. DONE: figure out how to run all of the tests at once. (RUN PYTEST ON THE FOLDER. It will find all the tests in subfolders) 
# 2. Use a config file? Make a custom mark? 
# 3. Get the API service to execute the query of "for X School, find all History collections in UserProfiles and return the documents"

class TestAPIService(TestBaseClass):
    """ Test API Service: verify functions in base API service class
    Test Coverage:
        Integration:
        TODO - "get" functionality using query combinations of: [collection, document, collection_group, where, order_by, limit]
        where to also include single & composite where clauses, including "array contains" which has limitations in firestore
        TODO - "post" functionality is more simple: set documents in collections and subcollections, update, delete
        Units:
        TODO - functions will be added to this list as the functions and the tests are written
        NOTE:
        - tests are written with current database values in mind, which are example data. Adding real values will affect tests.
    """

    api = APIService()


    @pytest.mark.api_call # Use custom mark to be able to filter tests run based on conditions. This one makes an api call.
    @pytest.mark.parametrize("collection, where", [("Schools", [["Name", "==", "X School"]]), ("Schools", [["Name", "exists"]])])
    def test_get_collection_valid(self, collection, where):
        """ Test Case: IT API.1
        This test verifies that a valid query will retrieve valid results.
        Requirement: refers to functional requirement x
        """
        # NOTE on the comment: IT = "Integration Test", Unit Test would be UT. "API" refers to the issue, which for this has not been created

        params = {collection: {"where": where}}
        schools = self.api.get(params)
        list_schools = list(schools.values())

        assert len(list_schools) == 1
        assert list_schools[0]["Name"] == "X School"

        # warnings.warn("we'll want a mock here, and also this test will break when we add another school")


    @pytest.mark.parametrize("collection, where", [(3, "invalid where clause"), ("valid_collection_name", 4)])
    def test_get_collection_invalid(self, collection, where):
        """ Test Case: IT API.2
        Looks at results where queries are passed in with invalid arguments of the wrong type
        """

        # NOTE This is where we are *expecting* an Exception. For the test to pass, the process must raise a TypeError exception, 
        # and the message must match the regex pattern (can be a simple string)
        with pytest.raises(TypeError, match="Bad query"):
            params = {collection: {"where": where}}
            self.api.get(params)

        # warnings.warn("we'll want a mock here")

    @pytest.mark.parametrize("collection, where", [("Schools", [["Name", "==", "lkjdsafnlaqk346q9y"]])])
    def test_get_collection_no_result(self, collection, where):
        """ Test Case: IT API.3
        Condition where a valid query is limited such that no results are expected to be returned
        """
        params = {collection: {"where": where}}
        result = self.api.get(params)
        
        assert result == {}

        # warnings.warn("we'll want a mock here")

    def test_get_document(self):
        params = {"Schools": {"reference": self.TEST_SCHOOL_ID}}
        school = self.api.get(params)

        assert len(school) == 1, "single result expected with get document by reference"
        assert school["Name"] == "X School"

    # @pytest.mark.xfail
    # def test_get_subcollection(self):
    #     """
    #     NOTE: Use xfail mark when the test hasn't been completely written yet.
    #         - it will be listed either as "xfailed" or "xpassed" in test summary
    #         - so, testing is not done if you still have xfail or xpass in test summary
    #     XFAIL: expected to fail
    #         - these tests are still run, but without any traceback reported when it fails
    #         - this one has an assert that makes it fail, so it is listed as "xfailed" in summary
    #         - other tests have no content, so do not actually fail. They are listed as "xpassed" in summary
    #     """
    #     self.fail("this test hasn't been written yet, so it's marked with xfail. It will be counted towards xpass results in summary, and not actually ran")
    #     pass

    # @pytest.mark.xfail
    # def test_get_reference_by_field(self):
    #     pass

    # @pytest.mark.xfail
    # def test_limit(self):
    #     pass

    # @pytest.mark.xfail
    # def test_order_by(self):
    #     pass

    # @pytest.mark.xfail
    # def test_combination(self):
    #     pass

    # @pytest.mark.xfail
    # def test_post(self):
    #     pass

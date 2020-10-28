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
# 1. DONE: figure out how to run all of the tests at once. (RUN PYTEST ON THE FOLDER) 
# 2. Use a config file? Make a custom mark? 
# 3. Get the API service to execute the query of "for X School, find all History collections in UserProfiles and return the documents"

class TestAPIService(TestBaseClass):

    api = APIService()

    @pytest.mark.parametrize("collection, where", [("Schools", [["Name", "==", "X School"]]), ("Schools", [["Name", "exists"]])])
    def test_get_collection_valid(self, collection, where):
        """ This test verifies that a valid query will retrieve valid results.
        Requirement: refers to functional requirement x
        Test Case: 23423.098
        """

        # params = {"collection": collection, "where": where}
        params = {collection: {"where": where}}
        schools = self.api.get(params)
        list_schools = list(schools.values())

        assert len(list_schools) == 1
        assert list_schools[0]["Name"] == "X School"

        warnings.warn("we'll want a mock here, and also this test will break when we add another school")


    @pytest.mark.parametrize("collection, where", [(3, "invalid where clause"), (["string1", "string2"], 4)])
    def test_get_collection_invalid(self, collection, where):
        try:
            params = {collection: {"where": where}}
            result = self.api.get(params)
        except TypeError as e:
            assert isinstance(e, TypeError)
            assert e.args[0] == "Bad query"
        except Exception as e:
            message = "Wrong exception: " + str(type(e)) + " " + e.args[0] 
            self.fail(message)
        else: 
            self.fail("Expecting exception, none found")
        warnings.warn("we'll want a mock here")

    @pytest.mark.parametrize("collection, where", [("Schools", [["Name", "==", "lkjdsafnlaqk346q9y"]])])
    def test_get_collection_no_result(self, collection, where):
        params = {collection: {"where": where}}
        result = self.api.get(params)
        
        assert result == {}

        warnings.warn("we'll want a mock here, and also this test will break when we add another school")

    def test_get_document(self):
        # params = {"collection": "Schools", "reference": self.SCHOOL_ID}
        params = {"Schools": {"reference": self.SCHOOL_ID}}
        school = self.api.get(params)

        assert len(school) == 1 #we should only get one back
        assert school["Name"] == "X School"
        warnings.warn("test not written")

    @pytest.mark.xfail # do this when you haven't finished writing the test
    def test_get_subcollection(self):
        pass

    @pytest.mark.xfail
    def test_get_reference_by_field(self):
        pass

    @pytest.mark.xfail
    def test_limit(self):
        pass

    @pytest.mark.xfail
    def test_order_by(self):
        pass

    @pytest.mark.xfail
    def test_combination(self):
        pass

    @pytest.mark.xfail
    def test_post():
        pass

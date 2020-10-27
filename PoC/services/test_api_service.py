import pytest
import warnings
import requests
import json
from test_base_class import TestBaseClass
from api_service import APIService

# Documentation and stuff
# Different marks: https://docs.pytest.org/en/stable/mark.html

# Built in marks: usefixtures, filterwarnings, skip, skipif, xfail, parametrize. Use with -m in command line to do things like skip tests

class TestAPIService(TestBaseClass):

    api = APIService()

    @pytest.fixture
    def valid_filter(self):
        filter = {
            'limit': 3,
            'orderBy': ['CharsCorrect', 'desc'],
            'startDate': ['<', 20200331],
            # 'endDate',
            # 'assigned'
            }
        table = {
            'Schools': self.SCHOOL_ID, 'UserProfiles': None, 'History': None
        }
        return [filter, table]

    @pytest.fixture
    def invalid_filter(self):
        filter = {
            # 'limit' = [-3, 0],
            # 'orderBy' = [['cheeseburger', '2'], [12, 1]],
            # 'startDate', ['<', 20200331]
            }

        return filter


    @pytest.mark.parametrize("collection, where", [("Schools", ["Name", "==", "X School"]), ("Schools", ["Name", "exists"])])
    def test_get_collection(self, collection, where):
        params = {"collection": collection, "where": where}
        schools = self.api.get(params)
        list_schools = list(schools.values())

        assert len(list_schools) == 1
        assert list_schools[0]["Name"] == "X School"

        warnings.warn("we'll want a mock here, and also this test will break when we add another school")

    def test_get_document(self):
        # history = 
        warnings.warn("test not written")

    # def test_get_subcollection(self):
    #     warnings.warn("test not written")

    # def test_get_reference_by_field(self):
    #     warnings.warn("test not written")

    # def test_limit(self):
    #     warnings.warn("test not written")

    # def test_order_by(self):
    #     warnings.warn("test not written")

    # def test_combination(self):
    #     warnings.warn("test not written")

        # @pytest.mark.xfail
        # def test_post():
        #     warn("test not written")

        # @pytest.mark.xfail
        # def test_authentication():
        #     def test_valid_login():
        #         warn("test not written")

        #     def test_invalid_login():
        #         warn("test not written")

        #     def test_valid_login_no_school():
        #         warn("test not written")

        #     def test_create_account():
        #         warn("test not written")

        #     def test_modify_account():
        #         warn("test not written")


        # # Test for any helper functions that need testing
        # @pytest.mark.xfail
        # def test_functions():
        #     warn("test not written")
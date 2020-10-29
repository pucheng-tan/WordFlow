import pytest

# Documentation and stuff
# pytest marks: https://docs.pytest.org/en/stable/mark.html
# pytest assertions: https://docs.pytest.org/en/stable/assert.html

# CREATING TESTS:

    # Test file names must start with "test_"
    # Test file names should generally be in the format test_file_being_tested.py
    # Template for """ comments for functions:
"""Test Case <test type> <issue>.<number>
A short summary of what the test does
Requirement: Functional Requirement 13.3: Pizzas must have pizza sauce
"""
    # test type = IT, UT, ET (integration, unit, end-to-end test)
    # issue = the issue in GitLab
    # number = give them numbers
    # requirement: If applicable, reference what requirement it covers

# MARKING TESTS:

    # parametrize: use to run tests multiple times with different parameters
    # xfail: use to mark a test as not completely written
    # api_call: use to mark test as one that makes call to external api
    # fixture: use to mark a function as a fixture that is used by other tests 
        # ex: if several functions use the same value in the tests, mark it as a fixture and use the name as a variable
        # NOTE: Am using test classes because the API cannot be instantiated more than once, and this seems to have broken fixtures.

# RUNNING TESTS: 

    # Test single file: pytest <file_name>
    # OR:
    # Test all files in directory (and subdirectories): pytest <file_path>

    # Useful switches:
    # Verbose = -v: "pytest test_path -v"
    # Marks = -v <args>: "pytest test_path -m api_call" run only tests marked with api_call
        # OR: "pytest test_path -m "not api_call"" to exclude tests marked with api_call. "" around not and the mark name
        # https://docs.pytest.org/en/stable/example/markers.html for further examples
        # Create a custom mark by adding it to the pytest.ini file located in the top level of the repository
    # Keyword(??) = -k <args>: "pytest test_path -k get_collection" runs test with "get collection" in the name of the test

# LOGGING TEST RESULTS:

    # pytest's file logging does not record the passes, so use external plugin:
    # before merge request, run to generate test log as file: pytest --json-report
        # It has a "success" field that checks that the test was run at the root, there are no warnings, and everything passed.
        # It wasn't fully tested, so if you run into bugs with that, it can be changed in conftest.py

class TestBaseClass():
    """Common testing methods and data are stored in this file"""    

    TEST_SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"

    def fail(self, message):
        """Automatically causes a test to fail, and prints out a given message in the summary
        Args:
            message (str): The message to be outputted in the test result.
                NOTE: Do not make this message the number 1
        Returns:
            None
        """
        assert str(message) == 1
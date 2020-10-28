import pytest
import warnings
import requests
import json

# Documentation and stuff
# Different marks: https://docs.pytest.org/en/stable/mark.html

# Built in marks: usefixtures, filterwarnings, skip, skipif, xfail, parametrize. Use with -m in command line to do things like skip tests

class TestBaseClass():
    """Common testing methods and data are stored in this file"""
    SCHOOL_ID = 'o2lTSAI6X4yGdIZ0huB9'

    
    def fail(self, message):
        """Automatically causes a test to fail, and prints out a given message
        Args:
            message (str): The message to be outputted in the test result.
                NOTE: Do not make this message the number 1
        Returns:
            None
        """
        assert message == 1
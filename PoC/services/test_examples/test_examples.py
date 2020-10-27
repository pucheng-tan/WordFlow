import pytest
import requests
import json

def func(x):
    return x + 5

@pytest.mark.two
def test_method():
    assert func(3) == 8
    assert func(3) == 5

@pytest.mark.one
def test_method2():
    a = 15
    b = 20
    assert a + 5 == b

@pytest.fixture
def main_url():
    return "https://reqres.in"

def test_valid_login(main_url):
    url = main_url + "/api/login/"
    data = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"

# py.test -m two //to run only tests with "mark"
# pytest -k method1 -v //increase verbosity
    # pytest .\PoC\services\test_examples.py
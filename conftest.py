import pytest
import os

@pytest.fixture(autouse=True)
def clear_yaml(path=""):
    if path == "":
        path = os.getcwd() + '/extract.yml'
    with open(path, 'w') as yf:
        pass

@pytest.fixture()
def header():
    head = {}
    return head

@pytest.fixture()
def body():
    body = {}
    return body


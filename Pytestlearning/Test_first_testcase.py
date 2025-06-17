import pytest

# test fixture at moudle level which is executed only once

def setup_module(module):
    print("creating db connection")

def teardown_module(module):
    print("closing db connection")

# test fixture at function level
def setup_function(function):
    print("launch browser")

def teardown_function(function):
        print("quit browser")

def test_doLogin():

    print("Executing login testcase")

def test_userReg():
    print("Executing user reg  testcase")


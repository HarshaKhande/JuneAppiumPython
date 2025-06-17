import pytest

# test fixture at moudle level which is executed only once

@pytest.fixture(scope = 'module')
def setup():
    print("creating db connection")

    yield
    print("closing the db connection")


@pytest.fixture(scope = 'function')
def before():
    print("launch browser")

    yield
    print("quit browser")



def test_doLogin(setup,before):

    print("Executing login testcase")

def test_userReg(setup,before):
    print("Executing user reg  testcase")



import pytest

# test fixture at moudle level which is executed only once


@pytest.mark.functional
def test_doLogin():

    print("Executing login testcase")

@pytest.mark.regression
def test_userReg():
    print("Executing user reg  testcase")

@pytest.mark.skip
def test_payment():
    print("Executing payment  testcase")




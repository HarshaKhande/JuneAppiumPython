import pytest

# test fixture at moudle level which is executed only once



def get_data():

    return[


        ("trainer@way2automation.com", "gfghhh"),
        ("java@way2automation.com", "fghghh"),
        ("info@way2automation.com", "gfggh")
    ]


@pytest.mark.parametrize("username, password", get_data())
def test_doLogin(username, password):
    print(username, "------", password)

    print("Executing login testcase")


def test_userReg():
    print("Executing user reg  testcase")


def test_payment():
    print("Executing payment  testcase")




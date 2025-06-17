def test_validate_tiles():

    # failure in the test will break the tests

    expected_title = "Google.com"
    actual_title = "Gmail.com"
    title = "This is gmail web site"


    #if actual_title == expected_title:
     #   print("Testcase is passed")
    #else:
     #   print("Testcase is failed")

    assert expected_title == actual_title, "Titles are not matching"

    assert "gmail" in title , "Gmail does  exists"

    assert False, "Forcefully failing the test"












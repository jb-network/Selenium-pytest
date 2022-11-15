import pytest
from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error",
                             [("wrong_username", "Password123", "Your username is invalid!"),
                              ("student", "bad_password", "Your password is invalid!")])
    def test_negative_login(self, browser, username, password, expected_error):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.gt_error_message() == expected_error, "Error message is not the expected message"



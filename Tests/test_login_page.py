import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(browser)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Logged In Successfully", "Header is not set to the expected setting"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"


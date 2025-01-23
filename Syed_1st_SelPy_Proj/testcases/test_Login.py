import pytest
from POM.LoginPage import LoginPage

@pytest.mark.usefixtures("setup")
class TestLoginPage:
    """
    A test class for verifying the login functionality of the application.
    The 'setup' fixture initializes the WebDriver for the test.
    """

    def test_verify_login_with_valid_creds(self):
        """
        Test case to verify that login works with valid credentials.
        """

        # Create an instance of the LoginPage class and pass the WebDriver
        LOGIN_PAGE = LoginPage(self.driver)

        # Enter valid email (or username) into the email field
        LOGIN_PAGE.enter_email("standard_user")

        # Enter valid password into the password field
        LOGIN_PAGE.enter_password("secret_sauce")

        # Click the login button to submit the form
        LOGIN_PAGE.click_login_button()

        # Validate that the user is successfully redirected to the inventory page
        assert "inventory.html" in self.driver.current_url, "Login failed!"

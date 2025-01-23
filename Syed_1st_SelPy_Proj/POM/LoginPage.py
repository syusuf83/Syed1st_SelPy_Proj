from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Define locators
        self.EMAIL_FIELD = (By.ID, "user-name")  # Locator for the username/email field
        self.PASS_FIELD = (By.ID, "password")   # Locator for the password field
        self.LOGIN_BUTTON = (By.ID, "login-button")  # Locator for the login button

    def enter_email(self, email):
        """Enter email into the email field."""
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        """Enter password into the password field."""
        password_field = self.driver.find_element(*self.PASS_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        """Click the login button."""
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

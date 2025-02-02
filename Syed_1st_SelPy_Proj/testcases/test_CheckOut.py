import pytest  # Import the pytest framework for testing
import time  # Import time module for sleep to pause between steps
from selenium import webdriver  # Import WebDriver from selenium to control browser
from selenium.webdriver.chrome.service import Service  # Import Service for handling ChromeDriver service
from selenium.webdriver.common.by import By  # Import By class to locate elements
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for waiting for elements
from selenium.webdriver.support import expected_conditions as EC  # Import expected_conditions for various wait conditions
from webdriver_manager.chrome import ChromeDriverManager  # Import ChromeDriverManager for automatic WebDriver management
import sys  # Import sys for system-specific parameters and functions (not used in the current code)
import os  # Import os for interacting with the operating system (not used in the current code)

# Importing Page Object Models (POM) for LoginPage and CheckOut to interact with the respective pages
from Syed_1st_SelPy_Proj.POM.CheckOut import CheckOut
from Syed_1st_SelPy_Proj.POM.LoginPage import LoginPage

# Fixture setup to initialize WebDriver for the tests
@pytest.fixture(scope="class")
def setup(request):
    # Initialize the Chrome WebDriver using the ChromeDriverManager for automatic installation of the appropriate version
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # Maximize the browser window for better visibility
    request.cls.driver = driver  # Assign the WebDriver to the test class for access in tests
    yield  # Pause the fixture after yielding, allowing the tests to run
    driver.quit()  # Quit WebDriver after tests are complete, cleaning up resources

# Test class for Checkout page functionality, using the setup fixture
@pytest.mark.usefixtures("setup")
class TestCheckoutPage:
    # Test to check if the login page URL opens correctly
    @pytest.mark.order(1)
    def test_open_page_url(self):
        """Test if the login page URL opens correctly"""
        self.driver.get("https://www.saucedemo.com/")  # Open the login page
        # Assert if "saucedemo" is part of the current URL
        assert "saucedemo" in self.driver.current_url, "Failed to open the correct URL"
        time.sleep(2)  # Pause for 2 seconds to allow the page to load

    # Test for user login functionality
    @pytest.mark.order(2)
    def test_login_functionality(self):
        """Test user login functionality"""
        login_page = LoginPage(self.driver)  # Create LoginPage object for interacting with the login page
        login_page.open_page()  # Open the login page
        login_page.enter_email("standard_user")  # Use the correct method name
        login_page.enter_password("secret_sauce")  # Enter the password
        login_page.click_login_button()  # Click the login button to submit the form

        # Wait for the inventory page to load after login
        WebDriverWait(self.driver, 10).until(EC.url_contains("inventory.html"))
        # Assert if the current URL contains "inventory.html" indicating successful login
        assert "inventory.html" in self.driver.current_url, "Login failed"
        time.sleep(2)  # Pause for 2 seconds after login

    # Test to add items to the shopping cart
    @pytest.mark.order(3)
    def test_add_items_to_cart(self):
        """Test to add two items to the cart."""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()  # Add first item to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()  # Add second item to cart

        # Find the cart icon and check if it displays the correct number of items (2 in this case)
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        assert cart_icon.text.strip() == "2", "Failed to add two items to the cart."  # Assert that 2 items are in the cart
        time.sleep(2)  # Pause for 2 seconds after adding items

    # Test to navigate to the checkout page
    @pytest.mark.order(4)
    def test_navigate_to_checkout(self):
        """Navigate to checkout page"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()  # Click on the shopping cart
        checkout_button = WebDriverWait(self.driver, 10).until(  # Wait for the checkout button to be clickable
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()  # Click the checkout button to go to checkout page
        time.sleep(2)  # Pause for 2 seconds after navigation

    #  Test to fill in checkout information
    @pytest.mark.order(5)
    def test_fill_checkout_information(self):
        """Test to fill in checkout information."""
        checkout_page = CheckOut(self.driver)  # Create CheckOut object to interact with the checkout form
        checkout_page.enter_checkout_first_name("John")  # Enter the first name
        checkout_page.enter_checkout_last_name("Doe")  # Enter the last name
        checkout_page.enter_checkout_zip_code("12345")  # Enter the zip code
        checkout_page.click_continue_checkout_button()  # Click the continue button to move to the next step
        time.sleep(2)  # Pause for 2 seconds after filling in the information
    #
    @pytest.mark.order(6)
    def test_complete_order(self):
        """Test to complete the purchase."""
        # Wait for the finish button to be clickable before clicking
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Finish']"))
        )

        # Scroll the finish button into view if it's not visible
        self.driver.execute_script("arguments[0].scrollIntoView();", finish_button)

        # Click the finish button to complete the order
        finish_button.click()

        # Wait for the success message to appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )

        success_message = self.driver.find_element(By.CLASS_NAME, "complete-header").text
        expected_message = "Thank you for your order!"

        # Check if the success message is displayed
        assert expected_message in success_message, "Order placement failed or success message not displayed."

        time.sleep(2)  # Pause for 2 seconds


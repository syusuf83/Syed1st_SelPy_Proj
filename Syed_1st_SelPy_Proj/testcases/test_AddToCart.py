import pytest
from POM.AddToCart import AddToCart  # Import the AddToCart class from the POM.AddToCart module to interact with the add-to-cart functionality.
from POM.LoginPage import LoginPage  # Import the LoginPage class from the POM.LoginPage module to interact with the login page.
from selenium.webdriver.common.by import By  # Import the By class from Selenium, used to locate elements on the page.
import time  # Import the time module to introduce pauses.

@pytest.mark.usefixtures("setup")  # This decorator ensures the 'setup' fixture is used for the test class. The setup fixture initializes resources like the WebDriver.
class TestAddToCart:
    """
    A test class for adding items to the cart on the SauceDemo inventory page.
    """

    def test_add_items_to_cart(self):
        """
        Test case to verify that items can be added to the cart successfully.
        """
        # Step 1: Login to the application
        LOGIN_PAGE = LoginPage(self.driver)  # Create an instance of the LoginPage class using the WebDriver.
        LOGIN_PAGE.enter_email("standard_user")  # Use the 'enter_email' method to input the username "standard_user".
        LOGIN_PAGE.enter_password("secret_sauce")  # Use the 'enter_password' method to input the password "secret_sauce".
        LOGIN_PAGE.click_login_button()  # Click the login button using the 'click_login_button' method.

        time.sleep(2)  # Pause for 2 seconds to simulate a wait between page actions.

        # Step 2: Add items to the cart
        ADD_TO_CART_PAGE = AddToCart(self.driver)  # Create an instance of the AddToCart class using the WebDriver.
        ADD_TO_CART_PAGE.add_backpack_to_cart()  # Call 'add_backpack_to_cart' to add the "Sauce Labs Backpack" to the cart.
        ADD_TO_CART_PAGE.add_tshirt_to_cart()   # Call 'add_tshirt_to_cart' to add the "Sauce Labs Bolt T-Shirt" to the cart.

        time.sleep(2)  # Pause for 2 seconds after adding items to the cart.

        # Step 3: Navigate to the cart page
        ADD_TO_CART_PAGE.open_cart()  # Call 'open_cart' to navigate to the cart page.

        time.sleep(2)  # Pause for 2 seconds before verifying the cart contents.

        # Step 4: Validate that items are in the cart
        assert "cart.html" in self.driver.current_url, "Failed to navigate to the cart page!"  # Assert that the URL contains "cart.html", indicating we're on the cart page.
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")  # Find all elements with the class name "inventory_item_name", which represent items in the cart.
        item_names = [item.text for item in cart_items]  # Extract the text of the items in the cart and store it in the 'item_names' list.

        # Ensure the correct items are in the cart
        assert "Sauce Labs Backpack" in item_names, "Backpack not found in the cart!"  # Assert that the "Sauce Labs Backpack" is found in the list of items in the cart.
        assert "Sauce Labs Bolt T-Shirt" in item_names, "T-Shirt not found in the cart!"  # Assert that the "Sauce Labs Bolt T-Shirt" is found in the list of items in the cart.

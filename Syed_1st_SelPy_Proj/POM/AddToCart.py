from selenium.webdriver.common.by import By

class AddToCart:
    """
    A page object class for the inventory page that allows adding items to the cart.
    """

    def __init__(self, driver):
        self.driver = driver
        # Locators for the 'Add to Cart' buttons
        self.ADD_TO_CART_BACKPACK = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        self.ADD_TO_CART_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.CART_ICON = (By.CLASS_NAME, "shopping_cart_link")  # Locator for the cart icon

    def add_backpack_to_cart(self):
        """Click the 'Add to Cart' button for the backpack."""
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()

    def add_tshirt_to_cart(self):
        """Click the 'Add to Cart' button for the t-shirt."""
        self.driver.find_element(*self.ADD_TO_CART_TSHIRT).click()

    def open_cart(self):
        """Click the cart icon to view added items."""
        self.driver.find_element(*self.CART_ICON).click()

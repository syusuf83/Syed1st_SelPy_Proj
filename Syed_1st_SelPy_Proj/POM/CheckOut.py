from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOut:
    def __init__(self, driver):
        self.driver = driver
        self.FIRST_NAME_FIELD = (By.ID, "first-name")  # Confirm this locator is correct

    def enter_checkout_first_name(self, first_name):
        """Enter the first name in the checkout form."""
        try:
            first_name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.FIRST_NAME_FIELD)
            )
            first_name_field.clear()
            first_name_field.send_keys(first_name)
        except Exception as e:
            print(f"Error: {e}")

    def enter_checkout_last_name(self, last_name):
        """Enter last name in the checkout form."""
        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='last-name'])[1]"))
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_checkout_zip_code(self, zip_code):
        """Enter zip/postal code in the checkout form."""
        zip_code_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='postal-code']"))
        )
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)

    def click_continue_checkout_button(self):
        """Click the Continue button on the checkout form."""
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

    def click_finish_button(self):
        """Click the Finish button on the checkout form."""
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Finish']"))  # Fixed tuple syntax
        )

        # Scroll into view if necessary
        self.driver.execute_script("arguments[0].scrollIntoView();", finish_button)

        # Click the button
        finish_button.click()

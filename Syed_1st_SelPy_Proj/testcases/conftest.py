import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    """
    A pytest fixture to initialize and set up the Selenium WebDriver for testing.
    The fixture is scoped at the class level, so it is set up once per test class.
    """
    # Initialize the WebDriver with ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Maximize the browser window
    driver.maximize_window()

    # Set an implicit wait of 6 seconds (wait time for finding elements)
    driver.implicitly_wait(6)

    # Navigate to the specified URL
    driver.get("https://www.saucedemo.com/")

    # Attach the WebDriver instance to the test class (allows access via 'self.driver')
    request.cls.driver = driver

    # Yield to allow test execution to proceed
    yield

    # Quit the WebDriver instance after test execution
    driver.quit()

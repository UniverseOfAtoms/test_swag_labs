import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    chromeService = Service(executable_path=ChromeDriverManager().install())
    selenium_driver = webdriver.Chrome(service=chromeService)
    yield selenium_driver
    time.sleep(5)
    selenium_driver.quit()
import pytest as pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver=driver


# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)


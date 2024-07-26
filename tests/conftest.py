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
    # Below lines (15 and 16) keep the chrome drive open
    # option = webdriver.ChromeOptions()
    # option.add_experimental_option('detach', True)
    # Selenium has the capability to interact with browser without giving the path,
    # It will take care by webdriver maager
    driver = webdriver.Chrome() #options=option
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver



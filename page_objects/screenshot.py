from selenium.webdriver.common.by import By

class ScreenShot:

    def __init__(self, driver):
        self.driver = driver


    def screenshot(self):
        return self.driver.get_screenshot_as_file('')



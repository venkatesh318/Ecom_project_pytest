from selenium.webdriver.common.by import By


class MobileResultsPage:

    def __init__(self, driver):
        self.driver = driver

    verification_text = (By.XPATH, '//div[text()="Newest First"]')
    iphone_path = (By.XPATH, "//div[normalize-space()='Apple iPhone 15 (Black, 128 GB)']")

    def mobile_selection(self):
        return self.driver.find_element(*MobileResultsPage.iphone_path)

    def verification_text_one(self):
        return self.driver.find_element(*MobileResultsPage.verification_text)

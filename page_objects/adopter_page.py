from selenium.webdriver.common.by import By

class AdopterMainPage:

    def __init__(self, driver):
        self.driver=driver

    adopter_name = (By.XPATH,"//span[@class='VU-ZEz']")
    add_to_cart = (By.XPATH, "//button[normalize-space()='Add to cart']")
    pincode_path = (By.XPATH, "//input[@id='pincodeInputId']")
    check_button_path = (By.XPATH, '//span[text()="Check"]')

    def to_get_adopter_name(self):
        return self.driver.find_element(*AdopterMainPage.adopter_name)

    def adding_adopter_to_cart(self):
        return self.driver.find_element(*AdopterMainPage.add_to_cart)

    def pincode_field(self):
        return self.driver.find_element(*AdopterMainPage.pincode_path)

    def check_button(self):
        return self.driver.find_element(*AdopterMainPage.check_button_path)

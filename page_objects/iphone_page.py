from selenium.webdriver.common.by import By

class IphonePage:

    def __init__(self, driver):
        self.driver=driver

    iphone_verif_text = (By.XPATH,"//span[text()='Apple iPhone 15 (Black, 128 GB)']")
    go_to_cart_button = (By.XPATH, "//button[normalize-space()='Add to cart']")

    def verifi_of_mobile_name(self):
        return self.driver.find_element(*IphonePage.iphone_verif_text)

    def adding_mobile_to_cart(self):
        return self.driver.find_element(*IphonePage.go_to_cart_button)
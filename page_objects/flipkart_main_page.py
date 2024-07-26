from selenium.webdriver.common.by import By

class FlipkartMainPage:

    def __init__(self, driver):
        self.driver = driver

    search_bar = (By.XPATH, '//form[@action="/search"]')
    search_bar_text_field = (By.NAME,'q')
    iphone_path = (By.XPATH, "//div[normalize-space()='Apple iPhone 15 (Black, 128 GB)']")
    login_button_path = (By.XPATH, '//a[@title="Login"]')

    def page_verification(self):
        return self.driver.current_url

    def searchBar(self):
        return self.driver.find_element(*FlipkartMainPage.search_bar)

    def searchBarText(self):
        return self.driver.find_element(*FlipkartMainPage.search_bar_text_field)

    def mobile_name(self):
        return self.driver.find_element(*FlipkartMainPage.mobile_model)

    def pressEnter(self):
        return self.driver.find_element()

    def login_button(self):
        return self.driver.find_element(*FlipkartMainPage.login_button_path)


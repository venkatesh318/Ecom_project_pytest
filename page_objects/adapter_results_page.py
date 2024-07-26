from selenium.webdriver.common.by import By

class AdopterResultsPage:

    def __init__(self, driver):
        self.driver = driver
    adopter_results_text = (By.XPATH,"//span[@class='BUOuZu']")
    adpoter_link_in_results_page = (By.XPATH,"//a[contains(text(),'Apple 20W ,USB-C Power Charging Adapter for iPhone')]")

    def adopter_text_in_results_page(self):
        return self.driver.find_element(*AdopterResultsPage.adopter_results_text)

    def selecting_the_adpoter(self):
        return self.driver.find_element(*AdopterResultsPage.adpoter_link_in_results_page)

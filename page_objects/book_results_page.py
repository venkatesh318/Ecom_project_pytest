from selenium.webdriver.common.by import By

class BookResultsPage:

    def __init__(self, driver):
        self.driver=driver

    book_results_text = (By.XPATH,"//span[@class='BUOuZu']")
    book_link = (By.XPATH, "//a[normalize-space()='Rich Dad Poor Dad: 25th Anniversary Edit Paperback']")

    def verifi_of_book_results(self):
        return self.driver.find_element(*BookResultsPage.book_results_text)

    def selecting_the_book(self):
        return self.driver.find_element(*BookResultsPage.book_link)
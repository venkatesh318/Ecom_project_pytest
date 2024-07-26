from selenium.webdriver.common.by import By

class BookMainPage:

    def __init__(self, driver):
        self.driver=driver

    book_name = (By.XPATH,"//span[@class='VU-ZEz']")
    add_to_cart = (By.XPATH, "//button[normalize-space()='Add to cart']")
    book_link = (By.XPATH, "//a[normalize-space()='Rich Dad Poor Dad: 25th Anniversary Edit Paperback']")

    def to_get_book_name(self):
        return self.driver.find_element(*BookMainPage.book_name)

    def adding_book_to_cart(self):
        return self.driver.find_element(*BookMainPage.add_to_cart)
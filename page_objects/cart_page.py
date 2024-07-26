from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    book_vtext = (By.XPATH, "// a[normalize - space() = 'Rich Dad Poor Dad: 25th Anniversary Edit Paperback']")
    adopter_vtext = (By.XPATH, "//a[contains(text(),'Apple 20W ,USB-C Power Charging Adapter for iPhone')]")
    iphone_vtext = (By.XPATH, "//a[normalize-space()='Apple iPhone 15 (Black, 128 GB)']")
    prices = (By.XPATH, '//span[@class="LAlF6k re6bBo"]')

    def mobile_cart(self):
        return self.driver.find_element(*CartPage.iphone_vtext)

    def book_cart(self):
        return self.driver.find_element(*CartPage.book_vtext)

    def adopter_cart(self):
        return self.driver.find_element(*CartPage.adopter_vtext)

    def price_of_items(self):
        char = '₹'
        prices_list = []
        pric_list = self.driver.find_elements(*CartPage.prices)
        for x in pric_list:
            prices_list.append(x.text)
        new_list = [ele.replace(char, '') for ele in prices_list]
        new_list1 = [ele.replace(',', '') for ele in new_list]
        new_list2 = [int(i) for i in new_list1]
        total_products_price = sum(new_list2)
        return total_products_price

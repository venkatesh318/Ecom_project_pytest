import datetime
import time
import pytest
from selenium.webdriver import Keys

from page_objects.flipkart_main_page import FlipkartMainPage
from page_objects.login_page import LoginPage
from page_objects.mobile_results import MobileResultsPage
from page_objects.iphone_page import IphonePage
from page_objects.book_results_page import BookResultsPage
from page_objects.cart_page import CartPage
from page_objects.book_page import BookMainPage
from page_objects.adapter_results_page import AdopterResultsPage
from page_objects.adopter_page import AdopterMainPage


@pytest.mark.usefixtures("setup")
class Testone:

    base_path = 'screenshots/'
    DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    # variables
    page_url = "https://www.flipkart.com/"
    mobile_model = 'IPhone 15 Black 128 gb'
    expected_error_message = "Please enter valid Email ID/Mobile number"
    verifi_text_in_mobile_search_results_page = "Newest First"
    expected_mobile_name = 'Apple iPhone 15 (Black, 128 GB)'
    book_name_for_searching = "Rich Dad Poor Dad Book"
    expected_book_results = 'results for "Rich Dad Poor Dad Book"'
    expected_book_name = 'Rich Dad Poor Dad: 25th Anniversary Edit Paperback  (Paperback, Robert Kiyosaki)'
    adopter_name_for_searching = "Apple Adopter 20w"
    expceted_adapter_results = 'results for "apple adapter 20w"'
    expceted_adapter_name = 'Apple 20W ,USB-C Power Charging Adapter for iPhone, iPad & AirPods  (White)'
    pincode = 500081
    expected_total_price = 73903

    # path for the screenshots
    main_page = base_path + 'main_page' + str(DateString) + '.png'
    login_page = base_path + 'login_page' + str(DateString) + '.png'
    login_error_page = base_path + 'login_error_page' + str(DateString) + '.png'
    mobile_results_page = base_path + 'mobile_results_page' + str(DateString) + '.png'
    mobile_window = base_path + 'mobile_window' + str(DateString) + '.png'
    cart_after_adding_mobile = base_path + 'cart_after_adding_mobile' + str(DateString) + '.png'
    book_window = base_path + 'book_window' + str(DateString) + '.png'
    book_results_page = base_path + 'book_results_page' + str(DateString) + '.png'
    cart_after_adding_book = base_path + 'cart_after_adding_book' + str(DateString) + '.png'
    adapter_result_page = base_path + 'adapter_result_page' + str(DateString) + '.png'
    adapter_window = base_path + 'adapter_window' + str(DateString) + '.png'
    cart_after_adding_adopter = base_path + 'cart_after_adding_adopter' + str(DateString) + '.png'

    def test_flipkart_page(self):
        # Flipkart main page validation
        page_validation = FlipkartMainPage(self.driver)
        page_name = page_validation.page_verification()
        assert page_name == self.page_url
        print(page_name)
        time.sleep(3)
        self.driver.get_screenshot_as_file(self.main_page)

    # Login Page
    def test_login_page(self):
        page_validation = FlipkartMainPage(self.driver)
        page_validation.login_button().click()
        ln_page = LoginPage(self.driver)
        ln_page.email_or_mobile_number().click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(self.login_page)
        ln_page.email_or_mobile_number().send_keys(self.pincode)
        ln_page.request_otp().click()
        actual_error_message = ln_page.error_validation().text
        time.sleep(2)
        self.driver.get_screenshot_as_file(self.login_page)
        assert actual_error_message == self.expected_error_message

    def test_mobile_page(self):
        global searching
        # product search (searching for iphone 15)
        searching = FlipkartMainPage(self.driver)
        searching.searchBar().click()
        searching.searchBarText().send_keys(self.mobile_model)
        searching.searchBarText().send_keys(Keys.RETURN)

        # iphone search results page
        mr_page = MobileResultsPage(self.driver)
        verification_name = mr_page.verification_text_one().text
        assert verification_name == self.verifi_text_in_mobile_search_results_page
        print(verification_name)
        time.sleep(3)
        self.driver.get_screenshot_as_file(self.mobile_results_page)

        # Mobile name confirmation
        mobile_name_confirmation = mr_page.mobile_selection().text
        assert mobile_name_confirmation == self.expected_mobile_name
        print(mobile_name_confirmation)

        # selecting the mobile
        mr_page.mobile_selection().click()

        # Navigating to newly opened window and verifing the mobile name
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        new_window = IphonePage(self.driver)
        time.sleep(3)
        actual_mobile_name = new_window.verifi_of_mobile_name().text
        assert actual_mobile_name == self.expected_mobile_name
        print(actual_mobile_name)
        time.sleep(3)
        self.driver.get_screenshot_as_file(self.mobile_window)

        # Adding mobile to cart
        new_window.adding_mobile_to_cart().click()
        time.sleep(3)
        self.driver.get_screenshot_as_file(self.cart_after_adding_mobile)

        # verification of cart page
        c_page = CartPage(self.driver)
        c_actual_mobile_name = c_page.mobile_cart().text
        assert c_actual_mobile_name == self.expected_mobile_name
        time.sleep(3)

    def test_book_page(self):
        # Searching book from the cart page
        searching.searchBar().click()
        searching.searchBarText().send_keys(self.book_name_for_searching)
        searching.searchBarText().send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.get_screenshot_as_file(self.book_results_page)

        # Book search results page
        book_page = BookResultsPage(self.driver)
        actual_result = book_page.verifi_of_book_results().text
        assert self.expected_book_results in actual_result

        # Selecting the book
        book_page.selecting_the_book().click()

        # Navigating to newly opened window and verifying the book name
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[2])

        b_page = BookMainPage(self.driver)
        actual_book_name = b_page.to_get_book_name().text
        assert actual_book_name == self.expected_book_name
        print(actual_book_name)
        time.sleep(3)

        self.driver.get_screenshot_as_file(self.book_window)

        # Adding book to cart
        b_page.adding_book_to_cart().click()
        time.sleep(3)

        self.driver.get_screenshot_as_file(self.cart_after_adding_book)

    def test_adapter_page(self):
        # Searching adopter from the cart page
        searching.searchBar().click()
        searching.searchBarText().send_keys(self.adopter_name_for_searching)
        time.sleep(3)
        searching.searchBarText().send_keys(Keys.RETURN)

        # Confirmation of adopter page
        time.sleep(3)
        self.driver.get_screenshot_as_file(self.adapter_result_page)
        ar_page = AdopterResultsPage(self.driver)
        # Selecting the adopter
        ar_page.selecting_the_adpoter().click()

        # Navigating to newly opened window and verifing the adopter
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[3])

        a_page = AdopterMainPage(self.driver)
        time.sleep(3)
        actual_adopter_name = a_page.to_get_adopter_name().text
        assert actual_adopter_name == self.expceted_adapter_name
        print(actual_adopter_name)

        # verification of pin code for adopter availability
        a_page.pincode_field().click()
        a_page.pincode_field().send_keys(self.pincode)
        a_page.check_button().click()
        time.sleep(3)
        self.driver.get_screenshot_as_file(self.adapter_window)
        time.sleep(2)

        # Adding Adopter to cart
        a_page.adding_adopter_to_cart().click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(self.cart_after_adding_adopter)

    # Do price validaton in the cart
    def test_cart_page_price_validation(self):
        c_page = CartPage(self.driver)
        actual_total_price = c_page.price_of_items()
        assert actual_total_price == self.expected_total_price
        print(actual_total_price)

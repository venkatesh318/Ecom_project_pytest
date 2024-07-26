from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_or_mobile = (By.XPATH, "//input[@class='r4vIwl BV+Dqf']")
    login_button = (By.XPATH,"//button[text()='Request OTP']")
    error_message = (By.XPATH,'//span[text()="Please enter valid Email ID/Mobile number"]')

    def email_or_mobile_number(self):
        return self.driver.find_element(*LoginPage.email_or_mobile)

    def request_otp(self):
        return self.driver.find_element(*LoginPage.login_button)

    def error_validation(self):
        return self.driver.find_element(*LoginPage.error_message)

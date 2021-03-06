from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _contact_link = (By.ID, "contact-link")
    _login_link = (By.XPATH, "//a[contains(@title, 'Log in to')]")
    _logout_button = (By.LINK_TEXT, "Sign out")
    _email_field = (By.ID, "email")
    _password_field = (By.ID, "passwd")
    _sign_in_button = (By.ID, "SubmitLogin")
    _account_link = (By.CSS_SELECTOR, "a[class='account'] > span ")
    _authentication_failure = (By.XPATH, "//li[contains(text(),'Authentication failed.')]")
    _number_of_items_in_cart = (By.CSS_SELECTOR, "span[class='ajax_cart_quantity']:nth-child(2)")

    def clear_field(self):
        self.get_element(self._email_field).clear()
        self.get_element(self._password_field).clear()

    def login(self, username, password):
        self.driver.implicitly_wait(5)
        self.clear_field()
        self.send_keys(username, self._email_field)
        self.send_keys(password, self._password_field)
        self.click_element(self._sign_in_button)

    def logout(self):
        self.click_element(self._logout_button)

    def verify_login_successful(self):
        return self.is_element_present(self._account_link)

    def verify_login_failed(self):
        return self.is_element_present(self._authentication_failure)

    def verify_number_of_items_in_cart(self):
        number_of_items_in_cart = self.wait_for_element(self._number_of_items_in_cart)
        return number_of_items_in_cart.text == "1"

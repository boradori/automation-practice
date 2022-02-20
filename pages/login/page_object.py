import logging

from . import locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @property
    def authentication_failure_message(self):
        return self._find_visible_element(locators.AUTHENTICATION_FAILURE).text

    @property
    def email_field(self):
        return self._find_visible_element(locators.EMAIL_FIELD)

    @property
    def password_field(self):
        return self._find_visible_element(locators.PASSWORD_FIELD)

    @property
    def sign_in_button(self):
        return self._find_clickable_element(locators.SIGN_IN_BUTTON)

    def get_number_of_items_in_cart(self):
        logging.info('Getting number of items in cart.')
        number = int(self._find_visible_element(locators.NUMBER_OF_ITEMS_IN_CART).text)
        return number

    def login(self, username, password):
        logging.info('Signing in.')
        self.email_field.send_keys(username)
        self.password_field.send_keys(password)
        self.sign_in_button.click()

    def logout(self):
        self._click(locators.LOGOUT_BUTTON)

    def navigate(self):
        logging.info('Navigating to "Login" page.')
        self._visit('http://automationpractice.com/index.php?controller=authentication&back=my-account')
        self.wait_for_email_field_to_be_clickable()

    def wait_for_email_field_to_be_clickable(self):
        logging.info('Waiting for email field to be clickable.')
        self._find_clickable_element(locators.EMAIL_FIELD, timeout=20)

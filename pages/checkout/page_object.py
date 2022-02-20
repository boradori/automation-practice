import pytest

from . import locators
from pages.base_page import BasePage
import logging


@pytest.mark.all
@pytest.mark.cart
class CheckoutPage(BasePage):
    @property
    def complete_message(self):
        return self._find_visible_element(locators.COMPLETE_MESSAGE, timeout=20).text

    @property
    def confirmation_price(self):
        return self._find_visible_element(locators.CONFIRMATION_PRICE, timeout=20).text

    @property
    def current_step(self):
        return self._find_visible_element(locators.CURRENT_STEP, timeout=20)

    @property
    def email_field(self):
        return self._find_visible_element(locators.EMAIL_FIELD)

    @property
    def error_message(self):
        return self._find_visible_element(locators.ERROR_MESSAGE).text

    @property
    def error_message_close_button(self):
        return self._find_clickable_element(locators.ERROR_MESSAGE_CLOSE_BUTTON)

    @property
    def heading(self):
        return self._find_visible_element(locators.HEADING, timeout=20).text

    @property
    def password_field(self):
        return self._find_visible_element(locators.PASSWORD_FIELD)

    @property
    def products(self):
        return self._find_present_elements(locators.PRODUCTS)

    @property
    def sign_in_button(self):
        return self._find_visible_element(locators.SIGN_IN_BUTTON)

    def click_confirm_button(self):
        logging.info('Clicking "Confirm" button.')
        self._click(locators.CONFIRM_BUTTON)

    def click_error_message_close_button(self):
        logging.info('Clicking "Error message close" button.')
        self._click(locators.ERROR_MESSAGE_CLOSE_BUTTON)
        self._wait_for_element_to_disappear(locator=locators.ERROR_MESSAGE_CLOSE_BUTTON)

    def click_pay_by_bank_wire(self):
        logging.info('Clicking "Pay by bank wire" button.')
        self._scroll_to_element(locator=locators.PAY_BY_BANK_WIRE_BUTTON)
        self._click(locators.PAY_BY_BANK_WIRE_BUTTON)

    def click_proceed_to_checkout_button(self):
        logging.info('Clicking "Proceed to checkout" button.')
        self._scroll_to_element(locator=locators.PROCEED_TO_CHECKOUT_BUTTON)
        self._click(locators.PROCEED_TO_CHECKOUT_BUTTON)

    def get_items_in_payment_page(self, more_details=True):
        logging.info('Getting item tables in the "Payment" page.')
        items_in_payment_page = []

        for product in self.products:
            if more_details:
                item_dict = {
                    'name': product.find_element_by_css_selector(locators.ITEM_NAME['value']).text,
                    'sku': product.find_element_by_xpath(locators.ITEM_SKU['value']).text[6:],
                    'color':
                        (
                            product.find_element_by_xpath(locators.ITEM_COLOR['value']).text.split(' : ')[1].split(
                                ', ')[0]
                        ),
                    'price': product.find_element_by_css_selector(locators.ITEM_PRICE['value']).text[1:]
                }
            else:
                item_dict = {
                    'name': product.find_element_by_css_selector(locators.ITEM_NAME['value']).text,
                    'price': product.find_element_by_css_selector(locators.ITEM_PRICE['value']).text[1:]
                }

            items_in_payment_page.append(item_dict)

        return items_in_payment_page

    def login(self, username, password):
        logging.info('Signing in.')
        self.email_field.send_keys(username)
        self.password_field.send_keys(password)
        self.sign_in_button.click()

    def toggle_tos_checkbox(self):
        logging.info('Toggling "Terms of Service" checkbox.')
        self._click_with_javascript(locator=locators.TOS_CHECKBOX_LABEL)
        self._pause_for_animation()

    def wait_for_current_step_to_have_expected_text(self, expected_text):
        logging.info(f'Waiting for current step to contain "{expected_text}".')
        self._wait_for_expected_text_to_appear(locators.CURRENT_STEP, expected_text, timeout=20)

    def wait_for_bank_wire_or_check_payment_heading(self):
        logging.info('Waiting for "BANK-WIRE" or "CHECK" PAYMENT heading.')
        self._wait_for_element_to_appear(locator=locators.PAGE_SUBHEADING, timeout=20)

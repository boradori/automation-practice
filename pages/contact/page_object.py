import logging
import os

from . import locators
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class ContactPage(BasePage):
    @property
    def attach_file_field(self):
        return self._find_present_element(locators.ATTACH_FILE_FIELD)

    @property
    def success_message(self):
        return self._find_visible_element(locators.SUCCESS_MESSAGE, timeout=20).text

    def attach_file(self):
        logging.info('Attaching file.')
        if os.name == 'nt':
            self.attach_file_field.send_keys(os.getcwd() + '\\image.jpg')
        else:
            self.attach_file_field.send_keys(os.getcwd() + '/image.jpg')

    def click_submit_inquiry_button(self):
        logging.info('Clicking "Submit inquiry" button.')
        self._click(locators.SUBMIT_BUTTON)

    def choose_subject(self, subject):
        logging.info(f'Choosing subject, "{subject}".')
        select = Select(self._find(locators.SUBJECT_HEADING))
        select.select_by_visible_text(subject)

    def enter_email_address(self, email_address):
        logging.info(f'Entering email address: {email_address}')
        self._type(locators.EMAIL_FIELD, email_address, clear_input=True)

    def enter_message(self, message):
        logging.info(f'Entering message: "{message}".')
        self._type(locators.MESSAGE_FIELD, message, clear_input=True)

    def enter_order_reference_without_session(self, reference):
        logging.info(f'Entering order reference: {reference}')
        self._type(locators.ORDER_REF_FIELD, reference, clear_input=True)

    def select_order_reference_by_position_with_session(self, position):
        logging.info(f'Selecting order reference No, {position}')
        select = Select(self._find(locators.ORDER_REF_FIELD_SELECTOR))
        select.select_by_index(position)

    def select_product_reference_by_position_with_session(self, position):
        logging.info(f'Selecting product reference No, {position}')
        self._wait_for_element_to_appear(locator=locators.PRODUCT_REF_FIELD_SELECTOR)
        select = Select(self._find(locators.PRODUCT_REF_FIELD_SELECTOR))
        select.select_by_index(position)

    def select_product_reference_by_product_name(self, product_name):
        logging.info(f'Selecting product, "{product_name}".')
        self._wait_for_element_to_appear(locator=locators.PRODUCT_REF_FIELD_SELECTOR)
        select = Select(self._find(locators.PRODUCT_REF_FIELD_SELECTOR))
        select.select_by_visible_text(product_name)

    def wait_for_email_field_to_be_clickable(self):
        logging.info('Waiting for "Subject Heading" to be clickable.')
        self._find_clickable_element(locators.EMAIL_FIELD)

import logging

from . import locators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class Header(BasePage):
    @property
    def cart_items(self):
        return self._find_present_elements(locators.ITEMS_IN_CART)

    @property
    def empty(self):
        return self._find_present_element(locators.EMPTY).text

    @property
    def quantity(self):
        return int(self._find_present_element(locators.QUANTITY).text)

    def click_contact_us_button(self):
        logging.info('Clicking "Contact us" button.')
        self._click(locators.CONTACT_US_BUTTON)

    def logout(self):
        logging.info('Signing out.')
        self._click(locators.SIGN_OUT_BUTTON)

    def move_to_cart(self):
        logging.info('Moving to the "Cart".')
        self._scroll_to_element(locator=locators.CART)
        self._move_to_element(locator=locators.CART)
        self._wait_for_elements_to_appear(locators.ITEMS_IN_CART)

    def search_item(self, keyword):
        logging.info(f'Searching for "{keyword}".')
        self._type(locators.SEARCH_BOX, keyword, clear_input=True, terminate_with_return_key=True)

    def search_item_dropdown_by_keyword(self, keyword, number_of_arrow_downs=1):
        self._type(locators.SEARCH_BOX, keyword, clear_input=True)
        self._pause_for_animation(3)

        for _ in range(number_of_arrow_downs):
            self._type(locators.SEARCH_BOX, Keys.ARROW_DOWN)

        self._type(locators.SEARCH_BOX, Keys.ENTER)

    def wait_for_logo_image_to_appear(self):
        logging.info('Waiting for the LOGO image.')
        self._wait_for_element_to_appear(locator=locators.LOGO_IMAGE)

    def user_is_signed_in(self):
        element = self._find_present_element(locators.SIGN_IN_OR_USERNAME_BUTTON)
        if element.get_attribute('class') == 'account':
            return True
        elif element.get_attribute('class') == 'login':
            return False

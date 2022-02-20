import logging

from . import locators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @property
    def heading(self):
        return self._find_present_element(locators.HEADING).text

    def wait_for_heading_to_be_displayed(self):
        logging.info('Waiting for "Account" page "Heading" to be displayed.')
        self._wait_for_element_to_appear(locator=locators.HEADING)

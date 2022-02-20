import logging

from . import locators
from pages.base_page import BasePage


class FrontPage(BasePage):
    @property
    def best_seller_product_names(self):
        products = self._find_present_elements(locators.BEST_SELLER_PRODUCT_NAMES)
        return [' '.join(product.text.split()).strip() for product in products]

    @property
    def popular_product_names(self):
        products = self._find_present_elements(locators.POPULAR_PRODUCT_NAMES)
        return [' '.join(product.text.split()).strip() for product in products]

    def add_item_to_cart_by_item_name(self, item_name):
        logging.info(f'Adding "{item_name}" to the cart.')
        self._click(locators.add_to_cart_by_item_name(item_name))

    def click_proceed_to_checkout_button(self):
        logging.info('Clicking "Proceed to checkout" button.')
        self._click(locators.PROCEED_TO_CHECKOUT_BUTTON)

    def get_number_of_items_by_category(self, category):
        if category == 'Popular':
            logging.info('Getting the number of "Popular" product cards:')
            return len(self.popular_product_names)
        elif category == 'Best':
            logging.info('Getting the number of "Best Sellers" product cards:')
            return len(self.best_seller_product_names)

    def move_to_item_by_item_name(self, item_name):
        logging.info(f'Moving to "{item_name}".')
        self._scroll_to_element(locator=locators.item_by_item_name(item_name))
        self._move_to_element(locator=locators.item_by_item_name(item_name))

    def navigate(self):
        logging.info('Navigating to the "Front" page.')
        self._visit('http://automationpractice.com/index.php')

    def select_category(self, category):
        if category == 'Popular':
            self._click(locators.POPULAR_BUTTON)
            self._wait_for_element_attribute_to_contain_value(
                'class', 'active', locator=locators.POPULAR_PRODUCT_LIST_CONTAINER
            )
        elif category == 'Best':
            self._click(locators.BEST_SELLER_BUTTON)
            self._wait_for_element_attribute_to_contain_value(
                'class', 'active', locator=locators.BEST_SELLER_LIST_CONTAINER
            )

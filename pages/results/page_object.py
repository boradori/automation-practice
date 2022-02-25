import logging

from . import locators
from pages.base_page import BasePage


def get_item_details(item):
    item_name = item.find_element_by_css_selector('div:nth-child(2) a[class="product-name"]')
    item_price = item.find_element_by_css_selector('div:nth-child(2) > div > span[itemprop="price"]')

    return {
        'name': item_name.text.strip(),
        'price': item_price.text.strip()[1:]
    }


class ResultsPage(BasePage):
    @property
    def cart_items_quantity(self):
        return int(self._get_text_from_element(locators.CART_QUANTITY))

    @property
    def no_results(self):
        return self._find_present_element(locators.NO_RESULTS_HEADING)

    @property
    def no_results_heading(self):
        return self._get_text_from_element(locators.NO_RESULTS_HEADING)

    @property
    def product_names(self):
        return self._get_text_from_elements(locators.PRODUCT_NAMES)

    @property
    def results_heading(self):
        return self._get_text_from_element(locators.RESULTS_HEADING)

    def add_items_to_cart(self, items_list, proceed_to_checkout=False):
        cart_items = []

        products = self._find_present_elements(locators.PRODUCTS, timeout=20)

        for idx, position in enumerate(items_list):
            product = products[position - 1]
            self._pause_for_animation()

            self._scroll_to_element(locator=locators.product_by_product_position(position))
            self._move_to_element(locator=locators.product_by_product_position(position))
            self._click_with_javascript(locator=locators.add_to_cart_button_by_product_position(position))

            self._wait_for_element_to_appear(locator=locators.ITEM_MODAL)

            item = get_item_details(product)
            cart_items.append(item)

            if idx + 1 == len(items_list):
                if proceed_to_checkout:
                    self._click(locators.PROCEED_TO_CHECKOUT_BUTTON)
                else:
                    self._click(locators.CONTINUE_SHOPPING_BUTTON)
            else:
                self._click(locators.CONTINUE_SHOPPING_BUTTON)

        return cart_items

    def get_title_by_keyword(self, keyword):
        return self._get_text_from_element(locators.result_title_by_keyword(keyword))

    def wait_for_products_to_appear(self):
        logging.info('Waiting for "Products" to appear.')
        self._wait_for_element_to_appear(locator=locators.RESULTS_HEADING)
        self._wait_for_elements_to_appear(locators.PRODUCTS)

    def wait_for_no_results_heading_to_disappear(self, element):
        logging.info('Waiting for "No Results Heading" to disappear."')
        self._wait_for_element_to_disappear(element=element)

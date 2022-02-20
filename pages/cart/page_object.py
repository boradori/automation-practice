import logging

from . import locators
from pages.base_page import BasePage


class CartPage(BasePage):
    @property
    def empty_cart_message(self):
        return self._get_text_from_element(locators.EMPTY_CART_MESSAGE)

    @property
    def products(self):
        return self._find_present_elements(locators.PRODUCTS)

    @property
    def summary_products_quantity(self):
        return int(self._get_text_from_element(locators.SUMMARY_PRODUCTS_QUANTITY).split(' ')[0])

    @property
    def title(self):
        return self._get_text_from_element(locators.TITLE)

    def click_proceed_to_checkout_button(self):
        logging.info('Clicking "Proceed to checkout" button.')
        self._scroll_to_element(locator=locators.PROCEED_TO_CHECKOUT_BUTTON)
        self._click(locators.PROCEED_TO_CHECKOUT_BUTTON)

    def get_items_in_cart_page(self, more_details=True):
        logging.info('Getting item tables in the "Cart" page.')
        items_in_cart_page = []

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

            items_in_cart_page.append(item_dict)

        return items_in_cart_page

    def navigate(self):
        logging.info('Navigating to the "Cart" page.')
        self._visit('http://automationpractice.com/index.php?controller=order')

    def remove_all_items_from_cart(self):
        for item in self.products:
            delete_button = item.find_element_by_css_selector('i.icon-trash')
            delete_button.click()
            self._wait_for_element_to_disappear(element=item)

        self._wait_for_element_to_appear(locator=locators.EMPTY_CART_MESSAGE)

    def remove_item_from_cart_by_product_position(self, position):
        logging.info(f'Removing item No. {position} from the "Cart".')
        item_to_delete = self._find_clickable_element(locators.delete_button_by_product_position(position))
        item_to_delete.click()
        self._wait_for_element_to_disappear(element=item_to_delete)

    def wait_for_products_to_appear(self):
        logging.info('Waiting for "Products" to appear.')
        self._wait_for_elements_to_appear(locators.PRODUCTS)

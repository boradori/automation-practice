from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging


class ResultsPage(SeleniumDriver):
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.items_in_cart = []

    # locators
    _no_results_heading = (By.CSS_SELECTOR, "p[class='alert alert-warning']")
    _heading = (By.XPATH, "//h1[contains(text(), 'Search')]")
    _products = (By.CSS_SELECTOR, ".product-container")
    _item_name = (By.CSS_SELECTOR, "a[class='product-name']")
    _item_price = (By.CSS_SELECTOR, "span[itemprop='price']")

    _number_of_items_in_cart = (By.CSS_SELECTOR, "a[title='View my shopping cart'] > span[class='ajax_cart_quantity']")
    _items_in_cart = (By.CSS_SELECTOR, "dl[class='products'] > dt")

    _add_to_cart_btn = (By.CSS_SELECTOR, "a[title='Add to cart']")
    _continue_shopping = (By.CSS_SELECTOR, "span[title='Continue shopping']")
    _proceed_to_checkout = (By.CSS_SELECTOR, "a[title='Proceed to checkout']")

    def verify_search_no_results(self):
        no_result_heading = self.wait_for_element(self._no_results_heading)
        return self.is_element_present(None, no_result_heading)

    def verify_search_item_dropdown(self, keyword):
        return self.is_element_present((By.XPATH, f"//h1[contains(text(), '{keyword}')]"))

    def verify_search_results(self, keyword):
        heading = self.wait_for_element((By.XPATH, f"//span[contains(text(), '{keyword}')]"))
        products = self.wait_for_elements(self._products)
        return len(products) >= 1 and self.is_element_present(None, heading)

    def get_item_details(self, product):
        item_name = product.find_element(*self._item_name)
        item_price = product.find_element(*self._item_price)

        item_dict = {
            'name': item_name.text.strip(),
            'price': item_price.text.strip()[1:]
        }

        return item_dict

    def add_items_to_cart(self, items_list):
        time.sleep(3)
        products = self.wait_for_elements(self._products)

        for idx, num in enumerate(items_list):
            product = products[num - 1]
            ActionChains(self.driver).move_to_element(product).perform()
            add_to_cart_btn = product.find_element(*self._add_to_cart_btn)

            self.click_element_js(add_to_cart_btn)

            if idx + 1 == len(items_list):
                proceed_to_checkout_btn = self.wait_for_element(self._proceed_to_checkout)
                item = self.get_item_details(product)
                self.items_in_cart.append(item)
                self.click_element(None, proceed_to_checkout_btn)
            else:
                continue_shopping_btn = self.wait_for_element(self._continue_shopping)
                item = self.get_item_details(product)
                self.items_in_cart.append(item)
                self.click_element(None, continue_shopping_btn)

    def verify_cart_modal_with_correct_quantity(self):
        items_in_cart = self.get_elements(self._items_in_cart)
        return len(self.items_in_cart) == len(items_in_cart)

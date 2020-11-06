from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time


class CartPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.items_in_cart = []
        self.item_to_remove = {}

    # locators
    _cart_title = (By.ID, "cart_title")
    _empty_cart_msg = (By.XPATH, "//p[contains(text(), 'Your shopping cart is empty.')]")
    _number_of_items_in_cart = (By.CSS_SELECTOR, "span[class='ajax_cart_quantity']:nth-child(2)")
    _cart_items = (By.CSS_SELECTOR, "table#cart_summary tbody > tr")
    _first_cart_item = (By.CSS_SELECTOR, "table#cart_summary tbody > tr:nth-child(1)")
    _item_name = (By.CSS_SELECTOR, "p.product-name > a")
    _item_sku = (By.XPATH, "//small[contains(text(), 'SKU :')]")
    _item_color = (By.XPATH, "//td[@class='cart_description']//a[contains(text(), 'Color : ')]")
    _item_price = (By.CSS_SELECTOR, "td[class='cart_total'] span")
    _delete_item_btn = (By.CSS_SELECTOR, "i.icon-trash")

    _total_products = (By.ID, "total_product")
    _total_shipping = (By.ID, "total_shipping")
    _total_before_tax = (By.ID, "total_price_without_tax")
    _tax = (By.ID, "total_tax")
    _total_after_tax = (By.ID, "total_price_container")

    def get_items_in_cart(self, more_details=True):
        cart_items = self.get_elements(self._cart_items)
        items_in_cart = []

        for item in cart_items:
            if more_details:
                item_dict = {
                    'name': item.find_element(*self._item_name).text,
                    'sku': item.find_element(*self._item_sku).text[6:],
                    'color': item.find_element(*self._item_color).text[8:],
                    'price': item.find_element(*self._item_price).text[1:]
                }
            else:
                item_dict = {
                    'name': item.find_element(*self._item_name).text,
                    'price': item.find_element(*self._item_price).text[1:]
                }

            items_in_cart.append(item_dict)

        return items_in_cart

    def verify_cart_with_correct_quantity(self):
        cart_items = self.get_elements(self._cart_items)
        return len(cart_items) == int()

    def remove_an_item_from_cart(self, row_number):
        self.items_in_cart = self.get_items_in_cart()

        cart_items = self.get_elements(self._cart_items)
        item_to_remove = cart_items[row_number - 1]

        self.item_to_remove = {
            'name': item_to_remove.find_element(*self._item_name).text,
            'sku': item_to_remove.find_element(*self._item_sku).text[6:],
            'color': item_to_remove.find_element(*self._item_color).text[8:],
            'price': item_to_remove.find_element(*self._item_price).text[1:]
        }

        delete_btn = item_to_remove.find_element(*self._delete_item_btn)
        self.click_element(None, delete_btn)

        time.sleep(3)

    def verify_item_is_removed_from_cart(self):
        new_items_in_cart = self.get_items_in_cart()
        return list(filter(lambda x: x != self.item_to_remove,
                           self.items_in_cart)) == new_items_in_cart

    def remove_all_items_from_cart(self):
        cart_items = self.get_elements(self._cart_items)

        for item in cart_items:
            delete_btn = item.find_element(*self._delete_item_btn)
            self.click_element(None, delete_btn)

            time.sleep(3)

        self.wait_for_element(self._empty_cart_msg)

    def verify_cart_is_empty(self):
        return self.is_element_present(self._empty_cart_msg) and not self.is_element_present(self._cart_items)

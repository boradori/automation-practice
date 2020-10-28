from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
from selenium.webdriver.common.keys import Keys
import time
import logging


class FrontPage(SeleniumDriver):
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _logo_img = (By.CSS_SELECTOR, "img[class='logo img-responsive']")
    _popular_btn = (By.CSS_SELECTOR, "a[class='homefeatured']")
    _best_sellers_btn = (By.CSS_SELECTOR, "a[class='blockbestsellers']")
    _popular_product_names = (By.XPATH, "//ul[@id='homefeatured']/*/div[@class='product-container']/div["
                                       "@class='right-block']/*/a[@class='product-name']")
    _best_sellers_product_names = (By.CSS_SELECTOR, "#blockbestsellers .product-container .right-block .product-name")
    _search_box = (By.ID, "search_query_top")
    _submit_search_btn = (By.CSS_SELECTOR, "button[name='submit_search']")

    _printed_title = (By.XPATH, "//span[contains(text(), 'printed')]")

    _faded_short_sleeve = (By.XPATH, "//div[@class='right-block']/h5/a[@title='Faded Short Sleeve T-shirts']")
    _add_faded_short_sleeve_to_cart_btn = (By.XPATH, "//div[@class='right-block']/h5/a[@title='Faded Short Sleeve "
                                                     "T-shirts']/../../div[@class='button-container']//span[text() = "
                                                     "'Add to cart']")
    _proceed_to_checkout_btn = (By.XPATH, "//span[contains(text(),'Proceed to checkout')]")
    _cart_title = (By.ID, "cart_title")

    def get_popular_product_cards(self):
        return self.get_elements(self._popular_product_names)

    def get_best_sellers_product_cards(self):
        return self.get_elements(self._best_sellers_product_names)

    def get_faded_short_sleeve(self):
        return self.get_element(self._faded_short_sleeve)

    def move_to_faded_short_sleeve(self):
        faded_short_sleeve = self.get_element(self._faded_short_sleeve)
        self.move_to_element(faded_short_sleeve)

    def add_faded_short_sleeve_to_cart(self):
        self.click_element(self._add_faded_short_sleeve_to_cart_btn)

    def get_proceed_to_checkout_btn(self):
        return self.get_element(self._proceed_to_checkout_btn)

    def verify_number_of_items(self, total):
        self.wait_for_element(self._logo_img)
        self.log.info(f'Number of product cards: {len(self.get_popular_product_cards())}')
        return len(self.get_popular_product_cards()) == total

    def verify_popular_items(self, first_item, last_item):
        self.click_element(self._popular_btn)
        popular_products = self.get_popular_product_cards()
        item_1 = popular_products[0].get_attribute('title')
        item_2 = popular_products[6].get_attribute('title')
        is_popular_active = self.is_element_present(
            (By.XPATH, "//ul[@id='homefeatured' and contains(@class, 'active')]"))
        is_best_sellers_active = self.is_element_present(
            (By.XPATH, "//ul[@id='blockbestsellers' and contains(@class, 'active')]"))
        return item_1 == first_item and item_2 == last_item and len(popular_products) == 7 and is_popular_active and not is_best_sellers_active

    def verify_best_sellers_items(self, first_item, last_item):
        self.click_element(self._best_sellers_btn)
        best_seller_products = self.get_best_sellers_product_cards()
        item_1 = best_seller_products[0].get_attribute('title')
        item_2 = best_seller_products[6].get_attribute('title')
        is_popular_active = self.is_element_present(
            (By.XPATH, "//ul[@id='homefeatured' and contains(@class, 'active')]"))
        is_best_sellers_active = self.is_element_present(
            (By.XPATH, "//ul[@id='blockbestsellers' and contains(@class, 'active')]"))
        return item_1 == first_item and item_2 == last_item and len(best_seller_products) == 7 and is_best_sellers_active and not is_popular_active

    def search_item_dropdown(self, keyword):
        search_box = self.get_element(self._search_box)
        self.send_keys(keyword, self._search_box)
        time.sleep(3)
        search_box.send_keys(Keys.ARROW_DOWN)
        search_box.send_keys(Keys.ENTER)

    def search_items(self, keyword):
        self.send_keys((keyword, Keys.ENTER), self._search_box)

    def verity_cart_page(self):
        return self.is_element_present(self._cart_title)

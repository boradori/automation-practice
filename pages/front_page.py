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
    _popular_btn = (By.CSS_SELECTOR, "a[class='homefeatured']")
    _best_sellers_btn = (By.CSS_SELECTOR, "a[class='blockbestsellers']")
    _popular_product_names = (By.XPATH, "//ul[@id='homefeatured']/*/div[@class='product-container']/div["
                                       "@class='right-block']/*/a[@class='product-name']")
    _best_sellers_product_names = (By.CSS_SELECTOR, "#blockbestsellers .product-container .right-block .product-name")
    _search_box = (By.ID, "search_query_top")
    _submit_search_btn = (By.XPATH, "//button[@name='submit_search']")
    _blouse_title = (By.XPATH, "//h1[contains(text(), 'Blouse')]")
    _printed_title = (By.XPATH, "//span[contains(text(), 'printed')]")

    def get_popular_product_cards(self):
        return self.get_elements(self._popular_product_names)

    def get_best_sellers_product_cards(self):
        return self.get_elements(self._best_sellers_product_names)

    def verify_number_of_items(self, total):
        self.log.info(f'Number of product cards: {len(self.get_popular_product_cards())}')
        return len(self.get_popular_product_cards()) == total

    def verify_popular_items(self, first_item, last_item):
        self.click_element(self._popular_btn)
        item_1 = self.get_popular_product_cards()[0].get_attribute('title')
        item_2 = self.get_popular_product_cards()[6].get_attribute('title')
        is_popular_active = self.is_element_present(
            (By.XPATH, "//ul[@id='homefeatured' and contains(@class, 'active')]"))
        return item_1 == first_item and item_2 == last_item and is_popular_active

    def verify_best_sellers_items(self, first_item, last_item):
        self.click_element(self._best_sellers_btn)
        item_1 = self.get_best_sellers_product_cards()[0].get_attribute('title')
        item_2 = self.get_best_sellers_product_cards()[6].get_attribute('title')
        is_best_sellers_active = self.is_element_present(
            (By.XPATH, "//ul[@id='blockbestsellers' and contains(@class, 'active')]"))
        return item_1 == first_item and item_2 == last_item and is_best_sellers_active

    def verify_search_dropdown(self):
        search_box = self.get_element(self._search_box)
        self.send_keys('blouse', self._search_box)
        time.sleep(3)
        search_box.send_keys(Keys.ARROW_DOWN)
        search_box.send_keys(Keys.ENTER)
        return self.is_element_present(self._blouse_title)

    def verify_search_results(self):
        search_box = self.get_element(self._search_box)
        self.send_keys('printed', self._search_box)
        search_box.send_keys(Keys.ENTER)
        heading = self.wait_for_element(self._printed_title)
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".product-container")) == 5 and heading
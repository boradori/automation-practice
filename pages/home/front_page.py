from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
import logging


class FrontPage(SeleniumDriver):
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    popular_btn = (By.CSS_SELECTOR, "a[class='homefeatured']")
    best_sellers_btn = (By.CSS_SELECTOR, "a[class='blockbestsellers']")
    popular_product_names = (By.XPATH, "//ul[@id='homefeatured']/*/div[@class='product-container']/div["
                                       "@class='right-block']/*/a[@class='product-name']")
    best_sellers_product_names = (By.CSS_SELECTOR, "#blockbestsellers .product-container .right-block .product-name")

    def get_popular_product_cards(self):
        return self.driver.find_elements(*self.popular_product_names)

    def get_best_sellers_product_cards(self):
        return self.driver.find_elements(*self.best_sellers_product_names)

    def verify_number_of_items(self, total):
        self.log.info(f'Number of product cards: {len(self.get_popular_product_cards())}')
        return len(self.get_popular_product_cards()) == total

    def verify_popular_items(self, first_item, last_item):
        self.driver.find_element(*self.popular_btn).click()
        item_1 = self.get_popular_product_cards()[0].get_attribute('title')
        item_2 = self.get_popular_product_cards()[6].get_attribute('title')
        is_popular_active = self.is_element_present(
            (By.XPATH, "//ul[@id='homefeatured' and contains(@class, 'active')]"))
        return item_1 == first_item and item_2 == last_item and is_popular_active

    def verify_best_sellers_items(self, first_item, last_item):
        self.driver.find_element(*self.best_sellers_btn).click()
        item_1 = self.get_best_sellers_product_cards()[0].get_attribute('title')
        item_2 = self.get_best_sellers_product_cards()[6].get_attribute('title')
        is_best_sellers_active = self.is_element_present(
            (By.XPATH, "//ul[@id='blockbestsellers' and contains(@class, 'active')]"))
        return item_1 == first_item and item_2 == last_item and is_best_sellers_active

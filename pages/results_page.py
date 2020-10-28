from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
from selenium.webdriver.common.keys import Keys
import time
import logging


class ResultsPage(SeleniumDriver):
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _heading = (By.XPATH, "//h1[contains(text(), 'Search')]")
    _products = (By.CSS_SELECTOR, ".product-container")

    def verify_search_item_dropdown(self, keyword):
        return self.is_element_present((By.XPATH, f"//h1[contains(text(), '{keyword}')]"))

    def verify_search_results(self, keyword):
        heading = self.wait_for_element((By.XPATH, f"//span[contains(text(), '{keyword}')]"))
        products = self.wait_for_elements(self._products)
        return len(products) >= 1 and self.is_element_present(None, heading)

from utilities.custom_logger import custom_logger
import logging
import time
import os
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumDriver:
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_screenshot(self, message):
        file_name = message + "_" + str(round(time.time() * 1000)) + ".png"
        screenshot_dir = "../screenshots/"
        relative_file_name = screenshot_dir + file_name
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, relative_file_name)
        destination_dir = os.path.join(current_dir, screenshot_dir)

        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred when taking screenshot")

    def wait_for_element(self, locator):
        element = None
        wait = WebDriverWait(self.driver, 5, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        try:
            element = wait.until(lambda dr: dr.find_element(*locator))
            self.log.info("Wait for " + locator[1])
        except:
            self.log.info("Element does not show up for 5 seconds with locator: " + locator[1])
        return element

    def wait_for_elements(self, locator):
        elements = None
        wait = WebDriverWait(self.driver, 5, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        try:
            elements = wait.until(lambda dr: dr.find_elements(*locator))
            self.log.info("Wait for locator: " + locator[1])
        except:
            self.log.info("Element does not show up for 5 seconds with locator: " + locator[1])
        return elements

    def get_element(self, locator):
        element = None
        try:
            element = self.wait_for_element(locator)
            self.log.info("Element found with locator: " + locator[1])
        except:
            self.log.info("Element not found with locator: " + locator[1])
        return element

    def get_elements(self, locator):
        elements = None
        try:
            elements = self.wait_for_elements(locator)
            self.log.info("Element list found with locator: " + locator[1])
        except:
            self.log.info("Element list not found with locator: " + locator[1])
        return elements

    def click_element(self, locator):
        try:
            element = self.get_element(locator)
            element.click()
            self.log.info("Clicked on element with locator: " + locator[1])
        except:
            self.log.info("Cannot click on the element with locator " + locator[1])

    def send_keys(self, data, locator):
        try:
            element = self.get_element(locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator[1])
        except:
            self.log.info("Cannot send data on the element with locator: " + locator[1])

    def is_element_present(self, locator):
        try:
            if locator:
                element = self.get_element(locator)

                if element is not None:
                    self.log.info("Element is present with locator: " + locator[1])
                    return True
                else:
                    self.log.info("Element is NOT present with locator: " + locator[1])
                    return False
            else:
                self.log.info("Element is NOT present with locator: " + locator[1])
                return False
        except:
            self.log.info("Element is NOT present with locator: " + locator[1])
            return False

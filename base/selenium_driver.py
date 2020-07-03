from utilities.custom_logger import custom_logger
from utilities.util import Util
import logging
import time
import os


class SeleniumDriver:
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.util = Util()

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

    def get_element(self, locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
            self.log.info("Element found with locator: " + locator)
        except:
            self.log.info("Element not found with locator: " + locator)
        return element

    def get_element_list(self, locator):
        elements = None
        try:
            elements = self.driver.find_elements(*locator)
            self.log.info("Element list found with locator: " + locator)
        except:
            self.log.info("Element list not found with locator: " + locator)
        return elements

    def click_element(self, locator):
        try:
            element = self.get_element(locator)
            element.click()
            self.log.info("Clicked on element with locator: " + locator)
        except:
            self.log.info("Cannot click on the element with locator " + locator)

    def send_keys(self, data, locator):
        try:
            element = self.get_element(locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator)

    def is_element_present(self, locator):
        try:
            if locator:
                # element = self.driver.find_element(*locator)
                element = self.get_element(locator)
                if element is not None:
                    self.log.info("Element is present")
                    return True
                else:
                    self.log.info("Element not present")
                    return False
            else:
                self.log.info("Element not present")
                return False
        except:
            print("Element not found")
            return False

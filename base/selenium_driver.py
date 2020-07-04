from utilities.custom_logger import custom_logger
from utilities.util import Util
import logging
import time
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumDriver:
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.util = Util()

    def get_screenshot(self, message):
        file_name = message + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshot_directory = "../screenshots/"
        screenshot_path = screenshot_directory + file_name
        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info("Screenshot saved to directory : " + screenshot_path)
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
            self.get_screenshot(locator[1])
        return element

    def wait_for_elements(self, locator):
        elements = None
        wait = WebDriverWait(self.driver, 5, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        try:
            elements = wait.until(lambda dr: dr.find_elements(*locator))
            self.log.info("Wait for " + locator[1])
        except:
            self.log.info("Element does not show up for 5 seconds with locator: " + locator[1])
            self.get_screenshot(locator[1])
        return elements

    def get_element(self, locator):
        element = None
        try:
            # element = self.driver.find_element(*locator)
            element = self.wait_for_element(locator)
            self.log.info("Element found with locator: " + locator[1])
        except:
            self.log.info("Element not found with locator: " + locator[1])
            self.get_screenshot(locator[1])
        return element

    def get_element_list(self, locator):
        elements = None
        try:
            # elements = self.driver.find_elements(*locator)
            elements = self.wait_for_elements(locator)
            self.log.info("Element list found with locator: " + locator[1])
        except:
            self.log.info("Element list not found with locator: " + locator[1])
            self.get_screenshot(locator[1])
        return elements

    def click_element(self, locator):
        try:
            element = self.get_element(locator)
            element.click()
            self.log.info("Clicked on element with locator: " + locator[1])
        except:
            self.log.info("Cannot click on the element with locator " + locator[1])
            self.get_screenshot(locator[1])

    def send_keys(self, data, locator):
        try:
            element = self.get_element(locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator[1])
        except:
            self.log.info("Cannot send data on the element with locator: " + locator[1])
            self.get_screenshot(locator[1])

    def is_element_present(self, locator):
        try:
            if locator:
                # element = self.driver.find_element(*locator)
                element = self.get_element(locator)
                # element = self.wait_for_element(locator)

                if element is not None:
                    self.log.info("Element is present with locator: " + locator[1])
                    return True
                else:
                    self.log.info("Element is NOT present with locator: " + locator[1])
                    self.get_screenshot(locator[1])
                    return False
            else:
                self.log.info("Element is NOT present with locator: " + locator[1])
                self.get_screenshot(locator[1])
                return False
        except:
            self.log.info("Element is NOT present with locator: " + locator[1])
            self.get_screenshot(locator[1])
            return False

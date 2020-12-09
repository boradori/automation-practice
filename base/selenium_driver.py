from utilities.custom_logger import custom_logger
import logging
import time
import os
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumDriver:
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1,
                                  ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                      NoSuchElementException])

    def navigate_to_front_page(self):
        self.driver.get("http://automationpractice.com/index.php")

    def navigate_to_login_page(self):
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

    def navigate_to_cart_page(self):
        self.driver.get("http://automationpractice.com/index.php?controller=order")

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

    def wait_for_element(self, locator, until=True):
        element = None

        try:
            if until:
                element = self.wait.until(lambda dr: dr.find_element(*locator))
                self.log.info("Wait for " + locator[1])
            else:
                element = self.wait.until_not(lambda dr: dr.find_element(*locator))
                self.log.info("Wait for " + locator[1] + " to be NOT present")
        except:
            self.log.info("Element does not show up for 5 seconds with locator: " + locator[1])
        return element

    def wait_for_elements(self, locator, until=True):
        elements = None

        try:
            if until:
                elements = self.wait.until(lambda dr: dr.find_elements(*locator))
                self.log.info("Wait for locator: " + locator[1])
            else:
                elements = self.wait.until_not(lambda dr: dr.find_elements(*locator))
                self.log.info("Wait for locator: " + locator[1] + " to be NOT present")
        except:
            self.log.info("Elements do not show up for 5 seconds with locator: " + locator[1])
        return elements

    def get_element(self, locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
            self.log.info("Element found with locator: " + locator[1])
        except:
            self.log.info("Element not found with locator: " + locator[1])
        return element

    def get_elements(self, locator):
        elements = None
        try:
            elements = self.driver.find_elements(*locator)
            self.log.info("Element list found with locator: " + locator[1])
        except:
            self.log.info("Element list not found with locator: " + locator[1])
        return elements

    def click_element(self, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
                element.click()
                self.log.info("Clicked on element with locator: " + locator[1])
            elif element:
                element.click()
                self.log.info("Clicked on element")
        except:
            if locator:
                self.log.info("Cannot click on element with locator " + locator[1])
            elif element:
                self.log.info("Cannot click on element")

    def click_element_js(self, element):
        try:
            if element:
                self.driver.execute_script("arguments[0].click();", element)
                self.log.info("Clicked on element with js executor method")
        except:
            self.log.info("Cannot click on element with js executor method")

    def send_keys(self, data, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
                element.send_keys(data)
                self.log.info("Sent data on element with locator: " + locator[1])
            elif element:
                element.send_keys(data)
                self.log.info("Sent data on element")
        except:
            if locator:
                self.log.info("Cannot send data on the element with locator: " + locator[1])
            elif element:
                self.log.info("Cannot send data on the element")

    def clear_field(self, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
                element.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
                self.log.info("Cleared field on element with locator: " + locator[1])
            elif element:
                element.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
                self.log.info("Cleared field on element")
        except:
            if locator:
                self.log.info("Cannot clear field on the element with locator: " + locator[1])
            elif element:
                self.log.info("Cannot clear field on the element")

    def is_element_present(self, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
            if element:
                if locator:
                    self.log.info("Element is present with locator: " + locator[1])
                else:
                    self.log.info("Element is present")
                return True
            else:
                self.log.info("Element is NOT present")
                return False
        except:
            self.log.info("Element is NOT present")
            return False

    def are_elements_present(self, locator, elements=None):
        try:
            if locator:
                elements = self.get_elements(locator)
            if elements:
                if locator:
                    self.log.info("Elements are present with locator: " + locator[1])
                else:
                    self.log.info("Elements are present")
                return True
            else:
                self.log.info("Elements are NOT present")
                return False
        except:
            self.log.info("Elements are NOT present")
            return False

    def is_element_enabled(self, locator, element=None):
        is_enabled = False
        try:
            if locator:
                element = self.get_element(locator)
            if element:
                is_enabled = element.is_enabled()
                if locator:
                    self.log.info("Element is enabled with locator: " + locator[1])
                else:
                    self.log.info("Element is enabled")
            else:
                self.log.info("Element is disabled")
            return is_enabled
        except:
            self.log.info("Element is disabled")
            return False

    def is_element_displayed(self, locator, element=None):
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator)
            if element:
                is_displayed = element.is_displayed()
                if locator:
                    self.log.info("Element is displayed with locator: " + locator[1])
                else:
                    self.log.info("Element is displayed")
            else:
                self.log.info("Element is NOT displayed")
            return is_displayed
        except:
            self.log.info("Element is NOT displayed")
            return False

    def move_to_element(self, element, x=None, y=None):
        if x is None and y is None:
            self.actions.move_to_element(element).perform()
        elif x is not None and y is not None:
            self.actions.move_to_element_with_offset(element, x, y).perform()

    def web_scroll(self, direction):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        elif direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def scroll_into_view_js(self, element):
        try:
            if element:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.log.info("Scroll into element with js executor method")
        except:
            self.log.info("Cannot scroll into element with js executor method")


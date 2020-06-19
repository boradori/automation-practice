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

    def is_element_present(self, element):
        try:
            if element is not None:
                self.log.info("Element present: " + element)
                return True
            else:
                self.log.info("Element not present")
                return False
        except:
            print("Element not found")
            return False

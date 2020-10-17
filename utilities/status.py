from utilities.custom_logger import custom_logger
from base.selenium_driver import SeleniumDriver
import logging


class Status(SeleniumDriver):
    log = custom_logger(logging.INFO)

    def __init__(self, driver):
        super(Status, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("------ SUCCESSFUL :: + " + message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("------ FAILED :: + " + message)
                    self.get_screenshot(message)
            else:
                self.result_list.append("FAIL")
                self.log.error("------ FAILED :: + " + message)
                self.get_screenshot(message)
        except:
            self.result_list.append("FAIL")
            self.log.error("------ EXCEPTION Occurred")
            self.get_screenshot(message)

    # def mark(self, result, message):
    #     self.set_result(result, message)

    def mark(self, result, message):
        self.set_result(result, message)

        if "FAIL" in self.result_list:
            self.log.error("------ TEST FAILED\n")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info("------ TEST SUCCESSFUL\n")
            self.result_list.clear()
            assert True == True

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *


class Util(object):
    def wait(self, driver):
        return WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_webdriver(self):
        base_url = "http://automationpractice.com/index.php"

        if self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "ie":
            driver = webdriver.Ie()
        elif self.browser == "safari":
            driver = webdriver.Safari()
        else:
            driver = webdriver.Chrome()

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        driver.maximize_window()

        driver.get(base_url)
        return driver

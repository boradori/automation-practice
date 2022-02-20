import pytest

from tests import config
from selenium import webdriver


def get_driver(desired_browser):
    if desired_browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        driver = webdriver.Chrome(chrome_options=options)
    elif desired_browser == 'firefox':
        driver = webdriver.Firefox()
    elif desired_browser == 'safari':
        driver = webdriver.Safari()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        driver = webdriver.Chrome(chrome_options=options)

    return driver


@pytest.fixture()
def driver(request):
    _driver = get_driver(config.browser)
    # _driver.maximize_window()
    _driver.set_window_position(0, 0)
    _driver.set_window_size(1920, 1080)

    config.driver = _driver

    def quit_driver():
        _driver.quit()

    request.addfinalizer(quit_driver)

    _driver.implicitly_wait(10)
    _driver.get(config.base_url)

    return _driver


@pytest.fixture(scope='session')
def session_driver(request):
    _driver = get_driver(config.browser)
    # _driver.maximize_window()
    _driver.set_window_position(0, 0)
    _driver.set_window_size(1920, 1080)

    config.driver = _driver

    def quit_driver():
        _driver.quit()

    request.addfinalizer(quit_driver)

    return _driver

import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.fixture()
def setup():
    print('Running method level setup')
    yield
    print('Running method level teardown')


@pytest.fixture(scope='class')
def one_time_setup(request):
    print('Running one_time_setup')

    browser = request.config.getoption('--browser')

    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver()

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.browser = browser

    yield driver
    driver.quit()
    print('Running one_time_teardown')


def pytest_addoption(parser):
    parser.addoption('--browser')

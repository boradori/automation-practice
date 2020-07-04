import pytest
from base.webdriverfactory import WebDriverFactory
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture(scope='function')
def setup():
    print('Running method level setup')
    yield
    print('Running method level teardown')


@pytest.fixture(scope='function')
def front_page_setup():
    print('Running method level setup: front_page')
    yield
    print('Running method level teardown: front_page')


@pytest.fixture(scope='class')
def class_setup(request):
    print('Running class_setup')

    browser = request.config.getoption('--browser')

    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver()
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.login('revay29821@zkeiw.com', 'RA^@*95QaOav')
    login_page.navigate_to_front_page()

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.browser = browser

    yield driver
    driver.quit()
    print('Running class_teardown')

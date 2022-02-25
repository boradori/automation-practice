from tests import config

pytest_plugins = ['tests.fixtures.driver', 'tests.fixtures.page_objects', 'tests.fixtures.components']


def pytest_addoption(parser):
    # https://docs.python.org/2/library/argparse.html#action
    parser.addoption('--browser', action='store', default='chrome')


def pytest_sessionstart(session):
    # https://docs.pytest.org/en/6.2.x/example/simple.html
    config.browser = session.config.getoption('--browser')
    config.base_url = 'http://automationpractice.com/index.php'


# @pytest.fixture(scope='class')
# def class_setup(request):
#     print('Running class_setup')
#
#     browser = request.config.getoption('--browser')
#
#     wdf = WebDriverFactory(browser)
#     driver = wdf.get_webdriver()
#
#     if request.cls is not None:
#         request.cls.driver = driver
#         request.cls.browser = browser
#
#     yield driver
#     driver.quit()
#     print('Running class_teardown')

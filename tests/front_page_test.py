from pages.front_page import FrontPage
from pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures('class_setup')
class FrontPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.front_page = FrontPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=3)
    def test_number_of_items(self):
        self.ts.mark(self.front_page.verify_number_of_items(7), 'Number of items on front page test')

    @pytest.mark.run(order=4)
    def test_popular_items(self):
        self.ts.mark(self.front_page.verify_popular_items('Faded Short Sleeve T-shirts',
                                                          'Printed Chiffon Dress'),
                     'Popular items test')

    @pytest.mark.run(order=5)
    def test_best_sellers_items(self):
        self.ts.mark(self.front_page.verify_best_sellers_items('Printed Chiffon Dress',
                                                               'Printed Dress'),
                     'Best sellers items test')

    @pytest.mark.run(order=6)
    def test_search_dropdown(self):
        self.ts.mark(self.front_page.verify_search_dropdown(), 'Search dropdown test')

    @pytest.mark.run(order=7)
    def test_search_results(self):
        self.ts.mark(self.front_page.verify_search_results(), 'Search results test')

    @pytest.mark.run(order=8)
    def test_add_to_cart_no_session(self):
        if self.login_page.verify_login_successful():
            self.login_page.logout()
            self.driver.get("http://automationpractice.com/index.php")
            self.driver.implicitly_wait(5)
            ActionChains(self.driver).move_to_element(self.front_page.get_faded_short_sleeve()).perform()
            self.front_page.add_faded_short_sleeve_to_cart()
            self.front_page.get_proceed_to_checkout_btn().click()
            self.ts.mark_final(self.front_page.verity_cart_page(), 'Add to cart w/o session test')

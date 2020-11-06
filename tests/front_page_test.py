from pages.front_page import FrontPage
from pages.login_page import LoginPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures('class_setup_with_login')
class FrontPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.front_page = FrontPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.status = Status(self.driver)

    @pytest.mark.run(order=3)
    def test_number_of_items(self):
        self.login_page.navigate_to_front_page()
        self.status.mark(self.front_page.verify_number_of_items(7), 'Number of items on front page test')

    @pytest.mark.run(order=4)
    def test_popular_items(self):
        self.status.mark(self.front_page.verify_popular_items('Faded Short Sleeve T-shirts',
                                                              'Printed Chiffon Dress'),
                         'Popular items test')

    @pytest.mark.run(order=5)
    def test_best_sellers_items(self):
        self.status.mark(self.front_page.verify_best_sellers_items('Printed Chiffon Dress',
                                                                   'Printed Dress'),
                         'Best sellers items test')

    @pytest.mark.run(order=6)
    def test_add_to_cart_no_session(self):
        if self.login_page.verify_login_successful():
            self.login_page.logout()

        self.login_page.navigate_to_front_page()
        self.driver.implicitly_wait(5)
        self.front_page.move_to_faded_short_sleeve()
        self.front_page.add_faded_short_sleeve_to_cart()
        self.front_page.get_proceed_to_checkout_btn().click()
        result1 = self.front_page.verity_cart_page()
        self.status.mark(result1, 'Add to cart w/o session test')

        self.front_page.navigate_to_login_page()
        self.login_page.login('revay29821@zkeiw.com', 'RA^@*95QaOav')
        result2 = self.login_page.verify_number_of_items_in_cart()
        self.status.mark(result2, 'Add to cart w/o session preserves items in cart test')

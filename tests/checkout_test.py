from pages.front_page import FrontPage
from pages.results_page import ResultsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures('class_setup')
class CheckoutTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.front_page = FrontPage(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.status = Status(self.driver)

    @pytest.mark.run(order=14)
    def test_order_summary_and_sign_in(self):
        self.front_page.search_items('printed')
        self.results_page.add_items_to_cart([1, 3, 5])
        self.cart_page.click_proceed_to_checkout()

        result = self.checkout_page.verify_authentication()
        self.status.mark(result, 'Checkout sign in flow test')

    @pytest.mark.run(order=15)
    def test_address(self):
        self.checkout_page.login('revay29821@zkeiw.com', 'RA^@*95QaOav')
        self.checkout_page.add_comment("Hello comment")

        result = self.checkout_page.verify_address()
        self.status.mark(result, 'Checkout address test')

    @pytest.mark.run(order=16)
    def test_shipping(self):
        self.checkout_page.click_proceed_to_checkout_address_btn()
        self.checkout_page.click_proceed_to_checkout_shipping_btn()

        result1 = self.checkout_page.verify_tos_error_message()
        self.status.mark(result1, 'Shipping tos error message test')

        self.checkout_page.dismiss_error_msg()
        self.checkout_page.check_tos()
        self.checkout_page.click_proceed_to_checkout_shipping_btn()

        result2 = self.checkout_page.verify_payment_heading()
        self.status.mark(result2, 'Shipping proceed with tos agreement test')

    @pytest.mark.run(order=17)
    def test_payment(self):
        self.checkout_page.pay_by_bank_wire()

        result1 = self.checkout_page.verify_pay_by_bank_wire()
        self.status.mark(result1, 'Pay by bank wire')

        self.checkout_page.click_confirm_btn()

        result2 = self.checkout_page.verify_complete_message()

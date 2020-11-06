from pages.front_page import FrontPage
from pages.results_page import ResultsPage
from pages.cart_page import CartPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures('class_setup')
class CartTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.front_page = FrontPage(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.status = Status(self.driver)

    @pytest.fixture()
    def clear_cart_teardown(self):
        yield
        self.results_page.navigate_to_cart_page()
        self.cart_page.remove_all_items_from_cart()

    @pytest.mark.run(order=10)
    @pytest.mark.usefixtures('clear_cart_teardown')
    def test_add_items_to_cart(self):
        self.front_page.navigate_to_front_page()
        self.front_page.search_items('printed')
        self.results_page.add_items_to_cart([1, 3, 5])

        result1 = self.results_page.verify_cart_modal_with_correct_quantity()
        self.status.mark(result1, 'Add multiple products to cart test')

    @pytest.mark.run(order=11)
    def test_items_in_results_page_and_cart_page(self):
        self.front_page.navigate_to_front_page()
        self.front_page.search_items('printed')
        self.results_page.add_items_to_cart([1, 3, 5])

        items_in_results_page = self.results_page.items_in_cart
        items_in_cart_page = self.cart_page.get_items_in_cart(False)

        result = items_in_results_page == items_in_cart_page
        self.status.mark(result, 'Matching items in cart from results page and cart page test')

    @pytest.mark.run(order=12)
    def test_remove_an_item_from_cart(self):
        self.results_page.navigate_to_cart_page()
        self.driver.implicitly_wait(5)
        self.cart_page.remove_an_item_from_cart(2)

        result = self.cart_page.verify_item_is_removed_from_cart()
        self.status.mark(result, 'Remove an item from cart test')

    @pytest.mark.run(order=13)
    def test_remove_all_items_from_cart(self):
        self.cart_page.remove_all_items_from_cart()

        result = self.cart_page.verify_cart_is_empty()
        self.status.mark(result, 'Remove all items from cart test')

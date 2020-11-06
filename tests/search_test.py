from pages.front_page import FrontPage
from pages.results_page import ResultsPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures('class_setup_with_login')
class SearchTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.front_page = FrontPage(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.status = Status(self.driver)

    @pytest.mark.run(order=7)
    def test_no_results(self):
        self.front_page.navigate_to_front_page()
        self.front_page.search_items('askldfjaslkdfjklsaf')
        result = self.results_page.verify_search_no_results()
        self.status.mark(result, 'Search items with no results test')

    @pytest.mark.run(order=8)
    def test_search_item_dropdown(self):
        self.front_page.navigate_to_front_page()
        self.front_page.search_item_dropdown('Printed Summer Dress')
        result = self.results_page.verify_search_item_dropdown('Printed Summer Dress')
        self.status.mark(result, 'Search an item via dropdown test')

    @pytest.mark.run(order=9)
    def test_search_results(self):
        self.front_page.navigate_to_front_page()
        self.front_page.search_items('printed')
        result = self.results_page.verify_search_results('printed')
        self.status.mark(result, 'Search results test')

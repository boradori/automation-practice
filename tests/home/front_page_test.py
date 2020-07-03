from pages.home.front_page import FrontPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures('class_setup')
class FrontPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.front_page = FrontPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_number_of_items(self):
        self.ts.mark(self.front_page.verify_number_of_items(7), 'Number of items on front page test')

    @pytest.mark.run(order=2)
    def test_popular_items(self):
        self.ts.mark(self.front_page.verify_popular_items('Faded Short Sleeve T-shirts',
                                                          'Printed Chiffon Dress'),
                     'Popular items test')

    @pytest.mark.run(order=3)
    def test_best_sellers_items(self):
        self.ts.mark(self.front_page.verify_best_sellers_items('Printed Chiffon Dress',
                                                               'Printed Dress'),
                     'Best sellers items test')

    @pytest.mark.run(order=4)
    def test_search_dropdown(self):
        self.ts.mark(self.front_page.verify_search_dropdown(), 'Search dropdown test')

    @pytest.mark.run(order=5)
    def test_search_results(self):
        self.ts.mark_final(self.front_page.verify_search_results(), 'Search results test')

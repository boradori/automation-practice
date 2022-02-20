import pytest

from utilities.user import get_username, get_password
import logging


@pytest.mark.all
@pytest.mark.search
class TestSearch:
    @pytest.fixture(autouse=True, scope='session')
    def set_up_and_tear_down_class(self, front_page, header, login_page):
        front_page.navigate()
        header.wait_for_logo_image_to_appear()

        if not header.user_is_signed_in():
            username = get_username()
            password = get_password()

            login_page.navigate()
            login_page.login(username, password)

    @pytest.fixture(autouse=True)
    def set_up_and_tear_down(self, front_page, header, session_driver):
        if session_driver.current_url != 'http://automationpractice.com/index.php':
            front_page.navigate()
            header.wait_for_logo_image_to_appear()

    @pytest.mark.order(9)
    def test_user_can_search_item_via_dropdown_option(self, header, results_page):
        search_term = 'Printed Summer Dress'

        header.search_item_dropdown_by_keyword(search_term, number_of_arrow_downs=3)

        expected_title = 'Printed Chiffon Dress'
        logging.info(f'Verifying that the "Results" page contains title of "{expected_title}".')
        actual_title = results_page.get_title_by_keyword(expected_title)
        logging.info(f'Expected title: {expected_title}')
        logging.info(f'Actual title:   {actual_title}')
        assert expected_title == actual_title

    @pytest.mark.order(10)
    def test_user_can_see_no_results(self, header, results_page):
        search_term = 'askldfjaslkdfjklsaf'

        header.search_item(search_term)

        logging.info('Verifying that there are no results.')
        expected_alert_message = f'No results were found for your search "{search_term}"'
        actual_alert_message = results_page.no_results_heading
        logging.info(f'Expected alert message: {expected_alert_message}')
        logging.info(f'Actual alert message:   {actual_alert_message}')
        assert expected_alert_message == actual_alert_message

    @pytest.mark.order(11)
    def test_user_can_see_results(self, header, results_page):
        search_term = 'printed'

        header.search_item('printed')

        logging.info(f'Verifying that the heading contains "{search_term}".')
        actual_heading = results_page.results_heading
        logging.info(f'Search term:    {search_term}')
        logging.info(f'Actual heading: {actual_heading}')
        assert search_term.upper() in actual_heading

        logging.info('Verifying that the correct items are searched.')
        actual_products = results_page.product_names
        for product in actual_products:
            logging.info(f'Search term:    {search_term}')
            logging.info(f'Actual product: {product}')
            assert search_term.title() in product

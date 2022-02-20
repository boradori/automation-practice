import pytest

from utilities.user import get_username, get_password
import logging


@pytest.mark.all
@pytest.mark.cart
class TestCart:
    @pytest.fixture(autouse=True, scope='session')
    def set_up_and_tear_down_class(self, cart_page, front_page, header, login_page):
        front_page.navigate()
        header.wait_for_logo_image_to_appear()

        if not header.empty:
            cart_page.navigate()
            cart_page.remove_all_items_from_cart()

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

    @pytest.fixture()
    def tear_down(self, cart_page):
        yield
        cart_page.navigate()
        cart_page.remove_all_items_from_cart()

    @pytest.mark.order(12)
    @pytest.mark.usefixtures('tear_down')
    def test_user_can_add_items_to_cart(self, header, results_page):
        search_term = 'printed'

        header.search_item(search_term)
        results_page.wait_for_products_to_appear()
        actual_items = results_page.add_items_to_cart([1, 3, 5])

        logging.info('Verifying that the items are properly displayed.')
        expected_item_names = ['Printed Summer Dress', 'Printed Chiffon Dress', 'Printed Dress']
        actual_item_names = [item['name'] for item in actual_items]
        logging.info(f'Expected item names: {expected_item_names}')
        logging.info(f'Actual item names:   {actual_item_names}')
        assert expected_item_names == actual_item_names

        logging.info(f'Verifying that there are {len(actual_item_names)} items in the cart.')
        expected_quantity = len(actual_item_names)
        actual_quantity = header.quantity
        logging.info(f'fExpected quantity: {expected_quantity}')
        logging.info(f'Actual quantity:    {actual_quantity}')
        assert expected_quantity == actual_quantity

        header.move_to_cart()

        logging.info(f'Verifying that there are {len(actual_item_names)} item tables in the cart.')
        expected_number_of_item_tables = len(actual_item_names)
        actual_number_of_item_tables = len(header.cart_items)
        logging.info(f'Expected number of item tables: {expected_number_of_item_tables}')
        logging.info(f'Actual number of item tables:   {actual_number_of_item_tables}')
        assert expected_number_of_item_tables == actual_number_of_item_tables

    @pytest.mark.order(13)
    def test_user_can_see_items_in_cart_page(self, cart_page, header, results_page):
        search_term = 'printed'

        header.search_item(search_term)
        results_page.wait_for_products_to_appear()
        results_page_cart_items = results_page.add_items_to_cart([1, 3, 5], proceed_to_checkout=True)

        cart_page.wait_for_products_to_appear()

        logging.info('Verifying that the items are properly displayed.')

        cart_page_items = cart_page.get_items_in_cart_page(more_details=False)

        logging.info(f'Results page cart items: {results_page_cart_items}')
        logging.info(f'Cart page items:         {cart_page_items}')
        assert results_page_cart_items == cart_page_items

    @pytest.mark.order(14)
    def test_user_can_remove_item_from_cart(self, cart_page):
        cart_page.navigate()
        cart_page.wait_for_products_to_appear()

        item_to_delete_by_position = 2
        cart_page.remove_item_from_cart_by_product_position(item_to_delete_by_position)

        actual_items = cart_page.get_items_in_cart_page()

        logging.info(f'Verifying that item No. {item_to_delete_by_position} is removed.')
        expected_item_names = ['Printed Summer Dress', 'Printed Dress']
        actual_item_names = [item['name'] for item in actual_items]
        logging.info(f'Expected item names: {expected_item_names}')
        logging.info(f'Actual item names:   {actual_item_names}')
        assert expected_item_names == actual_item_names

    @pytest.mark.order(15)
    def test_user_can_remove_all_items_from_cart(self, cart_page):
        cart_page.navigate()
        cart_page.wait_for_products_to_appear()

        cart_page.remove_all_items_from_cart()

        logging.info('Verifying that the empty cart message is displayed.')
        expected_message = 'Your shopping cart is empty.'
        actual_message = cart_page.empty_cart_message
        logging.info(f'Expected message: {expected_message}')
        logging.info(f'Actual message:   {actual_message}')
        assert expected_message == actual_message

    @pytest.mark.order(16)
    def test_user_can_proceed_to_checkout_page_from_cart_page_with_session(
        self,
        cart_page,
        checkout_page,
        header,
        results_page
    ):
        search_term = 'printed'

        header.search_item(search_term)
        results_page.wait_for_products_to_appear()
        results_page.add_items_to_cart([1, 3, 5], proceed_to_checkout=True)
        cart_page.wait_for_products_to_appear()

        cart_page.click_proceed_to_checkout_button()
        checkout_page.wait_for_current_step_to_have_expected_text('Address')

        logging.info('Verifying that the heading is "ADDRESSES".')
        expected_heading = 'ADDRESSES'
        actual_heading = checkout_page.heading
        logging.info(f'Expected heading: {expected_heading}')
        logging.info(f'Actual heading:   {actual_heading}')
        assert expected_heading == actual_heading

    @pytest.mark.order(17)
    def test_user_can_proceed_to_checkout_page_from_cart_page_without_session(
        self,
        cart_page,
        checkout_page,
        header,
        results_page
    ):
        search_term = 'printed'
        header.logout()

        header.search_item(search_term)
        results_page.wait_for_products_to_appear()
        results_page.add_items_to_cart([1, 3, 5], proceed_to_checkout=True)
        cart_page.wait_for_products_to_appear()

        cart_page.click_proceed_to_checkout_button()
        checkout_page.wait_for_current_step_to_have_expected_text('Sign in')

        logging.info('Verifying that the heading is "AUTHENTICATION".')
        expected_heading = 'AUTHENTICATION'
        actual_heading = checkout_page.heading
        logging.info(f'Expected heading: {expected_heading}')
        logging.info(f'Actual heading:   {actual_heading}')
        assert expected_heading == actual_heading

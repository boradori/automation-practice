import pytest
import logging
import operator

from utilities.user import get_username, get_password
from functools import reduce

results_page_added_items = []


@pytest.mark.all
@pytest.mark.checkout
class TestCheckout:
    @pytest.fixture(autouse=True, scope='session')
    def set_up_and_tear_down_class(self, cart_page, front_page, header, login_page):
        front_page.navigate()
        header.wait_for_logo_image_to_appear()

        if not header.empty:
            cart_page.navigate()
            cart_page.remove_all_items_from_cart()

        if header.user_is_signed_in():
            header.logout()

    @pytest.fixture()
    def set_up_and_tear_down(self, front_page, header, session_driver):
        if session_driver.current_url != 'http://automationpractice.com/index.php':
            front_page.navigate()
            header.wait_for_logo_image_to_appear()

    @pytest.mark.order(18)
    @pytest.mark.usefixtures('set_up_and_tear_down')
    def test_user_can_login_on_checkout_page(self, cart_page, checkout_page, header, results_page):
        search_term = 'printed'

        header.search_item(search_term)
        results_page.wait_for_products_to_appear()
        global results_page_added_items
        results_page_added_items = results_page.add_items_to_cart([1, 3, 5], proceed_to_checkout=True)

        cart_page.wait_for_products_to_appear()

        cart_page.click_proceed_to_checkout_button()

        logging.info(f'Verifying that the heading is "AUTHENTICATION".')
        expected_current_step = 'Sign in'
        checkout_page.wait_for_current_step_to_have_expected_text(expected_current_step)

        logging.info('Verifying that the heading is "AUTHENTICATION".')
        expected_heading = 'AUTHENTICATION'
        actual_heading = checkout_page.heading
        logging.info(f'Expected heading: {expected_heading}')
        logging.info(f'Actual heading:   {actual_heading}')
        assert expected_heading == actual_heading

        username = get_username()
        password = get_password()

        checkout_page.login(username, password)

        expected_current_step = 'Address'
        checkout_page.wait_for_current_step_to_have_expected_text(expected_current_step)

        logging.info('Verifying that the heading is "ADDRESSES".')
        expected_heading = 'ADDRESSES'
        actual_heading = checkout_page.heading
        logging.info(f'Expected heading: {expected_heading}')
        logging.info(f'Actual heading:   {actual_heading}')
        assert expected_heading == actual_heading

    @pytest.mark.order(19)
    def test_user_can_enter_shipping_address(self, checkout_page):
        checkout_page.click_proceed_to_checkout_button()
        checkout_page.wait_for_current_step_to_have_expected_text('Shipping')

        checkout_page.click_proceed_to_checkout_button()

        logging.info('Verifying that proceeding without TOS agreement displays an error message.')
        expected_message = 'You must agree to the terms of service before continuing.'
        actual_message = checkout_page.error_message
        logging.info(f'Expected message: {expected_message}')
        logging.info(f'Actual message:   {actual_message}')
        assert expected_message == actual_message

        checkout_page.click_error_message_close_button()
        checkout_page.toggle_tos_checkbox()

        checkout_page.click_proceed_to_checkout_button()
        checkout_page.wait_for_current_step_to_have_expected_text('Payment')

    @pytest.mark.order(20)
    def test_user_can_enter_payment_information(self, checkout_page):
        logging.info('Verifying that the items are properly displayed.')

        payment_page_items = checkout_page.get_items_in_payment_page(more_details=False)

        logging.info(f'Results page cart items: {results_page_added_items}')
        logging.info(f'Payment page items:      {payment_page_items}')
        assert results_page_added_items == payment_page_items

        checkout_page.click_pay_by_bank_wire()
        checkout_page.wait_for_bank_wire_or_check_payment_heading()

        checkout_page.click_confirm_button()

        logging.info('Verifying that the heading is "ORDER CONFIRMATION" or "ORDER SUMMARY".')
        expected_heading = ['ORDER CONFIRMATION', 'ORDER SUMMARY']
        actual_heading = checkout_page.heading
        logging.info(f'Expected heading: {expected_heading}')
        logging.info(f'Actual heading:   {actual_heading}')
        assert actual_heading in expected_heading

        logging.info('Verifying that the complete message is displayed.')
        expected_message = 'Your order on My Store is complete.'
        actual_message = checkout_page.complete_message
        logging.info(f'Expected message: {expected_message}')
        logging.info(f'Actual message:   {actual_message}')
        assert expected_message == actual_message

        item_prices = [float(item['price']) for item in results_page_added_items]

        logging.info('Verifying that the price is correct.')
        results_page_total_price = reduce(operator.add, item_prices)
        checkout_page_total_price = checkout_page.confirmation_price
        logging.info(f'Results page price:    ${results_page_total_price}')
        logging.info('Shipping fee:          $2.00')
        logging.info(f'Checkout page price:   {checkout_page_total_price}')
        assert results_page_total_price + 2 == float(checkout_page_total_price[1:])

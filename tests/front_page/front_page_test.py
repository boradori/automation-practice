import pytest

from utilities.user import get_username, get_password
import logging


@pytest.mark.all
@pytest.mark.front_page
class TestFrontPage:
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

    @pytest.mark.order(5)
    def test_user_can_see_correct_number_of_items(self, front_page):
        category = 'Popular'

        logging.info(f'Verifying the number of "{category}" items.')
        expected_number = 7
        actual_number = front_page.get_number_of_items_by_category(category)
        logging.info(f'Expected number of {category} items: {expected_number}')
        logging.info(f'Actual number of {category} items:   {actual_number}')
        assert expected_number == actual_number

        category = 'Best'

        front_page.select_category(category)

        logging.info(f'Verifying the number of "{category}" items.')
        expected_number = 7
        actual_number = front_page.get_number_of_items_by_category(category)
        logging.info(f'Expected number of {category} items: {expected_number}')
        logging.info(f'Actual number of {category} items:   {actual_number}')
        assert expected_number == actual_number

    @pytest.mark.order(6)
    def test_user_can_toggle_best_seller_items(self, front_page):
        category = 'Best'
        front_page.select_category(category)

        logging.info('Verifying that the "Best Seller" items are present.')
        expected_items = [
            'Printed Chiffon Dress',
            'Faded Short Sleeve T-shirts',
            'Blouse',
            'Printed Summer Dress',
            'Printed Dress',
            'Printed Summer Dress',
            'Printed Dress'
        ]
        actual_items = front_page.best_seller_product_names
        logging.info(f'Expected items: {expected_items}')
        logging.info(f'Actual items:   {actual_items}')
        assert expected_items == actual_items

    @pytest.mark.order(7)
    def test_user_can_toggle_popular_items(self, front_page):
        category = 'Popular'
        front_page.select_category(category)

        logging.info('Verifying that the "Popular" items are present.')
        expected_items = [
            'Faded Short Sleeve T-shirts',
            'Blouse',
            'Printed Dress',
            'Printed Dress',
            'Printed Summer Dress',
            'Printed Summer Dress',
            'Printed Chiffon Dress'
        ]
        actual_items = front_page.popular_product_names
        logging.info(f'Expected items: {expected_items}')
        logging.info(f'Actual items:   {actual_items}')
        assert expected_items == actual_items

    @pytest.mark.order(8)
    def test_user_can_add_to_cart_without_sign_in(self, cart_page, header, front_page, login_page):
        if header.user_is_signed_in():
            header.logout()

        front_page.navigate()
        header.wait_for_logo_image_to_appear()

        item_name = 'Faded Short Sleeve T-shirts'

        front_page.move_to_item_by_item_name(item_name)
        front_page.add_item_to_cart_by_item_name(item_name)
        front_page.click_proceed_to_checkout_button()

        logging.info('Verifying that the Cart page is displayed.')
        expected_title = 'SHOPPING-CART SUMMARY Your shopping cart contains: 1 Product'
        actual_title = cart_page.title
        logging.info(f'Expected title: {expected_title}')
        logging.info(f'Actual title:   {actual_title}')
        assert expected_title == actual_title

        logging.info('Verifying that the Cart contains 1 product.')
        expected_quantity = 1
        actual_quantity = cart_page.summary_products_quantity
        logging.info(f'Expected quantity: {expected_quantity}')
        logging.info(f'Actual quantity:   {actual_quantity}')
        assert expected_quantity == actual_quantity

        username = get_username()
        password = get_password()

        login_page.navigate()
        login_page.login(username, password)

        logging.info('Verifying that the Cart still contains 1 product.')
        expected_quantity = 1
        actual_quantity = login_page.get_number_of_items_in_cart()
        logging.info(f'Expected quantity: {expected_quantity}')
        logging.info(f'Actual quantity:   {actual_quantity}')
        assert expected_quantity == actual_quantity

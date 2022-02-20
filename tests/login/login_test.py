import logging
import pytest

from utilities.user import get_username, get_password


@pytest.mark.all
@pytest.mark.login
class TestLogin:
    @pytest.fixture(autouse=True)
    def set_up_and_tear_down(self, login_page):
        login_page.navigate()

    @pytest.mark.order(1)
    def test_invalid_login_with_invalid_email_address(self, login_page):
        invalid_username = 'invalidusername'
        password = get_password()

        login_page.login(invalid_username, password)

        logging.info('Verifying that the authentication failure message is displayed.')
        expected_message = 'Invalid email address.'
        actual_message = login_page.authentication_failure_message
        logging.info(f'Expected message: {expected_message}')
        logging.info(f'Actual message:   {actual_message}')
        assert expected_message == actual_message

    @pytest.mark.order(2)
    def test_invalid_login_with_invalid_password(self, login_page):
        username = get_username()
        invalid_password = 'invalidpassword'

        login_page.login(username, invalid_password)

        logging.info('Verifying that the authentication failure message is displayed.')
        expected_message = 'Authentication failed.'
        actual_message = login_page.authentication_failure_message
        logging.info(f'Expected message: {expected_message}')
        logging.info(f'Actual message:   {actual_message}')
        assert expected_message == actual_message

    @pytest.mark.order(3)
    def test_invalid_login_with_invalid_email_address_and_invalid_password(self, login_page):
        invalid_username = 'invalidusername'
        invalid_password = 'invalidpassword'

        login_page.login(invalid_username, invalid_password)

        logging.info('Verifying that the authentication failure message is displayed.')
        expected_message = 'Invalid email address.'
        actual_message = login_page.authentication_failure_message
        logging.info(f'Expected message: {expected_message}')
        logging.info(f'Actual message:   {actual_message}')
        assert expected_message == actual_message

    @pytest.mark.order(4)
    def test_valid_login(self, account_page, header, login_page):
        username = get_username()
        password = get_password()

        login_page.login(username, password)

        logging.info('Verifying that the login is successful.')
        assert header.user_is_signed_in()

        logging.info('Verifying that the "My Account" page is open.')
        assert account_page.heading == 'MY ACCOUNT'

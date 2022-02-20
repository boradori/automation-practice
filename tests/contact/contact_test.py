import pytest
import logging

from utilities.user import get_username


@pytest.mark.all
@pytest.mark.contact
class TestContact:
    @pytest.fixture(autouse=True, scope='session')
    def set_up_and_tear_down_class(self, cart_page, front_page, header, login_page):
        front_page.navigate()
        header.wait_for_logo_image_to_appear()

        if header.user_is_signed_in():
            header.logout()

    @pytest.fixture(autouse=True)
    def set_up_and_tear_down(self, front_page, header, session_driver):
        if session_driver.current_url != 'http://automationpractice.com/index.php':
            front_page.navigate()
            header.wait_for_logo_image_to_appear()

    @pytest.fixture(autouse=True)
    def set_up_and_tear_down(self, front_page, header, session_driver):
        if session_driver.current_url != 'http://automationpractice.com/index.php':
            front_page.navigate()
            header.wait_for_logo_image_to_appear()

    @pytest.mark.order(21)
    def test_user_can_submit_inquiry_via_contact_us_page(self, contact_page, header):
        header.click_contact_us_button()
        contact_page.wait_for_email_field_to_be_clickable()

        username = get_username()

        contact_page.choose_subject('Webmaster')
        contact_page.enter_email_address(username)
        contact_page.enter_order_reference_without_session('REF130')
        contact_page.attach_file()
        contact_page.enter_message('I have a complaint about the order REF130.')
        contact_page.click_submit_inquiry_button()

        logging.info('Verifying that the success message is displayed.')
        expected_message = 'Your message has been successfully sent to our team.'
        actual_message = contact_page.success_message
        logging.info(f'Expected message: {expected_message}')
        logging.info(f'Actual message:   {actual_message}')
        assert expected_message == actual_message

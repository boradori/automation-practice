from pages.front_page import FrontPage
from pages.contact_page import ContactPage
from utilities.status import Status
import unittest
import pytest
import time


@pytest.mark.usefixtures('class_setup')
class ContactTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.front_page = FrontPage(self.driver)
        self.contact_page = ContactPage(self.driver)
        self.status = Status(self.driver)

    @pytest.mark.run(order=18)
    def test_contact_us(self):
        self.front_page.click_contact_us_btn()
        self.contact_page.choose_subject('Webmaster')
        self.contact_page.enter_email('revay29821@zkeiw.com')
        self.contact_page.enter_order_reference('REF130')
        self.contact_page.attach_file()
        self.contact_page.enter_message('I have a complaint about the order REF130.')
        self.contact_page.submit_inquiry()

        result = self.contact_page.verify_success_message()
        self.status.mark(result, 'Contact us page test')

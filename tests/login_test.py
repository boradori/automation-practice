from pages.login_page import LoginPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures('class_setup')
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.login_page = LoginPage(self.driver)
        self.status = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        if self.login_page.verify_login_successful():
            self.login_page.logout()
            self.login_page.navigate_to_login_page()
            self.login_page.login('ry29821@zkeiw.com', 'abcabc')
            self.status.mark(self.login_page.verify_login_failed(), 'Invalid login test')
        else:
            self.login_page.navigate_to_login_page()
            self.login_page.login('ry29821@zkeiw.com', 'abcabc')
            self.status.mark(self.login_page.verify_login_failed(), 'Invalid login test')

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login('revay29821@zkeiw.com', 'RA^@*95QaOav')
        self.status.mark(self.login_page.verify_login_successful(), 'Valid login test')

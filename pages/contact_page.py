from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
import os
from pathlib import Path


class ContactPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _subject_heading = (By.ID, "id_contact")
    _email_field = (By.ID, "email")
    _order_ref_field = (By.ID, "id_order")
    _message_field = (By.ID, "message")
    _attach_file_field = (By.ID, "fileUpload")
    _submit_btn = (By.ID, "submitMessage")
    _success_msg = (By.XPATH, "//p[@class='alert alert-success']")

    def choose_subject(self, subject):
        if subject == 'Customer service':
            subject_heading = self.wait_for_element(self._subject_heading)
            self.send_keys((Keys.DOWN, Keys.RETURN), None, subject_heading)
        elif subject == 'Webmaster':
            subject_heading = self.wait_for_element(self._subject_heading)
            self.send_keys((Keys.DOWN, Keys.DOWN, Keys.RETURN), None, subject_heading)

    def enter_email(self, email):
        email_field = self.wait_for_element(self._email_field)
        self.send_keys(email, None, email_field)

    def enter_order_reference(self, ref):
        order_ref_field = self.wait_for_element(self._order_ref_field)
        self.send_keys(ref, None, order_ref_field)

    def enter_message(self, message):
        message_field = self.wait_for_element(self._message_field)
        self.send_keys(message, None, message_field)

    def attach_file(self):
        attach_file_field = self.wait_for_element(self._attach_file_field)
        self.send_keys(os.getcwd()+"/image.jpg", None, attach_file_field)

    def submit_inquiry(self):
        submit_btn = self.wait_for_element(self._submit_btn)
        self.click_element(None, submit_btn)

    def verify_success_message(self):
        success_msg = self.wait_for_element(self._success_msg)
        return self.is_element_present(None, success_msg)

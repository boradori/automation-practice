from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class CheckoutPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _authentication_heading = (By.XPATH, "//h1[contains(text(),'Authentication')]")

    _address_heading = (By.XPATH, "//h1[contains(text(),'Address')]")
    _delivery_address = (By.XPATH, "//h3[contains(text(),'Your delivery address')]")
    _billing_address = (By.XPATH, "//h3[contains(text(),'Your billing address')]")
    _name_delivery = (By.CSS_SELECTOR, "ul[id='address_delivery'] > li[class*='address_firstname']")
    _name_invoice = (By.CSS_SELECTOR, "ul[id='address_invoice'] > li[class*='address_firstname']")
    _address_delivery = (By.CSS_SELECTOR, "ul[id='address_delivery'] > li[class*='address_address1']")
    _address_invoice = (By.CSS_SELECTOR, "ul[id='address_invoice'] > li[class*='address_address1']")
    _city_delivery = (By.CSS_SELECTOR, "ul[id='address_delivery'] > li[class*='address_city']")
    _city_invoice = (By.CSS_SELECTOR, "ul[id='address_invoice'] > li[class*='address_city']")
    _country_delivery = (By.CSS_SELECTOR, "ul[id='address_delivery'] > li[class*='address_country_name']")
    _country_invoice = (By.CSS_SELECTOR, "ul[id='address_invoice'] > li[class*='address_country_name']")
    _phone_delivery = (By.CSS_SELECTOR, "ul[id='address_delivery'] > li[class*='address_phone_mobile']")
    _phone_invoice = (By.CSS_SELECTOR, "ul[id='address_invoice'] > li[class*='address_phone_mobile']")

    _shipping_heading = (By.XPATH, "//h1[contains(text(),'Shipping')]")
    _comment = (By.CSS_SELECTOR, "textarea[name='message']")
    _proceed_to_checkout_address = (By.CSS_SELECTOR, "button[name='processAddress']")

    _email_field = (By.ID, "email")
    _password_field = (By.ID, "passwd")
    _sign_in_button = (By.ID, "SubmitLogin")

    _tos_checkbox = (By.ID, "cgv")
    _proceed_to_checkout_shipping = (By.CSS_SELECTOR, "button[name='processCarrier']")
    _error_msg = (By.CSS_SELECTOR, "p[class='fancybox-error']")
    _error_msg_close_btn = (By.CSS_SELECTOR, "a[class='fancybox-item fancybox-close']")

    _payment_heading = (By.XPATH, "//h1[text()='Please choose your payment method']")
    _pay_by_bank_wire_btn = (By.CSS_SELECTOR, "a[title='Pay by bank wire']")
    _pay_by_check_btn = (By.CSS_SELECTOR, "a[title='Pay by check.']")

    _order_summary_heading = (By.XPATH, "//h1[contains(text(),'Order summary')]")
    _pay_by_bank_wire_heading = (By.XPATH, "//h3[contains(text(),'Bank-wire payment.')]")
    _pay_by_check_heading = (By.XPATH, "//h3[contains(text(),'Check payment')]")
    _confirm_btn = (By.XPATH, "//span[contains(text(), 'I confirm my order')]")

    _complete_msg = (By.XPATH, "//strong[text()='Your order on My Store is complete.']")

    def verify_authentication(self):
        authentication_heading = self.wait_for_element(self._authentication_heading)
        return self.is_element_present(None, authentication_heading)

    def login(self, username, password):
        sign_in_btn = self.wait_for_element(self._sign_in_button)
        self.send_keys(username, self._email_field)
        self.send_keys(password, self._password_field)
        self.click_element(None, sign_in_btn)

    def verify_address(self):
        return (
            self.is_element_present(self._address_heading) and
            self.get_element(self._name_delivery).text == self.get_element(
                self._name_invoice).text == 'Test Man' and
            self.get_element(self._address_delivery).text == self.get_element(
                self._address_invoice).text == 'somewhere' and
            self.get_element(self._city_delivery).text == self.get_element(
                self._city_invoice).text == 'city, Alabama 12345' and
            self.get_element(self._country_delivery).text == self.get_element(
                self._country_invoice).text == 'United States' and
            self.get_element(self._phone_delivery).text == self.get_element(
                self._phone_invoice).text == '1'
        )

    def add_comment(self, message):
        comment_field = self.wait_for_element(self._comment)
        self.send_keys(message, None, comment_field)

    def click_proceed_to_checkout_address_btn(self):
        self.click_element(self._proceed_to_checkout_address)
        self.wait_for_element(self._shipping_heading)

    def click_proceed_to_checkout_shipping_btn(self):
        self.click_element(self._proceed_to_checkout_shipping)

    def dismiss_error_msg(self):
        self.click_element(self._error_msg_close_btn)
        self.wait_for_element(self._error_msg_close_btn, False)

    def check_tos(self):
        self.click_element(self._tos_checkbox)

    def verify_tos_error_message(self):
        error_msg = self.wait_for_element(self._error_msg)
        return self.is_element_present(None, error_msg)

    def verify_payment_heading(self):
        payment_heading = self.wait_for_element(self._payment_heading)
        return self.is_element_present(None, payment_heading)

    def pay_by_bank_wire(self):
        pay_by_bank_wire_btn = self.wait_for_element(self._pay_by_bank_wire_btn)
        self.click_element(None, pay_by_bank_wire_btn)

    def pay_by_check(self):
        pay_by_check_btn = self.wait_for_element(self._pay_by_check_btn)
        self.click_element(None, pay_by_check_btn)

    def verify_pay_by_bank_wire(self):
        pay_by_bank_wire_heading = self.wait_for_element(self._pay_by_bank_wire_heading)
        return self.is_element_present(None, pay_by_bank_wire_heading)

    def click_confirm_btn(self):
        confirm_btn = self.wait_for_element(self._confirm_btn)
        self.click_element(None, confirm_btn)

    def verify_complete_message(self):
        complete_msg = self.wait_for_element(self._complete_msg)
        return self.is_element_present(None, complete_msg)

import unittest
from tests.login_test import LoginTest
from tests.front_page_test import FrontPageTest
from tests.search_test import SearchTest
from tests.cart_test import CartTest
from tests.checkout_test import CheckoutTest
from tests.contact_test import ContactTest

login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
front_page_test = unittest.TestLoader().loadTestsFromTestCase(FrontPageTest)
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
cart_test = unittest.TestLoader().loadTestsFromTestCase(CartTest)
checkout_test = unittest.TestLoader().loadTestsFromTestCase(CheckoutTest)
contact_test = unittest.TestLoader().loadTestsFromTestCase(ContactTest)

smoke_test = unittest.TestSuite([login_test, front_page_test, search_test, cart_test, checkout_test, contact_test])

unittest.TextTestRunner(verbosity=2).run(smoke_test)

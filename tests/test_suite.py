import unittest
from tests.login_test import LoginTest
from tests.front_page_test import FrontPageTest

login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
front_page_test = unittest.TestLoader().loadTestsFromTestCase(FrontPageTest)

smoke_test = unittest.TestSuite([login_test, front_page_test])

unittest.TextTestRunner(verbosity=2).run(smoke_test)

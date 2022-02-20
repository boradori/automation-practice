import pytest

from pages import (
    AccountPage,
    CartPage,
    CheckoutPage,
    ContactPage,
    FrontPage,
    LoginPage,
    ResultsPage
)


@pytest.fixture(scope='session')
def account_page(session_driver):
    return AccountPage(session_driver)


@pytest.fixture(scope='session')
def cart_page(session_driver):
    return CartPage(session_driver)


@pytest.fixture(scope='session')
def checkout_page(session_driver):
    return CheckoutPage(session_driver)


@pytest.fixture(scope='session')
def contact_page(session_driver):
    return ContactPage(session_driver)


@pytest.fixture(scope='session')
def front_page(session_driver):
    return FrontPage(session_driver)


@pytest.fixture(scope='session')
def login_page(session_driver):
    return LoginPage(session_driver)


@pytest.fixture(scope='session')
def results_page(session_driver):
    return ResultsPage(session_driver)

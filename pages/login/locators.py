from selenium.webdriver.common.by import By

ACCOUNT_LINK = {
    'by': By.CSS_SELECTOR,
    'value': 'a[class="account"] > span'
}

AUTHENTICATION_FAILURE = {
    'by': By.CSS_SELECTOR,
    'value': '.page-heading + .alert-danger li'
}

CONTACT_LINK = {
    'by': By.ID,
    'value': 'contact-link'
}

EMAIL_FIELD = {
    'by': By.ID,
    'value': 'email'
}

LOGIN_LINK = {
    'by': By.XPATH,
    'value': '//a[contains(@title, "Log in to")]'
}

LOGOUT_BUTTON = {
    'by': By.LINK_TEXT,
    'value': 'Sign out'
}

PASSWORD_FIELD = {
    'by': By.ID,
    'value': 'passwd'
}

NUMBER_OF_ITEMS_IN_CART = {
    'by': By.CSS_SELECTOR,
    'value': 'span[class="ajax_cart_quantity"]:nth-child(2)'
}

SIGN_IN_BUTTON = {
    'by': By.ID,
    'value': 'SubmitLogin'
}

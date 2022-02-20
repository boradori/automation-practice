from selenium.webdriver.common.by import By

BEST_SELLER_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'a[class="blockbestsellers"]'
}

BEST_SELLER_LIST_CONTAINER = {
    'by': By.ID,
    'value': 'blockbestsellers'
}

CART = {
    'by': By.CSS_SELECTOR,
    'value': '.shopping_cart > a'
}

CONTACT_US_BUTTON = {
    'by': By.XPATH,
    'value': '//div[@id="contact-link"]/a'
}

EMPTY = {
    'by': By.CSS_SELECTOR,
    'value': '.shopping_cart .ajax_cart_no_product'
}

ITEMS_IN_CART = {
    'by': By.CSS_SELECTOR,
    'value': '.shopping_cart dl[class="products"] > dt'
}

LOGO_IMAGE = {
    'by': By.CSS_SELECTOR,
    'value': 'img[class="logo img-responsive"]'
}

POPULAR_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'a[class="homefeatured"]'
}

POPULAR_PRODUCT_LIST_CONTAINER = {
    'by': By.ID,
    'value': 'homefeatured'
}

QUANTITY = {
    'by': By.CSS_SELECTOR,
    'value': '.shopping_cart .ajax_cart_quantity'
}

SEARCH_BOX = {
    'by': By.ID,
    'value': 'search_query_top'
}

SIGN_IN_OR_USERNAME_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'nav > .header_user_info:nth-child(1) a'
}

SIGN_OUT_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.logout'
}

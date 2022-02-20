from selenium.webdriver.common.by import By

ADD_TO_CART_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'a[title="Add to cart"]'
}

CART_QUANTITY = {
    'by': By.CSS_SELECTOR,
    'value': '.shopping_cart .ajax_cart_quantity'
}

CONTINUE_SHOPPING_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'span[title="Continue shopping"]'
}

ITEM_MODAL = {
    'by': By.XPATH,
    'value': '//div[contains(@style, "display: block") and @id="layer_cart"]'
}

PROCEED_TO_CHECKOUT_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'a[title="Proceed to checkout"]'
}

NO_RESULTS_HEADING = {
    'by': By.CSS_SELECTOR,
    'value': 'p[class="alert alert-warning"]'
}

PRODUCT_NAMES = {
    'by': By.CSS_SELECTOR,
    'value': '.product-container .product-name'
}

PRODUCTS = {
    'by': By.CSS_SELECTOR,
    'value': '.product-container'
}

RESULTS_HEADING = {
    'by': By.CSS_SELECTOR,
    'value': 'h1[class="page-heading  product-listing"]'
}


def add_to_cart_button_by_product_position(position):
    return {
        'by': By.XPATH,
        'value': f'//li[contains(@class, "ajax_block_product")][{position}]//a[@title="Add to cart"]'
    }


def product_by_product_position(position):
    return {
        'by': By.XPATH,
        'value': f'//li[contains(@class, "ajax_block_product")][{position}]'
    }


def result_title_by_keyword(keyword):
    return {
        'by': By.XPATH,
        'value': f'//h1[contains(text(), "{keyword}")]'
    }

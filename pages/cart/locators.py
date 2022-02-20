from selenium.webdriver.common.by import By

EMPTY_CART_MESSAGE = {
    'by': By.XPATH,
    'value': '//p[contains(text(), "Your shopping cart is empty.")]'
}

ITEM_COLOR = {
    'by': By.XPATH,
    'value': '//td[@class="cart_description"]//a[contains(text(), "Color : ")]'
}

ITEM_MODAL = {
    'by': By.XPATH,
    'value': '//div[contains(@style, "display: block") and @id="layer_cart"]'
}

ITEM_NAME = {
    'by': By.CSS_SELECTOR,
    'value': 'p.product-name > a'
}

ITEM_PRICE = {
    'by': By.CSS_SELECTOR,
    'value': 'td[class="cart_total"] span'
}

ITEM_SKU = {
    'by': By.XPATH,
    'value': '//small[contains(text(), "SKU :")]'
}

PROCEED_TO_CHECKOUT_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.cart_navigation a[title="Proceed to checkout"]'
}

PRODUCTS = {
    'by': By.CSS_SELECTOR,
    'value': 'table#cart_summary tbody > tr'
}

SUMMARY_PRODUCTS_QUANTITY = {
    'by': By.ID,
    'value': 'summary_products_quantity'
}

TITLE = {
    'by': By.ID,
    'value': 'cart_title'
}


def delete_button_by_product_position(position):
    return {
        'by': By.CSS_SELECTOR,
        'value': f'table#cart_summary tbody > tr:nth-child({position}) i.icon-trash'
    }

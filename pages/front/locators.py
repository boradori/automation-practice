from selenium.webdriver.common.by import By

ACTIVE_TAB = {
    'by': By.XPATH,
    'value': '//ul[@id="home-page-tabs"]/li[contains(@class, "active")]'
}

ADD_FADED_SHORT_SLEEVE_TO_CART_BUTTON = {
    'by': By.XPATH,
    'value':
        (
            '//div[@class="right-block"]/h5/a[@title="Faded Short Sleeve T-shirts"]'
            '/../../div[@class="button-container"]//span[text() = "Add to cart"]'
        )
}

BEST_SELLER_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'a[class="blockbestsellers"]'
}

BEST_SELLER_LIST_CONTAINER = {
    'by': By.ID,
    'value': 'blockbestsellers'
}

BEST_SELLER_PRODUCT_NAMES = {
    'by': By.CSS_SELECTOR,
    'value': '#blockbestsellers .product-container .right-block .product-name'
}

CART_TITLE = {
    'by': By.ID,
    'value': 'cart_title'
}

FADED_SHORT_SLEEVE = {
    'by': By.XPATH,
    'value': '//div[@class="right-block"]/h5/a[@title="Faded Short Sleeve T-shirts"]'
}

ITEM_MODAL = {
    'by': By.XPATH,
    'value': '//div[contains(@style, "display: block") and @id="layer_cart"]'
}

POPULAR_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'a[class="homefeatured"]'
}

POPULAR_PRODUCT_LIST_CONTAINER = {
    'by': By.ID,
    'value': 'homefeatured'
}

POPULAR_PRODUCT_NAMES = {
    'by': By.CSS_SELECTOR,
    'value': '#homefeatured .product-container .right-block .product-name'
}

PRINTED_TITLE = {
    'by': By.XPATH,
    'value': '//span[contains(text(), "printed")]'
}

PROCEED_TO_CHECKOUT_BUTTON = {
    'by': By.XPATH,
    'value': '//span[contains(text(),"Proceed to checkout")]'
}

SUBMIT_SEARCH_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'button[name="submit_search"]'
}


def add_to_cart_by_item_name(item_name):
    return {
        'by': By.XPATH,
        'value':
            (
                f'//ul[contains(@class, "active")]//div[@class="right-block"]/h5/a[@title="{item_name}"]'
                '/../../div[@class="button-container"]//span[text() = "Add to cart"]'
            )
    }


def item_by_item_name(item_name):
    return {
        'by': By.XPATH,
        'value': f'//ul[contains(@class, "active")]//div[@class="right-block"]/h5/a[@title="{item_name}"]'
    }

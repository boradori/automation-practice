from selenium.webdriver.common.by import By

BILLING_ADDRESS = {
    'by': By.XPATH,
    'value': '//h3[contains(text(), "Your billing address")]'
}

COMMENT = {
    'by': By.CSS_SELECTOR,
    'value': 'textarea[name="message"]'
}

COMPLETE_MESSAGE = {
    'by': By.XPATH,
    'value': '//strong[text()="Your order on My Store is complete."]'
}

CONFIRM_BUTTON = {
    'by': By.XPATH,
    'value': '//span[contains(text(), "I confirm my order")]'
}

CONFIRMATION_PRICE = {
    'by': By.CSS_SELECTOR,
    'value': 'span[class="price"]'
}

CURRENT_STEP = {
    'by': By.CSS_SELECTOR,
    'value': '.step_current span'
}

DELIVERY_ADDRESS = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_delivery"] > li[class*="address_address1"]'
}

DELIVERY_CITY = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_delivery"] > li[class*="address_city"]'
}

DELIVERY_COUNTRY = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_delivery"] > li[class*="address_country_name"]'
}

DELIVERY_NAME = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_delivery"] > li[class*="address_firstname"]'
}

DELIVERY_PHONE = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_delivery"] > li[class*="address_phone_mobile"]'
}

EMAIL_FIELD = {
    'by': By.ID,
    'value': 'email'
}

ERROR_MESSAGE = {
    'by': By.CSS_SELECTOR,
    'value': 'p[class="fancybox-error"]'
}

ERROR_MESSAGE_CLOSE_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'a[class="fancybox-item fancybox-close"]'
}

HEADING = {
    'by': By.CSS_SELECTOR,
    'value': '#center_column .page-heading'
}

INVOICE_ADDRESS = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_invoice"] > li[class*="address_address1"]'
}

INVOICE_CITY = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_invoice"] > li[class*="address_city"]'
}

INVOICE_COUNTRY = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_invoice"] > li[class*="address_country_name"]'
}

INVOICE_NAME = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_invoice"] > li[class*="address_firstname"]'
}

INVOICE_PHONE = {
    'by': By.CSS_SELECTOR,
    'value': 'ul[id="address_invoice"] > li[class*="address_phone_mobile"]'
}

ITEM_COLOR = {
    'by': By.XPATH,
    'value': '//td[@class="cart_description"]//a[contains(text(), "Color : ")]'
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

PAGE_SUBHEADING = {
    'by': By.CSS_SELECTOR,
    'value': '.page-subheading'
}

PAY_BY_BANK_WIRE_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'a[title="Pay by bank wire"]'
}

PAY_BY_CHECK_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'a[title="Pay by check."]'
}

PAY_BY_CHECK_WIRE_HEADING = {
    'by': By.CSS_SELECTOR,
    'value': '//h3[contains(text(), "Check payment")]'
}

PASSWORD_FIELD = {
    'by': By.ID,
    'value': 'passwd'
}

PROCEED_TO_CHECKOUT_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': 'button[name^="process"]'
}

PRODUCTS = {
    'by': By.CSS_SELECTOR,
    'value': 'table#cart_summary tbody > tr'
}

SIGN_IN_BUTTON = {
    'by': By.ID,
    'value': 'SubmitLogin'
}

TOS_CHECKBOX = {
    'by': By.ID,
    'value': 'uniform-cgv'
}

TOS_CHECKBOX_LABEL = {
    'by': By.CSS_SELECTOR,
    'value': 'label[for="cgv"]'
}

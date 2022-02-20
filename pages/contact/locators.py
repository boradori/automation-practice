from selenium.webdriver.common.by import By

ATTACH_FILE_FIELD = {
    'by': By.ID,
    'value': 'fileUpload'
}

EMAIL_FIELD = {
    'by': By.ID,
    'value': 'email'
}

MESSAGE_FIELD = {
    'by': By.ID,
    'value': 'message'
}

ORDER_REF_FIELD = {
    'by': By.ID,
    'value': 'id_order'
}

ORDER_REF_FIELD_SELECTOR = {
    'by': By.CSS_SELECTOR,
    'value': 'select[name="id_order"]'
}

PRODUCT_REF_FIELD_SELECTOR = {
    'by': By.CSS_SELECTOR,
    'value': 'select[name="id_product"]'
}

SUBJECT_HEADING = {
    'by': By.ID,
    'value': 'id_contact'
}

SUBMIT_BUTTON = {
    'by': By.ID,
    'value': 'submitMessage'
}

SUCCESS_MESSAGE = {
    'by': By.CSS_SELECTOR,
    'value': 'p[class="alert alert-success"]'
}

# Automation Practice

## Python Selenium WebDriver Automation on http://automationpractice.com/index.php

Libraries: selenium, pytest, pytest-env, pytest-ordering, pytest-html

Install the libraries by running the following command:
```pip install -r requirements.txt```

- Create an account in the test website if you do not have one.

In order to run the tests, you will need to set `ENV_PASSWORD` and `ENV_USERNAME` environment variables.

```.env
export ENV_PASSWORD=password_goes_here
export ENV_USERNAME=username_goes_here
```

## Execution:
`pytest -m all` runs all test suites.
Choose the browser of your choice from chrome, firefox, and safari.
Chrome is the default so omitting `--browser` works the same as `--browser chrome`.
```
pytest -m all
```
```
pytest -m all --browser chrome
```
If you want to use firefox, you have to specify `--browser firefox` like below.
```
pytest -m all --browser firefox
```

If you need to generate test report in HTML, add --html FILENAME.html

```
pytest -m all --browser chrome --html htmlreports.html
```

## What does this test suite cover?
The test suite covers basic work flows of automationpractice.com.

### Login test - invalid credential and successful login process
```
pytest -m login
```
- **test_invalid_login_with_invalid_email_address**
- **test_invalid_login_with_invalid_password**
- **test_invalid_login_with_invalid_email_address_and_invalid_password**
- **test_valid_login**

### Front page test - items on front page and add to cart without session
```
pytest -m front
```
- **test_user_can_see_correct_number_of_items**
- **test_user_can_toggle_best_seller_items**
- **test_user_can_toggle_popular_items**
- **test_user_can_add_to_cart_without_sign_in**

### Search test - search items and the results
```
pytest -m search
```
- **test_user_can_search_item_via_dropdown_option**
- **test_user_can_see_no_results**
- **test_user_can_see_results**

### Cart test - add and remove items from cart
```
pytest -m cart
```
- **test_user_can_add_items_to_cart**
- **test_user_can_see_items_in_cart_page**
- **test_user_can_remove_item_from_cart**
- **test_user_can_remove_all_items_from_cart**
- **test_user_can_proceed_to_checkout_page_from_cart_page_with_session**
- **test_user_can_proceed_to_checkout_page_from_cart_page_without_session**

### Checkout test - order summary, shipping, and payment method
```
pytest -m checkout
```
- **test_user_can_login_on_checkout_page**
- **test_user_can_enter_shipping_address**
- **test_user_can_enter_payment_information**

# Automation Practice

## Python Selenium WebDriver Automation on http://automationpractice.com/index.php

Libraries: selenium, ddt, pytest, pytest-ordering, pytest-html

Install the libraries by running the following command:
```pip install -r requirements.txt```

Since we are using **pytest-env**, you need to make pytest.ini file in the root of the test suite.

```touch pytest.ini```

In **pytest.ini**, add the following snippet after replacing USERNAME, PASSWORD, INVALID_USERNAME, and INVALID_PASSWORD with your own.

```
[pytest]
env =
    USERNAME=YOUR_VALID_USERNAME_COMES_HERE
    PASSWORD=YOUR_VALID_PASSWORD_COMES_HERE
    INVALID_USERNAME=ANY_INVALID_USERNAME_COMES_HERE
    INVALID_PASSWORD=ANY_INVALID_PASSWORD_COMES_HERE
```

## Execution:
```
py.test -v -s tests/test_suite.py
```

Choose the browser of your choice. Default is Chrome. Choose from chrome, firefox, ie, and safari.
```
py.test -v -s tests/test_suite.py --browser=firefox
```

If you need to generate test report in HTML, add --html=FILENAME.html

```
py.test -v -s tests/test_suite.py --html=htmlreports.html
```

## What does this test suite cover?
The test suite covers basic work flows of automationpractice.com.

### Login test - invalid credential and successful login process
- **Invalid login**
- **Valid login**

### Front page test - items on front page and add to cart without session
- **Number of popular items and best seller items** - both categories display 7 items
- **Popular items** - count and order of popular items
- **Best seller items** - count and order of best seller items
- **Add to cart without** session and preservation of items in cart after login process

### Search test - search items and the results
- **No results** - items that are not in the store shows no results message
- **Search item via dropdown menu** - select a single item and redirects to the item details page
- **Search items** - search results page

### Cart test - add and remove items from cart
- **Add items to cart** - search items and a list of items to the cart
- **Cart items in results page and cart page** - comparison of cart items in both pages
- **Remove an item from cart** - getting rid of **n**th item among cart items
- **Remove all items from cart**

### Checkout test - order summary, shipping, and payment method
- **Order summary and sign in** - order summary page and authentication requirement if signed out
- **Address**
- **Shipping** - check shipping TOS and proceed to payment method page
- **Payment** - select payment method and finish checkout process

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")
CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")

@when ('Click on cart icon')
def click_cart(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(CART_ICON)).click()

@then ('Verify Cart Empty message is shown')
def verify_empty_cart_msg(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(
        By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert actual_text == expected_text, \
        f'Expected {expected_text}, but got {actual_text}'

@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart/')

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    wait = WebDriverWait(context.driver, 10)
    cart_summary = wait.until(EC.visibility_of_element_located(TOTAL_TXT)).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

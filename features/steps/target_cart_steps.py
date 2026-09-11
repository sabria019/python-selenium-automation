from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")

@when ('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(3)

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
    sleep(2)
    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

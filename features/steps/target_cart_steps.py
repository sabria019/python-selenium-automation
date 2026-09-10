from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open main target page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

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

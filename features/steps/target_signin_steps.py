from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open main target page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when ('Click Sign In')
def click_account(context):
    context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()
    sleep(3)

@when('Click Sign In from right side navigation menu')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']").click()
    sleep(3)

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1").text
    assert actual_text == expected_text, \
        f'Expected {expected_text}, but got {actual_text}'
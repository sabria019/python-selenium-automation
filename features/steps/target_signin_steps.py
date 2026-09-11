from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ACCOUNT_SIGN_IN = (By.CSS_SELECTOR, "#account-sign-in")
SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
SIGN_IN_HEADING = (By.CSS_SELECTOR, "h1")

@when ('Click Sign In')
def click_account(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(ACCOUNT_SIGN_IN)).click()

@when('Click Sign In from right side navigation menu')
def click_sign_in(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(*SIGN_IN_HEADING).text
    assert actual_text == expected_text, \
        f'Expected {expected_text}, but got {actual_text}'
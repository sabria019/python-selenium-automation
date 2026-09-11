from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')
    sleep(3)

@then('Verify there are 2 storycards under Unlock added value')
def verify_storycards(context):
    storycards = context.driver.find_elements(
        By.CSS_SELECTOR,
        "[data-test='@web/SlingshotComponents/common/Storycard']")

    expected_count = 2
    actual_count = len(storycards)

    assert actual_count == expected_count, \
        f'Expected {expected_count} storycards, but got {actual_count}'
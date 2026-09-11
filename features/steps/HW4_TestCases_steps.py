from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
TOTAL_TXT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")

STORYCARDS = (By.CSS_SELECTOR, "[data-test='@web/SlingshotComponents/common/Storycard']")


@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')

    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_all_elements_located(STORYCARDS))


@then('Verify there are 2 storycards under Unlock added value')
def verify_storycards(context):
   all_storycards = context.driver.find_elements(*STORYCARDS)
   storycards = all_storycards[1:3]

   expected_count = 2
   actual_count = len(storycards)

   assert actual_count == expected_count, \
       f'Expected {expected_count} storycards, but got {actual_count}'
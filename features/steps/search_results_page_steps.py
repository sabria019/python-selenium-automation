from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


RESULTS_COUNT_TXT = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "['data-test='content-wrapper'] h4")

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN)).click()


@then('Verify search results are shown for {expected_product}')
def verify_search_result_shown(context, expected_product):
    # search_results = context.driver.find_element(*RESULTS_COUNT_TXT).text
    # assert f'{expected_product}' in search_results, f"Expected {expected_product} but got {search_results}"
    context.app.search_results_page.verify_search_results_shown()
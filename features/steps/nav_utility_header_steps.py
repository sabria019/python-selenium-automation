from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
UTILITY_HEADER_WRAPPER = (By.CSS_SELECTOR, "[class*='utilityHeaderWrapper']")
UTILITY_HEADER_LINKS = (By.CSS_SELECTOR, "a[data-test*='@web/GlobalHeader/utilityHeader']")


@when('Search for {product}')
def search_product(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    # sleep(7)
    context.app.header.search_product(product)

@when('Click on cart button')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()

@then('Verify Navigation Utility Header is shown')
def verify_utility_header(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*UTILITY_HEADER_WRAPPER)
    assert len(header_links) == expected_amount, f'Expected 6 links, but got {len(header_links)}'

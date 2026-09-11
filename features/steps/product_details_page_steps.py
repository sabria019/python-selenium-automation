from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open target product A-95162138 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/women-39-s-balloon-long-sleeve-smocked-waist-v-neck-t-shirt-universal-thread-8482-navy-blue-m/-/A-95162138')
    sleep(5)

@then('Verify user can click though colors')
def click_and_verify_colors(context):
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)   # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()
        # for visibility only:
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlush'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Navy Blue or Blush'
        actual_colors.append(selected_color)
        print(actual_colors)

    expected_colors = ['Navy Blue', 'Blush']
    assert expected_colors == actual_colors, f'Expected {expected_colors} colors, did not match {actual_colors}'
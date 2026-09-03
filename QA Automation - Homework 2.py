# 1. Practice with locators:
# Amazon logo — search by XPATH, "//i[@class='a-icon a-icon-logo']"
# Email field - search by ID, "ap_email_login"
# Continue button - search by XPATH, "//input[@class='a-button-input']"
# Conditions of Use link - search by Link Text, "//a[text()='Conditions of Use']"
# Privacy Notice link - search by Link Text, "//a[text()='Privacy Notice']"
# Need help link - search by Link Text, "//a[text()='Need help?']"
# Create a free business account link - search by ID, "ab-registration-ingress-link"


#2. Test Case:
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# Open Target Website
driver.get("https://www.target.com")

driver.find_element(By.ID, "account-sign-in").click()
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

# Verification (Assertion)
expected_result = 'Sign in or create account'
actual_result = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
assert expected_result == actual_result, f'Expected {expected_result}, did not match {actual_result}'

# Verify Login Button
driver.find_element(By.ID, "login")

print('Test case PASSED')
driver.quit()
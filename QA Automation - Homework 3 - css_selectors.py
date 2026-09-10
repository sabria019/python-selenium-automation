# Most Optimal Locators for StackOverflow Create Account page

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Create your account
driver.find_element(By.CSS_SELECTOR, "h1.fs-headline1")

# "By clicking “Sign up”, you agree to our terms of service and acknowledge you have read our privacy policy."
driver.find_element(By.CSS_SELECTOR, "div.js-terms")

# Email entry field
driver.find_element(By.CSS_SELECTOR, "#email")

# Password entry field
driver.find_element(By.CSS_SELECTOR, "#password")

# Show/hide password button
driver.find_element(By.CSS_SELECTOR, "svg.js-show-password")

# Sign up button
driver.find_element(By.CSS_SELECTOR, "#submit-button")

# Sign up with Google button
driver.find_element(By.CSS_SELECTOR, "button[data-provider='google']")

# Sign up with GitHub button
driver.find_element(By.CSS_SELECTOR, "button[data-provider='github']")

# "Get Stack Overflow Internal free for up to 50 users." link
driver.find_element(By.CSS_SELECTOR, "a[href*='/teams']")
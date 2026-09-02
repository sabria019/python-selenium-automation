# 1. Practice with locators:
# Amazon logo — search by XPATH, "//i[@class='a-icon a-icon-logo']"
# Email field - search by ID, "ap_email_login"
# Continue button - search by XPATH, "//input[@class='a-button-input']"
# Conditions of Use link - search by Link Text, "//a[text()='Conditions of Use']"
# Privacy Notice link - search by Link Text, "//a[text()='Privacy Notice']"
# Need help link - search by Link Text, "//a[text()='Need help?']"
# Create a free business account link - search by ID, "ab-registration-ingress-link"


#2. Test Case:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# click account button
account_button = driver.find_element(By.XPATH,"//a[@aria-label='Account']")
account_button.click()
sleep(3)

# click Sign In button from side navigation
sign_in_button = driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
sign_in_button.click()
sleep(10)

# verify Sign In page opened and text is shown
sign_in_text = driver.find_element(By.XPATH, "//button[text()='Sign in or create account']")

# verify Sign In button is present
sign_in_button = driver.find_element(By.XPATH,"//button[text()='Sign in or create account']")

# close browser
driver.quit()


#notes: create an incognito selenium Chrome browser:
#from time import sleep
#from selenium import webdriver
#from selenium.webdriver.common.by import By

#options = webdriver.ChromeOptions()
#options.add_argument("--incognito")

#driver = webdriver.Chrome(options=options)
#driver.maximize_window()
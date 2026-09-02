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
driver.get('https://www.amazon.com/')
sleep(2)

# By ID
element = driver.find_element(By.ID, 'twotabsearchtextbox')
print(element)

# By XPATH
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")

# By XPATH, multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @spellcheck='false']")
driver.find_element(By.XPATH, "//input[@spellcheck='false' and @tabindex='0'] and @type='text']")

# By XPATH, text()
driver.find_element(By.XPATH, "//h2[text()='Designer gifts for Mom']")
driver.find_element(By.XPATH, "//h2[text()='Designer gifts for Mom'] and @class='....'")
driver.find_element(By.XPATH, "//input(contains(@placeholder, 'Search A')]")

driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLinkMobile']")

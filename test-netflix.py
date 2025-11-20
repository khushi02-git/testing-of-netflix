from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
service = Service()
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://www.netflix.com")

time.sleep(3)

expected_title = "Netflix"
if expected_title in driver.title:
    print("TEST 1 PASS: Netflix page loaded successfully")
else:
    print(" TEST 1 FAIL: Netflix title not found")

try:
    signin_btn = driver.find_element(By.LINK_TEXT, "Sign In")
    print("TEST 2 PASS: Sign In button is visible")
except:
    print(" TEST 2 FAIL: Sign In button not found")

try:
    email_box = driver.find_element(By.NAME, "email")
    email_box.send_keys("test@example.com")
    print(" TEST 3 PASS: Email textbox works")
except:
    print(" TEST 3 FAIL: Email textbox not found")

driver.get("https://www.netflix.com/in/browse")
time.sleep(3)

try:
    search_icon = driver.find_element(By.CSS_SELECTOR, "button.searchTab")
    search_icon.click()
    time.sleep(1)

    search_box = driver.find_element(By.CSS_SELECTOR, "input.searchInput")
    search_box.send_keys("Action" + Keys.ENTER)
    print(" TEST 4 PASS: Search feature works")
except:
    print(" TEST 4 FAIL: Search feature not working")

time.sleep(3)

driver.save_screenshot("netflix_test.png")
print("✔ Screenshot saved as netflix_test.png")

driver.quit()

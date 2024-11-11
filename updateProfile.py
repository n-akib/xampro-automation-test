import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Up The driver
driver = webdriver.Firefox()

# Open the URL
driver.get("https://www.xampro.org/dashboard")

# Load data from JSON file
with open('reg_data.json') as f:
    data = json.load(f)

# Access the data
email = data["email"]
password = data["password"]

# Locate form elements and fill them out
email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "password")

# Fill out the login form
email_field.send_keys(email)
password_field.send_keys(password)

# Login
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
driver.execute_script("arguments[0].click();", login_button)

# Wait for login to complete and the dropdown to become interactable
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "basic-nav-dropdown")))

# Locate the dropdown menu and scroll into view
update_menu = driver.find_element(By.XPATH, "//div[@class='profile-view-btn nav-item dropdown']//a[@id='basic-nav-dropdown']")
driver.execute_script("arguments[0].scrollIntoView(true);", update_menu)

# Wait until the dropdown is clickable and then click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "basic-nav-dropdown")))
driver.execute_script("arguments[0].click();", update_menu)

# Wait briefly for the dropdown to open
time.sleep(2)

# Locate and click the "Profile" option
profile_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[8]//a[1]")))
profile_option.click()

name = driver.find_element(By.XPATH, "//input[@id='fullName']")
name.click()
name.send_keys("Rohim Molla" + Keys.TAB)

gender = driver.find_element(By.XPATH, "//label[normalize-space()='Male']")
gender.click()

# Wait for login to complete and the dropdown to become interactable
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "education")))

education_menu = driver.find_element(By.XPATH, "//select[@id='education']")
driver.execute_script("arguments[0].scrollIntoView(true);", education_menu)

# Wait until the dropdown is clickable and then click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "education")))
driver.execute_script("arguments[0].click();", education_menu)

# Wait briefly for the dropdown to open
time.sleep(2)
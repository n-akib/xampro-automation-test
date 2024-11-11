import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Firefox()

# Open the website
driver.get("https://www.xampro.org/signup")
driver.maximize_window()

# Load data from JSON file
with open('reg_data.json') as f:
    data = json.load(f)

# Access the data
f_name = data["fullname"]
email = data["email"]
phone = data["phone"]
password = data["password"]

# Locate form elements and fill them out
fullname = driver.find_element(By.ID, "name")
email_field = driver.find_element(By.ID, "email")
phone_field = driver.find_element(By.ID,"phoneNumber")
password_field = driver.find_element(By.ID, "password")
confirm_pass = driver.find_element(By.ID,"confirmPassword")

# Fill out the registration form
fullname.send_keys(f_name)
email_field.send_keys(email)
phone_field.send_keys(phone)
password_field.send_keys(password)
confirm_pass.send_keys(password)

# Submission
Submit = driver.find_element(By.XPATH, "//div[@class='account-access-submit-button']//img")
driver.execute_script("arguments[0].click();", Submit)

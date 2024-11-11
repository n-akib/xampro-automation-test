import json
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set Up The driver
driver = webdriver.Firefox()

# Open the url
driver.get("https://www.xampro.org/login")

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
Login = driver.find_element(By.XPATH, "//button[@type='submit']")
driver.execute_script("arguments[0].click();", Login)
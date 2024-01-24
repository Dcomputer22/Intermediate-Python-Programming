from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

load_dotenv()
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
phone_number = os.getenv("PHONE_NUMBER")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3766357120&f_AL=true&f_WT"
           "=2&keywords=Data%20Science&origin=JOB_SEARCH_PAGE_LOCATION_SUGGESTION&refresh=true")

# Sign in to my linkedin account
sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_btn.click()
time.sleep(2)

username_input = driver.find_element(By.ID, "username")
username_input.send_keys(username)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

# Opening Job listings
all_listing = driver.find_elements(By.CSS_SELECTOR, ".job-card-container__link")

for listing in all_listing:
    listing.click()
    print("Opening available jobs listings")
    # Easy apply button
    time.sleep(2)
    apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
    apply_button.click()

    # Insert a phone number
    time.sleep(5)
    phone = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
    if phone.text == "":
        phone.send_keys(phone_number)

    # Go to next button
    time.sleep(3)
    next_button = driver.find_element(By.CSS_SELECTOR, "footer button .artdeco-button--primary")
    next_button.click()
    time.sleep(5)

    # Click review button
    review_button = driver.find_element(By.CSS_SELECTOR, "footer button .artdeco-button--primary")
    review_button.click()
    time.sleep(2)


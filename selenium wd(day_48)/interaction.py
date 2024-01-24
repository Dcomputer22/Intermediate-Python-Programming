from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Fatima")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Jimoh")
email = driver.find_element(By.NAME, "email")
email.send_keys("fatima@gmail.com")
sign_up = driver.find_element(By.CLASS_NAME, "btn")
sign_up.click()

# driver.quit()

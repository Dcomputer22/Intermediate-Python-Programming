from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

rental_url = "https://appbrewery.github.io/Zillow-Clone/"
google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeL4YNdwtZFBIgxofaIVIO8htBXFMkHX" \
                  "_c_Ju5W-VYU0sOjVA/viewform?usp=sf_link"

response = requests.get(rental_url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a", "property-card-link")
link_list = [link.get("href") for link in links]

prices = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
price_list = [price.text.split('+')[0].split('/')[0] for price in prices]

addresses = soup.select("a address")
address_list = [address.text.strip().replace('|', '') for address in addresses]

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

for each_form in range(len(price_list)):
    driver.get(google_form_url)
    time.sleep(3)
    address_response = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/'
                                                     'div[1]/div/div[1]/input')
    price_response = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                   '/div/div[1]/div/div[1]/input')
    link_response = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/'
                                                  'div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_response.send_keys(address_list[each_form])
    price_response.send_keys(price_list[each_form])
    link_response.send_keys(link_list[each_form])
    submit_button.click()


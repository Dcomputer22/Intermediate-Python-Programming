from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os
load_dotenv()
USERNAME = "dcomputer023"
PASSWORD = os.getenv("PASSWORD")
SIMILAR_ACCOUNT = "chef_hilda"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(7)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(20)
        save_login_prompt = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(15)
        notification_prompt = self.driver.find_element(By.XPATH, "// button[contains(text(), 'Not Now')]")
        if notification_prompt:
            notification_prompt.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(15)
        scroll_bar_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        scroll_bar = self.driver.find_element(By.XPATH, scroll_bar_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_bar)
            time.sleep(3)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")

        for each_button in all_buttons:
            try:
                each_button.click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel_button.click()


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()

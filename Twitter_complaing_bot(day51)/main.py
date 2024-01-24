from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

CHROME_OPTIONS = webdriver.ChromeOptions()


class InternetSpeedTwitterBot:
    def __init__(self, chrome_options):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        continue_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        continue_button.click()
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        time.sleep(120)
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"down: {self.down + float(download_speed)}")
        print(f"up: {self.up + float(upload_speed)}")

        self.driver.quit()

    def tweet_at_provider(self):
        pass


twitter_bot = InternetSpeedTwitterBot(CHROME_OPTIONS)
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()


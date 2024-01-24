from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
in_five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in prices:
            price_text = price.text
            if price_text != "":
                cost = price_text.split("-")[1].strip().replace(",", "")
                item_prices.append(cost)

        cost_upgrade = {}
        for n in range(len(item_prices)):
            cost_upgrade[item_prices[n]] = items_ids

        money_detail = driver.find_element(By.ID, "money").text
        if "," in money_detail:
            money_detail = money_detail.replace(",", "")
        cookie_count = int(money_detail)
        print(cost_upgrade)

        affordable_upgrades = {}
        for cost, id, in cost_upgrade.items():
            cost = int(cost)
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_affordable_price_upgrades = max(affordable_upgrades)
        print(highest_affordable_price_upgrades)
        to_purchase_id = affordable_upgrades[highest_affordable_price_upgrades]

        driver.find_element(By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5
        if time.time() > in_five_min:
            cookie_per_sec = driver.find_element(by=By.ID, value="cps").text
            print(cookie_per_sec)
            break

# driver.quit()

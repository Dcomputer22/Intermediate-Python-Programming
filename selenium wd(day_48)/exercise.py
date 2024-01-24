from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events_dict = {}
name_list = []
time_list = []

# Using XPATH
events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
events_list = events.text.split('\n')
for event in events_list:
    if events_list.index(event) % 2 == 0:
        time = event
        time_list.append(time)
    else:
        name = event
        name_list.append(name)

for n in range(len(time_list)):
    events_dict[n] = {
        "time": time_list[n],
        "name": name_list[n]
    }

print(events_dict)

# Or through CSS SELECTOR
my_event_dict = {}
event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for i in range(len(event_names)):
    my_event_dict[i] = {
        "time": event_time[i].text,
        "name": event_names[i].text
    }

print(my_event_dict)
driver.quit()

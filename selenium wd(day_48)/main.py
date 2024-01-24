from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.ebay.com/itm/404566989026?hash=item5e321258e2:g:OKQAAOSw7PJlNika&amdata="
           "enc%3AAQAIAAAA0BCvQ5q6lueMyJ2Hpclky%2FwgIMfcEznIQKq5IEw85VD0ydV1KLe4JoPcE20jmStkFW12NW"
           "dYqeArAlnlp%2F5FfNZ94SBSYgSbw0PyWAxO%2BmJBbVPN9BlOXdjAUYyVzz89CrmT77XIgqlDc2hGK8K1es%2Fh8l"
           "1G6XsibXiNV90Acbyj2CoEPX32bqqB8NxzbF7ytT1sEHghGNN03sJchgPL8bFLsVchhDPT4qt04nIH%2FKZQprt6m774"
           "SHtxlWBFUDgC83nwBWfQO0Yiy8kyyzgVMO8%3D%7Ctkp%3ABFBMxsDR4v1i")

price_dollar = driver.find_element(By.CLASS_NAME, "x-price-primary")

print(f"The price is {price_dollar.text}")

driver.quit()
# Selenium can be quit useful for finding elements by name.

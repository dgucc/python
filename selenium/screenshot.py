# selenium + screenshot an entire webpage
# python -m pip install selenium
# https://github.com/mozilla/geckodriver/releases + adapt PATH for geckodriver.exe
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time


options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)

url = "https://scrapingcourse.com/ecommerce/"
png = "example.png"

driver.get(url)
time.sleep(3)

driver.save_full_page_screenshot("img/" + png)


driver.close()

driver.quit()

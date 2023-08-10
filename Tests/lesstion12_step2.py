from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element(By.CSS_SELECTOR, "#num1").text
    b = browser.find_element(By.CSS_SELECTOR, "#num2").text
    x = str(int(a) + int(b))
    search1 = Select(browser.find_element(By.TAG_NAME, "select"))
    search1.select_by_value(x)

    submit1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit1.click()

finally:
    time.sleep(5)
    browser.quit()


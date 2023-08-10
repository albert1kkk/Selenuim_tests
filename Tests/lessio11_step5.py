from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element(By.CSS_SELECTOR, "[src='images/chest.png'")
    chest.get_attribute("valuex")

    x = chest.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    submit1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit1.click()

finally:
    time.sleep(5)
    browser.quit()
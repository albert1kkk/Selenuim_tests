from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc():
    return str(math.log((abs(12*math.sin(int(x))))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".trollface")
    button.click()

    switch = browser.window_handles[1]
    browser.switch_to.window(switch)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = (calc())

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
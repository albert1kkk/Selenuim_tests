from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    time.sleep(2)




    check1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check1.click()

    radio1 = browser.find_element(By.CSS_SELECTOR, ".form-check.form-radio-custom [for]")
    radio1.click()

    submit1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit1.click()

finally:
    time.sleep(5)
    browser.quit()
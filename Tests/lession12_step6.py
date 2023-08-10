from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("test")

    secondname = browser.find_element(By.NAME, "lastname")
    secondname.send_keys("test")

    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("test")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    upload = browser.find_element(By.CSS_SELECTOR, "#file")
    upload.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
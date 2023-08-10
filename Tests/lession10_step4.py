from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys("Albert")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys("Kasimov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
    input3.send_keys("test@test.ru")
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    time.sleep(5)
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()


# def btest_2():
    # link = "http://suninjuly.github.io/registration1.html"
    # browser = webdriver.Chrome()
    # browser.get(link)
    #
    # input1 = browser.find_element(By.CSS_SELECTOR, ".form-control.first")
    # input1.send_keys("Albert")
    # input2 = browser.find_element(By.CSS_SELECTOR, ".form-control.second")
    # input2.send_keys("Kasimov")
    # input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
    # input3.send_keys("test@test.ru")
    # input4 = browser.find_element(By.XPATH, "//div[@class='second_block']//div[@class='form-group first_class']//input")
    # input4.send_keys("test")
    # input5 = browser.find_element(By.XPATH, "//div[@class='second_block']//div[@class='form-group second_class']//input")
    # input5.send_keys("test")
    # submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    # submit.click()
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # welcome_text = welcome_text_elt.text
    # time.sleep(5)
    # assert "Congratulations! You have successfully registered!" == welcome_text


# def btest_3():
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
#     submit.click()
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     welcome_text = welcome_text_elt.text
#     time.sleep(5)
#     assert ""


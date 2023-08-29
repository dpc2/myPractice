from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/training-ground')

input_element = browser.find_element(By.CSS_SELECTOR, \
                                     'input[id="ipt1"]')

input_element.send_keys("Hello World!")

button_element = browser.find_element(By.CSS_SELECTOR, \
                                      'button[id="b1"]')

button_element.click()

while(True):
    pass
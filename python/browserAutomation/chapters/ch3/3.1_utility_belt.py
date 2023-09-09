from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

button = browser.find_element(By.CSS_SELECTOR, "button#b1")
button.click()

alert = Alert(browser)
print(alert.text)

alert.accept()

while(True):
    pass
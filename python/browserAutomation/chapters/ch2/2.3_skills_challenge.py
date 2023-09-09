from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/trial-of-the-stones')



input1_locator = "input[id='r1Input']"
button1_locator = "button#r1Btn"


input1_element = browser.find_element(By.CSS_SELECTOR, input1_locator)
input1_element.send_keys("rock")


button1_element = browser.find_element(By.CSS_SELECTOR, button1_locator)
button1_element.click()

# XPath
# ("//div[@id='passwordBanner']/h4")[0].innerHTML

# CSS Selector
# $$("div[id='passwordBanner'] > h4")


password1_locator = "div[id='passwordBanner'] > h4"


password1_element = browser.find_element(By.CSS_SELECTOR, password1_locator)
password1 = password1_element.text


input2_locator = "input[id='r2Input']"
input2_element = browser.find_element(By.CSS_SELECTOR, input2_locator)
input2_element.send_keys(password1)


button2_locator = "button[id='r2Butn']"
button2_element = browser.find_element(By.CSS_SELECTOR, button2_locator)
button2_element.click()


# Simple approach
# $x("//p[text()='3000']/../span")[0].innerHTML
richest_merchant_locator = "//p[text()='3000']/.. /span"
richest_merchant_element = browser.find_element(By.XPATH, richest_merchant_locator)
richest_merchant = richest_merchant_element.text
print(richest_merchant)


merchant_input_locator = "r3Input"
merchant_input = browser.find_element(By.ID, merchant_input_locator)
merchant_input.send_keys(richest_merchant)


merchant_button_locator = "button#r3Butn"
merchant_button_element = browser.find_element(By.CSS_SELECTOR, merchant_button_locator)
merchant_button_element.click()


check_answer_button_locator = "button[name='checkButn']"
check_answer_element = browser.find_element(By.CSS_SELECTOR, check_answer_button_locator)
check_answer_element.click()


find_answer_locator = "div[id='trialCompleteBanner'] h4"
find_answer_element = browser.find_element(By.CSS_SELECTOR, find_answer_locator)

assert find_answer_element.text == "Trial Complete"

while (True):
    pass

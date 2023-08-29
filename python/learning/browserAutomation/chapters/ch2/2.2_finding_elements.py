from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/training-ground')


# Using CSS selector - $$()
# $$("input[id='ipt2']")
input2_css_locator = "input[id='ipt2']"


# Using XPath - $x()
# $x("//button[@id='b4']")
button4_xpath_locator = "//button[@id='b4']"


# Using XPath to move up and down the hierarchy to find
# the price of Product 1:
# $x("//b[text()='Product 1']/../../p")[0].innerHTML
# This locator is brittle, but it's all we have
#price1_xpath_locator = "//b[text()='Product 1']/../../p[0].innerHTML" 


# Assign elements
input2_element = browser.find_element(By.CSS_SELECTOR, input2_css_locator)
button4_element = browser.find_element(By.XPATH, button4_xpath_locator)


# Manipulate elements
input2_element.send_keys("Test text")
button4_element.click()


#price1_element = browser.find_element(By.XPATH, price1_xpath_locator)
#print(price1_element)

while(True):
    pass

#browser.quit()
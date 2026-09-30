import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1: select one checkbox
a=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
for checkbox in a :
    b=checkbox.get_attribute('id')
    if b=='monday' or b=='tuesday':
        checkbox.click()

time.sleep(2)
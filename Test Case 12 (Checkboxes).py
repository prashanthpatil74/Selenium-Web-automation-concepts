import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1: select one checkbox
driver.find_element(By.XPATH,"//label[normalize-space()='Sunday']").click()

# 2 :select all checkboxes
a=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
for i in a:
    print(i.get_attribute('id'))

#Approach 1
for i in range(len(a)):
    a[i].click()
time.sleep(3)

#Approach 2
for checkbox in a:
    checkbox.click()

# 3: select multiple checkboxes by choice
for checkbox in a :
    b=checkbox.get_attribute('id')
    if b=='monday' or b=='tuesday':
        checkbox.click()

# 4: select last 2 checkboxes
for i in range(len(a)-2,len(a)):
    a[i].click()

# 5: select first 3 checkboxes
for i in range(len(a)):
    if i<3:
        a[i].click()
time.sleep(2)

# 6: unselect all checkboxes
for checkbox in a:
    checkbox.click()
    if checkbox.is_selected():
        checkbox.click()
time.sleep(2)

import time
from turtledemo.paint import switchupdown

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(2)


a=driver.window_handles

# # approach1
parent=a[0]
child=a[1]
print(parent,child)
driver.switch_to.window(parent)
print(driver.title)
driver.switch_to.window(child)
print(driver.title)

# approach2: by loop
for i in a:
    driver.switch_to.window(i)
    print(driver.title)

time.sleep(2)
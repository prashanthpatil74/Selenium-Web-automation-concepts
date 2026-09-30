#test case1:
#open orangehrm demo
#login it
#captures title and verify title

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(2)
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(5)
actual=driver.title
expected="OrangeHRM"
if actual==expected:
    print("login passed")
else:
    print("failed")
driver.close()
#driver.close
#driver.quit

#driver.close
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
driver.close()

#driver.quit
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
driver.quit()


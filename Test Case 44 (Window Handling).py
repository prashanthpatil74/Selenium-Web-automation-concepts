import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Meta Pay").click()
time.sleep(5)
a=driver.window_handles
print(a)
driver.switch_to.window(a[1])
driver.find_element(By.LINK_TEXT,"Creators").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Getting Started").click()
time.sleep(2)
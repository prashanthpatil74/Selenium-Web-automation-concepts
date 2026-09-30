import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(2)
a=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
time.sleep(2)
driver.switch_to.frame(a)
b=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
time.sleep(2)
driver.switch_to.frame(b)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello")
time.sleep(2)
driver.switch_to.parent_frame()
time.sleep(2)


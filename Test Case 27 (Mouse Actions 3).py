#double click:double_click()
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
time.sleep(2)
a=driver.find_element(By.ID,"field1")
a.clear()
a.send_keys("Usha")
time.sleep(3)
button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act=ActionChains(driver)
act.double_click(button).perform()
time.sleep(2)
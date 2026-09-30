# drag and drop
import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
a=driver.find_element(By.XPATH,"//div[@id='box6']")
b=driver.find_element(By.ID,"box106")
c=driver.find_element(By.ID,"box3")
d=driver.find_element(By.ID,"box103")


act=ActionChains(driver)
act.drag_and_drop(a,b).perform()
act.drag_and_drop(c,d).perform()
time.sleep(2)
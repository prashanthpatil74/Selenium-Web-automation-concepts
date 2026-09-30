#mouse hover:move_to_element()
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
Meta=driver.find_element(By.XPATH,"//a[normalize-space()='Meta Pay']")
time.sleep(5)
act=ActionChains(driver)
act.move_to_element(Meta).click().perform()
time.sleep(3)
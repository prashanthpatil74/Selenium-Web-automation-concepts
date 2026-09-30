#Right Click:context_click()v
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)
act.context_click(button).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
driver.switch_to.alert.accept()
time.sleep(5)
#horizonatl drag and drop:slider:drag_and_drop_by_offset
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
minimum=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
maximum=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
print(maximum.location)
print(minimum.location)
act=ActionChains(driver)
act.drag_and_drop_by_offset(minimum,100,0).perform()
# act.drag_and_drop_by_offset(maximum,-25,0).perform()
act.click_and_hold(maximum).move_by_offset(-50, 5).release().perform()
print(maximum.location)
print(minimum.location)
time.sleep(2)

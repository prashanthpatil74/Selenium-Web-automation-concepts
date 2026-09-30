#back()
#forward()
#refresh()
import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.snapdeal.com/")
time.sleep(2)
driver.get("https://www.amazon.in/")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(3)
driver.quit()

#maximize window
import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(10)
print("maximized")

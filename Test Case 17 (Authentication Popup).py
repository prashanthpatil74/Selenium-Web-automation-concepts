#syntax=http://username:password@test.com
import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(5)
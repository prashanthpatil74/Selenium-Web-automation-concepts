import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.save_screenshot("D://Pycharm//Selenium//homepage.png")
time.sleep(2)
driver.quit()
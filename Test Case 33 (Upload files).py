import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
driver.find_element(By.ID,"file-upload").send_keys("D:/Pycharm/Selenium/Test Case 1 (Basic).py")
driver.find_element(By.ID,"file-submit").click()
time.sleep(5)
if driver.page_source.find("File Uploaded!"):
    print("Verified")
else:
    print("File Not Uploaded")
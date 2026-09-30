import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/upload-download.php")
driver.maximize_window()
driver.find_element(By.ID,"downloadButton").click()
time.sleep(3)
if os.path.isfile('D:/sampleFile.jpeg'):
    print("Downloaded")
else:
    print("Not Downloaded")
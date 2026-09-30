#Open link from window to new window
import time

from selenium import webdriver
from selenium.webdriver import  Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
link=Keys.CONTROL+Keys.ENTER
driver.find_element(By.XPATH,"//a[normalize-space()='Register']").send_keys(link)
time.sleep(10)


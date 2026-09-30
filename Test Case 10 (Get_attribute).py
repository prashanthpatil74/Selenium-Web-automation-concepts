import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
a=driver.find_element(By.XPATH,"//input[@id='Email']")
a.clear()
a.send_keys("Prashant@gmail.com")

print("Result of grt attribute:",a.get_attribute("value"))
time.sleep(2)

b=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("Result of get attribute:",b.get_attribute("type"))
time.sleep(2)
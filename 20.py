import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
time.sleep(5)
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
time.sleep(5)
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(5)
actual=driver.title
expected="Dashboard / nopCommerce administration"
if actual==expected:
    print("Login Successful")
else:
    print("Login failed")
driver.close()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

#relative/partial xpath
driver.find_element(By.XPATH,"//*[@id='Email']").clear()
driver.find_element(By.XPATH,"//*[@id='Email']").send_keys("admin@yourstore.com")

#absolute/full xpath
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/div/input").clear()
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/div/input").send_keys("admin")
time.sleep(5)
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(5)

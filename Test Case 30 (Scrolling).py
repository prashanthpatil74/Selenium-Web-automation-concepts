import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# scroll to some position by pixels
driver.execute_script("window.scrollBy(0,3000)","")
a=driver.execute_script("return window.pageYOffset")           #javascipt
time.sleep(2)
print(a)

#element location
b=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",b)
a=driver.execute_script("return window.pageYOffset")
time.sleep(5)



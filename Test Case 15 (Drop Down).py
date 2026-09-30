import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/r.php/")
driver.maximize_window()

a=Select(driver.find_element(By.XPATH,"//select[@id='day']"))

#select one option
a.select_by_visible_text("1")

b= Select(driver.find_element(By.XPATH,"//select[@id='month']"))
b.select_by_value("3")

c=Select(driver.find_element(By.XPATH,"//select[@id='year']"))
c.select_by_index(10)
time.sleep(4)

# #capture all options
c=Select(driver.find_element(By.XPATH,"//select[@id='month']"))
b=c.options
print(len(b))

for i in b:
    print(i.text)

 #select dropdown value without using built in fun
x=Select(driver.find_element(By.XPATH,"//select[@id='year']"))
y=x.options
for i in y:
    if i.text=="2025":
        i.click()
time.sleep(4)
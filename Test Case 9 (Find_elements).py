import time

from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.get("https://demo.nopcommerce.com/")

#find_element:return single element

#find_element: locator matching single web element
a=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
a.send_keys("Laptop")

b=driver.find_element(By.XPATH,"//div[@class='footer-upper']//a")
print(b.text)
time.sleep(2)

#locator throwing no such element exceptions
#driver.find_element(By.LINK_TEXT,"Log in").click()
#driver.find_element(By.LINK_TEXT,"Log ").click()      ....NoSuchElementException

#find_elements:return multiple element

# locator matching multiple web element
elements=driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
print(len(elements))
print(elements[0].text)
for i in elements:
    print(i.text)

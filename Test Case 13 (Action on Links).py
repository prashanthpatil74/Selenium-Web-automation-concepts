from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

#click on link
driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#find number of links in page
b=driver.find_elements(By.TAG_NAME,'a')
c=driver.find_elements(By.XPATH,'//a')
print(len(b))

# #print all link name
for link in b:
    print(link.text)
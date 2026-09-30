#app command: get,title,current_url,page_source
from selenium import webdriver
driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
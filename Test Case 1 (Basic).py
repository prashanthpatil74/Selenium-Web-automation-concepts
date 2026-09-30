#Instagram login
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
a="login"
b=driver.title
if a==b:
    print("Its Matched")
else:
    print("Not matched")
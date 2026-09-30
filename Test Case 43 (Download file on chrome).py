from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By

preferences={"download.default_directory":"D:\Pycharm\Selenium\download"}

driver=webdriver.ChromeOptions()
driver.add_experimental_option("prefs",preferences)
driver=webdriver.Chrome(options=driver)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[normalize-space()='LambdaTest.txt']").click()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='dob']").click()

a=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
a.select_by_visible_text("Nov")

b=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
b.select_by_visible_text("2006")

dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
for ele in dates:
    if ele.text=="25":
        ele.click()
        break

time.sleep(2)
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By



# # Initialize the driver
# driver = webdriver.Chrome()
#
# # Open the website with a date picker
# driver.get('https://example.com/datepicker')
# driver.find_element(By.ID, 'datePicker').click()
#
# # Select the desired month and year, if necessary
# driver.find_element(By.XPATH, '//select[@class="ui-datepicker-month"]/option[text()="October"]').click()
# driver.find_element(By.XPATH, '//select[@class="ui-datepicker-year"]/option[text()="2024"]').click()
#
# # Select the specific day
# driver.find_element(By.XPATH, '//a[text()="22"]').click()
# time.sleep(2)
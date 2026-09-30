import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)

#apporach 1
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("09/11/2000")
time.sleep(2)

#approach 2
year="2023"
month="April"
date="22"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
while True:
    a=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    b=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if a==month and b==year:
        break
    else:
        driver.find_element(By.XPATH,"//a[@title='Prev']").click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text==date:
        ele.click()
        break


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/date-picker")
driver.maximize_window()

# Click the input to open calendar
driver.find_element(By.ID, "datePickerMonthYearInput").click()
time.sleep(1)

# Select Month
driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("July")

# Select Year
driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("2025")

# Select Day (e.g., 28)
days = driver.find_elements(By.CLASS_NAME, "react-datepicker__day")
for day in days:
    if day.text == "28" and "react-datepicker__day--outside-month" not in day.get_attribute("class"):
        day.click()
        break
# day.text == "28": We want to click on the 28th.
#
# "react-datepicker__day--outside-month" is a special class applied to days from previous or next months shown in the calendar.
#
# We ignore those days by checking that this class is not present in the day’s class attribute.

time.sleep(2)
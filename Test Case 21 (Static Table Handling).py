import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

#count number of rows and column
#number of rows=
row=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(row)
col=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(col)

#read  specific row and column data
a=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
print(a)
time.sleep(2)

#read all rows and column data
for r in range(2,row+1):
    for c in range(1,col+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr"+str(r)+"]/td["+str(c)+"]").text
        print(data)
    print()

#read data based on condition(book name whose author is mukesh)
for r in range(2,row+1):
    a=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if a=="Mukesh":
        b=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        c=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(b,c)



from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")  # Replace with actual URL
driver.maximize_window()

# Locate the table
table = driver.find_element(By.ID, "product")

# Get all rows from the table body
rows = table.find_elements(By.XPATH, ".//tbody/tr")

# Loop through rows
for row in rows:
    # Get all columns in current row
    cols = row.find_elements(By.TAG_NAME, "td")
    for col in cols:
        print(col.text, end=" | ")
    print()

driver.quit()

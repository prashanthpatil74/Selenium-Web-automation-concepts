import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
time.sleep(2)

#self
a=driver.find_element(By.XPATH,"//a[contains(text(),'Wipro')]/self::a").text
print(a)

#parent
b=driver.find_element(By.XPATH,"//a[contains(text(),'Wipro')]/parent::td").text
print(b)

#ancestor
c=driver.find_element(By.XPATH,"//a[contains(text(),'Wipro')]/ancestor::tr/child::td").text
print(c)

#ancestor
d=driver.find_element(By.XPATH,"//a[contains(text(),'Wipro')]/ancestor::tr").text
print(d)

#descendant
e=driver.find_elements(By.XPATH,"//a[contains(text(),'Wipro')]/ancestor::tr/descendant::*")
print(len(e))

#following=after self
f=driver.find_elements(By.XPATH,"//a[contains(text(),'Wipro')]/ancestor::tr/following::*")
print(len(f))

#following-sibling
g=driver.find_elements(By.XPATH,"//a[contains(text(),'Wipro')]/ancestor::tr/following-sibling::*")
print(len(g))

#preceding=before self
h=driver.find_elements(By.XPATH,"//a[contains(text(),'Wipro')]/ancestor::tr/preceding::*")
print(len(h))

#preceding-sibling
i=driver.find_elements(By.XPATH,"//a[contains(text(),'Wipro')]/ancestor::tr/preceding-sibling::*")
print(len(i))
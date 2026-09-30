#without getting any ui we can still execute our test case

from selenium import webdriver

ops=webdriver.ChromeOptions()
ops.add_argument('--headless')
driver=webdriver.Chrome(options=ops)
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)

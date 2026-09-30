# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get("https://text-compare.com/")
# driver.maximize_window()
# input1=driver.find_element(By.NAME,"text1")
# input2=driver.find_element(By.NAME,"text2")
#
# input1.send_keys("Welcome")
#
# act=ActionChains(driver)
#
# #select=control+a
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()
# #act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#
# #copy=control+c
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()
#
# #press tab to navigate input2
# act.send_keys(Keys.TAB).perform()
#
# #paste
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# time.sleep(2)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

input_box = driver.find_element(By.ID, "userName")

actions = ActionChains(driver)
actions.click(input_box).send_keys("Usha").perform()
time.sleep(2)
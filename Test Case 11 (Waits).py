# #impicit wait
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # seconds

driver.get("https://www.instagram.com/accounts/login/")
driver.find_element(By.XPATH,"//span[contains(text(),'Home')]").click()

#explicit wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()

# Create WebDriverWait instance
wait = WebDriverWait(driver, 15)

# Wait for the username field and enter value
username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_input.send_keys("usha_nazare45")

# Wait for the password field and enter value
password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_input.send_keys("rushi2404")

# Wait for the login button to become clickable and click
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# Optional: Wait for home page or handle "Save Your Login Info" popup
time.sleep(5)

# Quit driver
driver.quit()


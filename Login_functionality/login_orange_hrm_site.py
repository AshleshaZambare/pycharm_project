from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)
driver = webdriver.Chrome(service= service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)
#enter the valid credentials
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
login_btn = driver.find_element(By.CLASS_NAME, "oxd-button")
login_btn.click()

title = driver.title
if title == "OrangeHRM":
    print("Login passed")
else:
    print("Login failed")

time.sleep(2)
driver.close()
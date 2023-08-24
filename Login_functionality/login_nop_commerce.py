from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)
driver = webdriver.Chrome(service = service_obj)
driver.get("https://admin-demo.nopcommerce.com/login/")
driver.maximize_window()

#provide the credentials
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")

driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

act_title = driver.title
expected_title = "Dashboard / nopCommerce administration"
if act_title ==  expected_title:
    print("Login passed")
else:
    print("Login failed")

time.sleep(2)
driver.close()
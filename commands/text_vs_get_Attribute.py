from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)
driver = webdriver.Chrome(service = service_obj)
driver.get("https://admin-demo.nopcommerce.com/login/")
driver.maximize_window()

#
element = driver.find_element(By.ID, "Email")
print("text:", element.text)
print("get_attribute:", element.get_attribute("value"))
print("get_attribute:", element.get_attribute("Email"))
print("get_attribute:", element.get_attribute("name"))

print()
button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print(button.text)
print(button.get_attribute('value'))
print(button.get_attribute('type'))
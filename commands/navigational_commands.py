from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.get("https://www.snapdeal.com/")
driver.back()
driver.forward()
driver.refresh()
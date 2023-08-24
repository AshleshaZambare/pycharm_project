from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)

driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()

search_btn = driver.find_element(By.XPATH, "//input[@type = 'text']")
search_btn.send_keys("iphone")
search_btn.submit()
driver.close()

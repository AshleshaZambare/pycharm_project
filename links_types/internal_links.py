import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Digital downloads").click()

driver.close()

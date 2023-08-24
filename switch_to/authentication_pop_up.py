import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)
url = "https://the-internet.herokuapp.com/digest_auth"

#syntax for authenticated url is: https://username:password@url

auth_url = "https://admin:admin@the-internet.herokuapp.com/digest_auth"

driver = webdriver.Chrome(service= service_obj)
driver.get(auth_url)
driver.maximize_window()

time.sleep(2)
driver.close()


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://en-gb.facebook.com/login/")
driver.maximize_window()

#1. tagname and id syntax: tagname#value_of_id
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("ashlesha_Z")
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("ashlesha_Z")

#2. tagname and class syntax: tagname.value_of_class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("ashlesha_Z")
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("ashlesha_Z")

#3. tagname and attribute syntax: tagname[attribute=value]
#driver.find_element(By.CSS_SELECTOR,"input[placeholder='Email address or phone number']").send_keys("ashlesha_Z")
#driver.find_element(By.CSS_SELECTOR,"[placeholder='Email address or phone number']").send_keys("ashlesha_Z")

#4. tagname, class and attribute syntax: tagname.value_of_class[attribute='va;ue']
#driver.find_element(By.CSS_SELECTOR,"input.inputtext[placeholder='Email address or phone number']").send_keys("ashlesha_Z")
driver.find_element(By.CSS_SELECTOR,".inputtext[placeholder='Email address or phone number']").send_keys("ashlesha_Z")

time.sleep(2)
driver.close()


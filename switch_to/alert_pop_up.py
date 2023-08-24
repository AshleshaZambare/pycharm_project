import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)
url = "https://the-internet.herokuapp.com/javascript_alerts"

driver = webdriver.Chrome(service= service_obj)
driver.get(url)
driver.maximize_window()

btn = driver.find_element(By.XPATH, "//button[text() = 'Click for JS Prompt']").click()

#to handle alert window methods are
#1. switch_to.alert

#diff alert window will be there
#1. with ok
#2. with ok and cancel
#3. with text box, ok and cancel button

# to click on ok  - alert_obj.accept()
# to click on cancel - alert_obj.dissmiss()
# to enter data in input box - alert_obj.send_keys('input data')

my_alert = driver.switch_to.alert
my_alert.send_keys("welcome")
time.sleep(2)
#my_alert.accept()
my_alert.dismiss()
time.sleep(2)
driver.close()



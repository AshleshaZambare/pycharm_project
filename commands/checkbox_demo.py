import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# select a single checkbox
driver.find_element(By.XPATH, "//input[@type = 'checkbox' and @id = 'monday']").click()

#select multiple checkbox
checkbox_list = driver.find_elements(By.XPATH, "//input[@type = 'checkbox' and contains(@id, 'day')]")
print(len(checkbox_list))
for check_box in checkbox_list:
    check_box.click()
time.sleep(3)

#uclearing all the checkboxes
checkbox_list = driver.find_elements(By.XPATH, "//input[@type = 'checkbox' and contains(@id, 'day')]")
print(len(checkbox_list))
for check_box in checkbox_list:
    if check_box.is_selected():
        check_box.click()

time.sleep(3)
#check a checkbox based on condition(last 2)
checkbox_list = driver.find_elements(By.XPATH, "//input[@type = 'checkbox' and contains(@id, 'day')]")
print(len(checkbox_list))
for i in range(len(checkbox_list)-2, len(checkbox_list)):
    checkbox_list[i].click()

time.sleep(2)
#check first 2 checkbox
checkbox_list = driver.find_elements(By.XPATH, "//input[@type = 'checkbox' and contains(@id, 'day')]")
print(len(checkbox_list))
for i in range(len(checkbox_list)):
    if i<2:
        checkbox_list[i].click()

time.sleep(2)
driver.close()


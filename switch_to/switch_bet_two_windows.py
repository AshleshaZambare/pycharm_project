import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)

driver = webdriver.Chrome(service= service_obj)
driver.get(url)
driver.maximize_window()

print(driver.current_window_handle)

time.sleep(1)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click() #open another browser window

#to switch to specific windows we use windowID and below method
# driver.switch_to.window(WindowID)
# below ways we can get Window ID

print(driver.current_window_handle)  # to print current page window ID
WindowId_lst = driver.window_handles
print(WindowId_lst)

for winid in WindowId_lst:
    driver.switch_to.window(winid)
    win_title = driver.title
    if win_title == "OrangeHRM":
        print("parent window is open")

    if win_title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM":
        print("child window is open")

driver.close()
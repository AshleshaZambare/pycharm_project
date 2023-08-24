from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
print(driver.page_source)



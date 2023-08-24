import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html"
driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)

driver = webdriver.Chrome(service= service_obj)
driver.get(url)
driver.maximize_window()

#to identify frame check in html
#1. frame
#2. iframe
#3. form

#methods used to switch to frames are
#1. switch_to.frame(name of frame)
#2. switch_to.frame(id of frame)
#3. switch_to.frame(webelement)
#4. switch_to.frame(0)

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()  # to got to main page

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

time.sleep(2)
driver.close()
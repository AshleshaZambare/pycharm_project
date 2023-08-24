import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://demo.automationtesting.in/Frames.html"
driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)

driver = webdriver.Chrome(service= service_obj)
driver.get(url)
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click() # to open inner frame

outer_frame = driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)

text_box = driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys("entering a data")

driver.switch_to.default_content()

time.sleep(2)
driver.close()
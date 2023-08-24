import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/iframe"
driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)

driver = webdriver.Chrome(service= service_obj)
driver.get(url)
driver.maximize_window()

# first_frame = driver.find_element(By.XPATH, "//*[@id='content']/div/h3")
# driver.switch_to.frame(first_frame)
# driver.switch_to.default_content()

second_frame = driver.switch_to.frame("mce_0_ifr") # as id of frame is present
textbox = driver.find_element(By.XPATH, "//*[@id='tinymce']")

textbox.clear()  # Clear any existing content
textbox.send_keys('Your data goes here.................')


time.sleep(2)
driver.close()

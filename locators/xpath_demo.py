import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
#absolute path
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys("standard_user")

#relative xpath
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@value = 'Login']").click()

#realtive path options
#1. and operator
#driver.find_element(By.XPATH, "//button[@data-test = 'add-to-cart-sauce-labs-backpack' and @id = 'add-to-cart-sauce-labs-backpack']").click()

#2. or operator
#driver.find_element(By.XPATH, "//button[@data-test = 'add-to-cart-sauce-labs-backpack' or @id = 'add-to-cart-sauce-labs-backpack']").click()

#3. contains()
#driver.find_element(By.XPATH, "//button[contains(@name, 'sauce-labs-backpack')]").click()

#4. start-with
#driver.find_element(By.XPATH, "//button[starts-with(@name, 'add-to-cart')]").click()

#5. text()
driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()

time.sleep(2)
driver.close()

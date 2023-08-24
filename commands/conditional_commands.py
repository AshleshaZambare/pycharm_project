from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

search_box = driver.find_element(By.ID, "small-searchterms")
print(search_box.is_displayed())
print(search_box.is_enabled())

male_rd_btn = driver.find_element(By.ID, "gender-male")
female_rd_btn = driver.find_element(By.ID, "gender-female")
print(male_rd_btn.is_selected())
print(female_rd_btn.is_selected())

male_rd_btn.click()
print(male_rd_btn.is_selected())
print(female_rd_btn.is_selected())

female_rd_btn.click()
print(male_rd_btn.is_selected())
print(female_rd_btn.is_selected())

driver.close()

print()
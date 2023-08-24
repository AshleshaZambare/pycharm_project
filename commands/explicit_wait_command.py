from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)

my_wait = WebDriverWait(driver, 10, ignored_exceptions= [NoSuchElementException, TimeoutException]) # Declaration
driver.get("https://www.amazon.in/")
driver.maximize_window()

search_btn = my_wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'text1']")))
search_btn.send_keys('iphone')
search_btn.submit()
driver.close()
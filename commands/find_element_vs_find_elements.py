from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#1. find_element - returns the single web_elements
#locator matching with single element
web_element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
web_element.send_keys("hello")

#locator matching with multiple elements
web_element = driver.find_element(By.XPATH, "//div[@class= 'footer-upper']//a")
print(web_element.text)
print(".........................................")
#locator with no web element available throws NoSuchElementException
#driver.find_element(By.ID, "Log in").click()  #throws NoSuchElementException

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#2. find_elements - returns the list of web elements
#locator matching with single element
web_elements1 = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
print(web_elements1, type(web_element))
print(len(web_elements1))
for ele in web_elements1:
    print(ele.text)
#doesnt provide text send_keys methods as it is list

print(".........................................")
#locator matching with multiple elements
web_elements2 = driver.find_elements(By.XPATH, "//div[@class= 'footer-upper']//a")
print(web_elements2, type(web_elements2))
print(len(web_elements2))
for ele in web_elements2:
    print(ele.text)

print(".........................................")
#locator with no web element available throws NoSuchElementException
web_elements3 = driver.find_elements(By.ID, "Log in")  #throws NoSuchElementException
print(web_elements3, type(web_elements3))
print(len(web_elements3))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
driver.close()


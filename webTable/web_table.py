import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://testautomationpractice.blogspot.com/"
driver_path = "E:\Ashlesha\Drivers"
service_obj = Service(driver_path)

driver = webdriver.Chrome(service= service_obj)
driver.get(url)
driver.maximize_window()

no_of_rows = len(driver.find_elements(By.XPATH, '//table[@name = "BookTable"]//tr'))
print("no of rows in the table are:", no_of_rows)

no_of_columns = len(driver.find_elements(By.XPATH, '//table[@name = "BookTable"]//tr[1]/th'))
print("total no of columns:", no_of_columns)

#read specific row and column
data = driver.find_element(By.XPATH, '//table[@name = "BookTable"]//tr[5]/td[1]').text
print(data)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#read all data from the table
for r in range(2,(no_of_rows+1)):
    for c in range(1, (no_of_columns+1)):
        data1 = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text
        print(data1, end="              ")
    print()

print(">>>>>>>>>>>>>>>>>>>>>>>>")
#read data based on condition
#list the book name whose author is mukesh
for r in range(2,(no_of_rows+1)):
    author_name = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr[' + str(r) + ']/td[2]').text
    if author_name =="Mukesh":
        bookname = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr[' + str(r) + ']/td[1]').text
        print(bookname)

driver.close()


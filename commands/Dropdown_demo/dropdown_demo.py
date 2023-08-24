import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
my_wait = WebDriverWait(driver, 25)

driver.get("https://formstone.it/components/dropdown/demo/")
driver.maximize_window()

time.sleep(2)
#dropdown_web_Ele = my_wait.until(EC.presence_of_element_located((By.NAME, "country_id")))
dropdown_web_Ele = driver.find_element(By.XPATH, "//select[@id = 'demo_groups']")
dropdown_ele= Select(dropdown_web_Ele)

#dropdown_ele.select_by_visible_text("One")

dropdown_ele.select_by_visible_text("Five")

dropdown_ele.select_by_value("8")

#dropdown_ele.select_by_index(1)
print("no of dropdown options are: ", len(dropdown_ele.options))
for opt in dropdown_ele.options:
    print(opt.text)
    if opt.text == "Three":
        opt.click()
print("no of dropdown options are: ", len((dropdown_ele.options)), type(dropdown_ele.options))

#for practise
# https://testautomationpractice.blogspot.com/
# https://itera-qa.azurewebsites.net/home/automation

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)

driver = webdriver.Chrome(service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(4)
act = ActionChains(driver)
#
# #Enter credentials
# name_box = driver.find_element(By.ID, "name").send_keys("AShlesha Zambare")
# email = driver.find_element(By.ID, "email").send_keys("ashleshazambare@gmail.com")
# phone = driver.find_element(By.ID, "phone").send_keys("9767142849")
# address = driver.find_element(By.ID, "textarea").send_keys("deokar Residency, pune")
#
#
# #radio button
# female_btn = driver.find_element(By.XPATH, "//input[@id= 'female' and @value='female']").click()
# #male_btn = driver.find_element(By.XPATH, "//input[@id= 'male' and @value='male']").click()
#
#
# #Check box
# day_list = driver.find_elements(By.XPATH, "//div[@class = 'form-check form-check-inline']/input[@type = 'checkbox']")
# print(day_list)
# print(len(day_list))
# for day_checkbox in day_list:
#     print(day_checkbox.get_attribute("value"))
#     day = day_checkbox.get_attribute("value")
#     #day_checkbox.click()  # select all checkbox
#     if day == 'monday':
#         if not day_checkbox.is_selected():
#             day_checkbox.click()
#

#dropdown options
# dropdown_ele = driver.find_element(By.ID, "country")
# drop_op = Select(dropdown_ele)
#
# #drop_op.select_by_visible_text("India")
# #drop_op.select_by_value("china")
# drop_op.select_by_index(4)
#
# color_dropdown_ele = driver.find_element(By.ID, "colors")
# color_dropdown_ele = Select(color_dropdown_ele)
# color_dropdown_ele.select_by_value("green")
# time.sleep(3)

#date picker
# date_box = driver.find_element(By.ID, "datepicker").click()
#
# prev_btn = driver.find_element(By.XPATH, "//a[@data-handler = 'prev']")
#
# exp_year = 2024
# exp_month = "June"
# exp_date = 21
# while True:
#     next_btn = driver.find_element(By.XPATH, "//a[@data-handler = 'next']")
#     year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
#     month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
#     print(year, month)
#     if year != exp_year and exp_month != month:
#         print("................in if")
#         time.sleep(3)
#         next_btn.click()
#         print("after click")
#         time.sleep(3)
#     else:
#         break
#
# for row in range(1, 8):
#     for col in range(1, 6):
#         date = driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr[' + str(row) + ']/td[' + str(col) + ']")
#         if date.text == exp_date:
#             print(date.text)
#             date.click()

#WebTable
# no_of_rows = len(driver.find_elements(By.XPATH, '//table[@name="BookTable"]/tbody/tr'))
# no_of_col = len(driver.find_elements(By.XPATH, '//table[@name="BookTable"]/tbody/tr/th'))
#
# for i in range(1, no_of_col):
#     heading = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr[1]/th[' + str(i) + ']').text
#     print(heading, end="            ")
#
# print()
#
# for r in range(2, no_of_rows):
#     for c in range(1,  no_of_col):
#         print(driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text, end = "         ")
#     print()
#
# #pagination Table
# no_of_rows = len(driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr/td"))
# no_of_rows = len(driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr/td"))
#
# #text_box
# field1 = driver.find_element(By.ID, "field1")
# field1.clear()
# field1.send_keys("Welcome!!!")
#
# double_click_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
#

# act.double_click(double_click_btn).perform()
#
#
# #Alerts
# time.sleep(2)
# alert_btn = driver.find_element(By.XPATH, "//button[normalize-space() = 'Alert']").click()
# time.sleep(2)
# my_alert = driver.switch_to.alert
# my_alert_text = my_alert.text
# print(my_alert_text)
# my_alert.accept()
#
# confirm_box_btn = driver.find_element(By.XPATH, "//button[normalize-space() = 'Confirm Box']").click()
# time.sleep(2)
# con_alert = driver.switch_to.alert
# con_alert_text = con_alert.text
# #con_alert.dismiss()
# con_alert.accept()
# print(con_alert_text)
#
# prompt_btn = driver.find_element(By.XPATH, "//button[text()= 'Prompt']").click()
# time.sleep(2)
# prompt_alert = driver.switch_to.alert
# prompt_alert.send_keys("Ashlesha Zambare")
# prompt_alert_text = prompt_alert.text
# prompt_alert.accept()
# print(prompt_alert_text)
#
# time.sleep(5)

driver.implicitly_wait(20)


#switch between windows
# new_window_btn = driver.find_element(By.XPATH, "//button[normalize-space() = 'New Browser Window']").click()
# window_id_lst = driver.window_handles
# driver.switch_to.window(window_id_lst[1])
# act_title = driver.title
# exp_title = "Your Store"
# if act_title == exp_title:
#     print("new window has launched succesfully")
#

#drag and drop
drag_ele = driver.find_element(By.ID, "draggable")
drop_ele = driver.find_element(By.ID, "droppable")
act.drag_and_drop(drag_ele, drop_ele).perform()
time.sleep(5)
if drop_ele.text == "Dropped!":
    print("image is dropped successfully")

#slider
#slider_ele = driver.find_element(By.)
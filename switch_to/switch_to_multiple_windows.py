
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

text_box = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("selenium")
text_box = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys(Keys.RETURN)

parent_div = driver.find_element(By.CLASS_NAME, 'wikipedia-search-results')
time.sleep(5)
search_result_lst = driver.find_elements(By.XPATH, "//div[@id = 'Wikipedia1_wikipedia-search-results']/div[@id = 'wikipedia-search-result-link']/a")

print(search_result_lst, len(search_result_lst))

for link in search_result_lst:
    print(link.text)
    time.sleep(6)
    link.click()



windowid_lst = driver.window_handles
print(windowid_lst)

#close specific window
for windowid in windowid_lst:
    driver.switch_to.window(windowid)
    time.sleep(2)
    if driver.title == "Selenium in biology - Wikipedia":
        driver.close()
time.sleep(5)

#

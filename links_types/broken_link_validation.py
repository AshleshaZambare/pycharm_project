from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

driver_path = "E:\Ashlesha\Drivers"
ser_obj = Service(driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.XPATH, "//a")
#all_links = driver.find_elements(By.TAG_NAME, "a")
print("total no of links:", len(all_links))
# for link in all_links:
#     print(link.text)
#     print(link.get_attribute("href"))

valid_link_cnt = 0
broken_link_cnt = 0
for link in all_links:
    print(">>>>>>>>>>>>", link.text)
    url = link.get_attribute("href")
    try:
        response = requests.head(url)
    except:
        None

    if response.status_code >=400:
        print("broken link: ", url)
        broken_link_cnt +=1
    else:
        valid_link_cnt +=1
        print("valid link:", url)

print("no of broken links are: ", broken_link_cnt)
print("no of valid links are: ", valid_link_cnt)


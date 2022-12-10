import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

file = open("Data.json")
info = json.load(file)
file.close()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(info["url"])
driver.implicitly_wait(5)
def test_Login():
    print("Test Started")
    print("flipkart login assignment")
    print(driver.title)
    driver.find_element(By.XPATH, '//*[@class="_2IX_2- VJZDxU"]').send_keys(info["mail_id"])
    driver.find_element(By.XPATH, '//*[@class="_2IX_2- _3mctLh VJZDxU"]').send_keys(info["password"])
    time.sleep(2)
    driver.get_screenshot_as_file("screenshots/before_login.png")
    driver.find_element(By.XPATH, '//*[@class="_2KpZ6l _2HKlqd _3AWRsL"]').click()
    time.sleep(2)
    driver.get_screenshot_as_file("screenshots/after_login.png")
    driver.close()
    driver.quit()
    print("Test Completed")
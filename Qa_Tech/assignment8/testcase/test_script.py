import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

file = open("Data.json")
info = json.load(file)
file.close()


def test_login():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(info["url"])
    driver.implicitly_wait(5)
    print("Test Started")
    print("G-Mail login & sending mail")
    driver.find_element(By.NAME, 'identifier').send_keys(info["mail-id"])
    driver.find_element(By.XPATH, '//*[text()="Next"]').click()
    driver.find_element(By.NAME, 'Passwd').send_keys(info["password"])
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[text()="Next"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="T-I T-I-KE L3"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="agP aFw"]').send_keys(info["receive-id"])
    driver.find_element(By.XPATH, '//*[@class="aoT"]').send_keys(info["subject"])
    driver.find_element(By.XPATH, '//*[@class="Am Al editable LW-avf tS-tW"]').send_keys(info["text-content"])
    driver.find_element(By.XPATH, '//*[@class="T-I J-J5-Ji aoO v7 T-I-atl L3"]').click()
    time.sleep(2)
    driver.get_screenshot_as_file("screenshots/conformation_pic.png")
    print("message sucessfully sent to ", info["receive-id"], " --mail ids")
    time.sleep(5)
    driver.close()
    driver.quit()
    print("Test Completed")


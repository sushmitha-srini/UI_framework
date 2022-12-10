import json
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

media = []
file = open("data.json")
info = json.load(file)
file.close()

driver = selenium.webdriver.Firefox()
driver.maximize_window()
driver.get(info["Qa_Tech_url"])
driver.implicitly_wait(5)


def test_url():
    print("Test Started")
    a = driver.title
    print("Title Of The Page Is  ", a)
    if a == "QA Automation Tools Trainings and Tutorials | QA Tech Hub":
        print("condition passed & Title matched", a)
    else:
        print("condition failed &  gTitle")
    driver.get(info["Facebook_url"])
    print(driver.title)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    driver.close()
    driver.quit()
    print("Test Completed")

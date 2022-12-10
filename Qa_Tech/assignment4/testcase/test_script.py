from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import selenium
import pytest


list = []
file = open("Data.json")
info = json.load(file)
file.close()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(info["url"])
driver.implicitly_wait(10)


def test_try():
    driver.find_element(By.XPATH, "//*[@type='text']").click()
    driver.find_element(By.XPATH, "//*[@type='text']").send_keys("keychains")
    # driver.find_element(By.XPATH, "//*[@type='submit']").click()
    driver.find_element(By.XPATH, "//*[@class='gh-sb ']").click()
    driver.find_element(By.XPATH, '//option[text() = "Antiques"]').click()
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    print("listed products sucessfully")
    items = driver.find_elements(By.XPATH, "//*[@class='s-item__title']")

    for item in items:
        list.append(item.text)
    print("Total no of items present under this category are ")
    print(list)
    print("Total no of links present in this category ", len(list))
    print("separated the product : ", list[35])
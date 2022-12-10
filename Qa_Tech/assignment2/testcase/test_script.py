import json
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

media = []
file = open("Data.json")
info = json.load(file)
file.close()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(info["link1"])
driver.implicitly_wait(5)
print("Test Started")
def test_checkURL():
    b = driver.current_url
    print(b)
    print(info["link2"])

    if b == info["link2"]:
        print("redirect to same webpage")
    else:
        print("not same web page")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'firstname').send_keys(info["first_name"])
    driver.find_element(By.NAME, 'lastname').send_keys(info["surname"])
    driver.find_element(By.NAME, 'reg_email__').send_keys(info["e-mail"])
    driver.find_element(By.NAME, 'reg_email_confirmation__').send_keys(info["e-mail"])
    driver.find_element(By.NAME, 'reg_passwd__').send_keys(info["password"])
    driver.find_element(By.XPATH, '//option[(text()="1")]').click()
    driver.find_element(By.XPATH, '//option[(text()="May")]').click()
    driver.find_element(By.XPATH, '//option[(text()="2000")]').click()
    driver.find_element(By.XPATH, '//*[@class="_58mt"][1]').click()
    driver.get_screenshot_as_file("screenshots/be_sub.png")
    driver.find_element(By.XPATH, '//*[@class="_6j mvm _6wk _6wl _58mi _3ma _6o _6v"]').click()
    time.sleep(10)
    driver.get_screenshot_as_file("screenshots/af_sub.png")
    time.sleep(3)
    print("page created sucessfully")
    driver.close()
    driver.quit()
    print("Test completed")

#

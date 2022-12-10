import json
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

file = open("Data.json")
info = json.load(file)
file.close()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(info["url"])
driver.implicitly_wait(5)
def test_login():
    print("Test Started")
    print("snapdeal login assignment")
    pointer = ActionChains(driver)
    LOGIN = driver.find_element(By.XPATH, "//*[@class='accountInner']")
    pointer.click_and_hold(LOGIN).perform()
    driver.find_element(By.XPATH, "//*[@class='dropdownAccountNonLoggedIn']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='userName']").send_keys(info["id"])
    driver.find_element(By.XPATH, '//*[@class="btn col-xs-24 btn-large btn-skyblue continueBtn marT20 marB30"]').click()
    driver.find_element(By.NAME, 'j_name').send_keys(info["name"])
    driver.find_element(By.NAME, 'j_number').send_keys(info["no"])
    driver.find_element(By.NAME, 'j_dob').clear()
    time.sleep(2)
    driver.find_element(By.NAME, 'j_dob').send_keys(info["dob"])
    driver.find_element(By.ID, 'j_password').send_keys(info["password"])
    time.sleep(2)
    driver.get_screenshot_as_file("screenshots/before_pic.png")
    driver.find_element(By.ID, 'userSignup').click()
    time.sleep(3)
    driver.get_screenshot_as_file("screenshots/after_pic.png")
    time.sleep(2)
    driver.close()
    driver.quit()
    print("Test Completed")

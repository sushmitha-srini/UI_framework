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
    print("drag & drop assignment7")
    pointer = ActionChains(driver)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@class="demo-frame"]'))
    drag = driver.find_element(By.ID, 'draggable')
    drop = driver.find_element(By.ID, 'droppable')
    before_color = drop.value_of_css_property("color")
    print("before", before_color)
    pointer.drag_and_drop(drag,drop).perform()
    after_color = drop.value_of_css_property("color")
    print("after", after_color)
    time.sleep(4)
    driver.close()
    driver.quit()
    print("Test Completed")

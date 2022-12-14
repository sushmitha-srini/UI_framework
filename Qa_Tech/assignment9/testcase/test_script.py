import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

file = open("Data.json")
info = json.load(file)
file.close()

v = 57
total = []
sub = []
add = []

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


    counts = driver.find_elements(By.XPATH, '//*[@class="ts"]')
    for count in counts:
        total.append(count.text)
    print("Total count of messeages in my INBOX are ", total[2])

    if v > int(total[1]):
        while (v > int(total[1])):
            driver.find_element(By.XPATH, "//*[@class='T-I J-J5-Ji amD T-I-awG T-I-ax7 T-I-Js-Gs L3']").click()
            time.sleep(5)
        val = v - int(total[1])
    else:
        val = v


    names = driver.find_elements(By.XPATH, "//*[@class='bA4']")
    for name in names:
        add.append(name.text)
    while ("" in add):
        add.remove("")
    v1 = add[val]
    subjects = driver.find_elements(By.XPATH, '//*[@class="bog"]')
    for subject in subjects:
        sub.append(subject.text)
    v2 = sub[val]
    print("The ", v, "th message's sender name is ", v1, " & the subject is about ", v2)
    time.sleep(5)
    driver.close()
    driver.quit()
    print("Test Completed")
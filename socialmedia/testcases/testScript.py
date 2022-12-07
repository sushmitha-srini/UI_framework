import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

media = []
file = open("Data.json")
info = json.load(file)
file.close()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(info["url"])
driver.implicitly_wait(5)
print("Test Started")



def test_socialmedia():
    driver.find_element(By.XPATH, "//*[@class='menu']").click()
    time.sleep(2)
    SocialActivity = driver.find_elements(By.XPATH, '//*[@class="social so-slide"]/ul/li/a')
    for link in SocialActivity:
        media.append(str(link.get_attribute("href")))
    print(media)

    for i in range(3):
        try:
            driver.get(media[i])
            driver.switch_to.new_window()
            time.sleep(2)
            screenshotname = "screenshots/" + (media[i].split("/"))[2].split(".")[-2] + ".png"
            print(screenshotname)
            driver.get_screenshot_as_file(screenshotname)
            print("logged in sucessfully for ", media[i])


        except:

            screenshotname = "screenshots/" + (media[i].split("/"))[2].split(".")[-2] + ".png"
            print(screenshotname)
            driver.get_screenshot_as_file(screenshotname)
            print("loading page failed in ", media[i])


def tearDown():
    driver.close()
    driver.quit()
    print("Test Completed")


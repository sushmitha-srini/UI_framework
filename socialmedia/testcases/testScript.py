import unittest
import json
from email._header_value_parser import get_attribute

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

media = []
file = readpayloadjson(["D:/Sushmitha/ASS/socialmedia/testcases/TestData/Data.json"])

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.gcitsolutions.com/gold-coast-it-solutions/")
        self.driver.implicitly_wait(5)
        print("Test Started")

    

    def test_socialmedia(self):
        self.driver.find_element(By.XPATH, "//*[@class='menu']").click()
        time.sleep(2)
        SocialActivity = self.driver.find_elements(By.XPATH, '//*[@class="social so-slide"]/ul/li/a')
        for link in SocialActivity:
            media.append(str(link.get_attribute("href")))
        print(media)
        self.driver.switch_to.new_window()
        time.sleep(2)
        self.driver.get(media[2])
        self.driver.get_screenshot_as_file("screenshots/screenshot_linkdin.png")
        time.sleep(2)
        print("linkedin opened successfully")

        try:
            self.driver.get(media[0])
            self.driver.switch_to.new_window()
            time.sleep(2)

        except:
            self.driver.get_screenshot_as_file("screenshots/screen_facebook.png")
            print("loading page failed in ", media[0])

        try:
            self.driver.get(media[1])
            self.driver.switch_to.new_window()
            time.sleep(2)

        except:
            self.driver.get_screenshot_as_file("screenshots/screenshot_twitter.png")
            print("loading page failed in ", media[1])

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")


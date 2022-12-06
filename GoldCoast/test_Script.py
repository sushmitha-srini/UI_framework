
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


list1 = []
list2 = []
c = []

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.gcitsolutions.com/gold-coast-it-solutions/")
        self.driver.implicitly_wait(5)
        print("Test Started")

    def test_homepage(self):
        global a
        self.driver.find_element(By.XPATH, "//*[@class='menu']").click()
        time.sleep(2)
        menu = self.driver.find_elements(By.XPATH, "//*[@class='menu-list']")
        for variable in menu:
            list1.append(variable.text)
        a= list1[0].split("\n")
        print(a)

    def test_page(self):
        self.driver.find_element(By.XPATH, "//*[@class='menu']").click()
        time.sleep(2)
        menu_list = self.driver.find_elements(By.XPATH, "//*[@class='menu-list']")
        for variable in menu_list:
            list2.append(variable.text)
        b= list2[0].split("\n")
        print(b)
        c = a + b
        print(c)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")
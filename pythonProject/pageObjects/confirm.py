from selenium.webdriver.common.by import By
from utilities.BaseClass import *

class Confirm:

    def __init__(self, driver):
        self.driver = driver

    filterValid = (By.XPATH, '//*[@class="validate filter-input form-control ng-untouched ng-pristine ng-valid"]')
    textIndia = (By.LINK_TEXT, 'India')
    textGermany = (By.LINK_TEXT, 'Germany')
    textSweden = (By.LINK_TEXT, 'Sweden')

    checkbox = (By.XPATH, '//*[@class="checkbox checkbox-primary"]')
    sucessbtn = (By.XPATH, '//*[@class="btn btn-success btn-lg"]')
    notification = (By.XPATH, '//*[@class="alert alert-success alert-dismissible"]')






    def getfilterValid(self):
        return self.driver.find_element(*Confirm.filterValid)

    def linkText1(self):
        return self.driver.find_element(*Confirm.textIndia)

    def linkText2(self):
        return self.driver.find_element(*Confirm.textGermany)

    def linkText3(self):
        return self.driver.find_element(*Confirm.textSweden)

    def getcheckbox(self):
        return self.driver.find_element(*Confirm.checkbox)

    def get_btn(self):
        return self.driver.find_element(*Confirm.sucessbtn)

    def alert(self):
        return self.driver.find_element(*Confirm.notification)








import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass

             ###  if test fails screenshot is taken automatically but it happens only when test fails  ###

class Test_one(BaseClass):
    def test_e2e(self, setup, getData):
        log = self.test_logdemo()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        products = checkoutPage.getproductTitle()

        for product in products:
            productName = product.find_element(By.XPATH, 'div/h4/a').text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, 'div/button').click()
        checkoutPage.clickprimaryButton().click()
        confirmPage = checkoutPage.clicksucessButton()
        confirmPage.getfilterValid().send_keys(getData["suggession"])
        self.verifyLinkText(getData["country"])
        if getData["country"] == "India":
            confirmPage.linkText1().click()
            log.info("1st selected country " +getData["country"])
        elif getData["country"] == "Sweden":
            confirmPage.linkText3().click()
        else:
            confirmPage.linkText2().click()
            log.info("2nd selected country " +getData["country"])
        confirmPage.getcheckbox().click()
        confirmPage.get_btn().click()
        Info = confirmPage.alert().text
        assert 'Success!' in Info
        print(Info)




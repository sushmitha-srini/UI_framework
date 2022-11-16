from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, '//*[@href="/angularpractice/shop"]')

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
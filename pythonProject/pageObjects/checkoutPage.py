from selenium.webdriver.common.by import By

from pageObjects.confirm import Confirm


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    productTitle = (By.XPATH, '//*[@class="card h-100"]')
    primaryButton = (By.XPATH, '//*[@class="nav-link btn btn-primary"]')
    subProduct = (By.XPATH, 'div/h4/a')
    sucessButton = (By.XPATH, '//*[@class="btn btn-success"]')


    def getproductTitle(self):
        return self.driver.find_elements(*CheckoutPage.productTitle)

    def clickprimaryButton(self):
        return self.driver.find_element(*CheckoutPage.primaryButton)

    def clicksucessButton(self):
        self.driver.find_element(*CheckoutPage.sucessButton).click()
        confirmPage = Confirm(self.driver)
        return confirmPage



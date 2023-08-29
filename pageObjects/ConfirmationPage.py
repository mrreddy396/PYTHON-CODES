from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    locationbox = (By.XPATH, "//input[@type='text']")
    countryvalue = (By.LINK_TEXT,"India")
    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    purchase = (By.XPATH, "//input[@type='submit']")
    def getlocationbox(self):
        return self.driver.find_element(*ConfirmationPage.locationbox)

    def getCountryValue(self):
        return self.driver.find_element(*ConfirmationPage.countryvalue)
    def getcheckbox(self):
        return self.driver.find_element(*ConfirmationPage.checkbox)
    def getpurchase(self):
        return self.driver.find_element(*ConfirmationPage.purchase)

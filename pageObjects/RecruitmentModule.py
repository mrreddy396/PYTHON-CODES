
from selenium.webdriver.common.by import By


class RecuritmentPage:
    def __init__(self, driver):
        self.driver = driver

    recurit = (By.XPATH, "//a[contains(@href,'recruitment')]")
    actions = (By.XPATH, "(//button[@type='button'])[5]")
    # reject = (By.XPATH, "(//button[@type='button'])[3]")
    reject = (By.XPATH, "(//button[@type='button']9)")

    def getRecurit(self):
        return self.driver.find_element(*RecuritmentPage.recurit)

    def getActions(self):
        return self.driver.find_element(*RecuritmentPage.actions)

    def getReject(self):
        return self.driver.find_element(*RecuritmentPage.reject)

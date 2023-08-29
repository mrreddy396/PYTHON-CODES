from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutitems = (By.XPATH, "//h4[@class='card-title']/a")
    addtocart = (By.XPATH, "//button[contains(@class,'btn')]")
    finalCheckout=(By.XPATH,"//button[contains(@class,'btn-success')]")

    def getCheckOut(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def getCheckOutItems(self):
        return self.driver.find_elements(*CheckOutPage.checkoutitems)

    def getAddtoCart(self):
        return self.driver.find_elements(*CheckOutPage.addtocart)
    def getFinalCheckOut(self):
        return self.driver.find_element(*CheckOutPage.finalCheckout)

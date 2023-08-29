from selenium.webdriver.common.by import By


class GreenkartConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    individualTotal = (By.XPATH, "//tr/td[5]/p")
    FinalTotal = (By.XPATH, "//span[@class='totAmt']")
    promoCode = (By.XPATH, "//input[@type='text']")
    Apply = (By.XPATH, "//button[@class='promoBtn']")
    TotalAfterDiscount = (By.XPATH, "//span[@class='discountAmt']")
    PlaceOrder=(By.XPATH,"//button[text()='Place Order']")
    Country=(By.XPATH,"//select/option[@value='India']")
    checkbox=(By.XPATH,"//input[@type='checkbox']")
    proceed=(By.XPATH,"//button[text()='Proceed']")


    def getIndividualTotal(self):
        return self.driver.find_elements(*GreenkartConfirmationPage.individualTotal)

    def getFinalTotal(self):
        return self.driver.find_element(*GreenkartConfirmationPage.FinalTotal)

    def getPromoCode(self):
        return self.driver.find_element(*GreenkartConfirmationPage.promoCode)

    def getApply(self):
        return self.driver.find_element(*GreenkartConfirmationPage.Apply)


    def getTotalAfterDiscount(self):
        return self.driver.find_element(*GreenkartConfirmationPage.TotalAfterDiscount)

    def getPlaceOrder(self):
        return self.driver.find_element(*GreenkartConfirmationPage.PlaceOrder)
    def getCountry(self):
        return self.driver.find_element(*GreenkartConfirmationPage.Country)
    def getCheckBox(self):
        return self.driver.find_element(*GreenkartConfirmationPage.checkbox)
    def getProceed(self):
        return self.driver.find_element(*GreenkartConfirmationPage.proceed)

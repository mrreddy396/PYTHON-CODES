from selenium.webdriver.common.by import By


class GreenKart:
    def __init__(self, driver):
        self.driver = driver

    itemnames = (By.XPATH, "//h4[@class='product-name']")
    addtocart = (By.XPATH, "//button[text()='ADD TO CART']")
    bag = (By.XPATH, "//a[@class='cart-icon']")
    checkout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def getItemNames(self):
        return self.driver.find_elements(*GreenKart.itemnames)

    def getAddToCart(self):
        return self.driver.find_elements(*GreenKart.addtocart)

    def getBag(self):
        return self.driver.find_element(*GreenKart.bag)

    def getCheckout(self):
        return self.driver.find_element(*GreenKart.checkout)

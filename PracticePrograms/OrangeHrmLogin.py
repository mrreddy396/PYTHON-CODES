from selenium.webdriver.common.by import By


class OrangeHrmLogin:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@name='username']")
    password = (By.XPATH, "//input[@name='password']")
    submit = (By.XPATH, "//button[@type='submit']")

    def getUserName(self):
        return self.driver.find_element(*OrangeHrmLogin.username)

    def getPassword(self):
        return self.driver.find_element(*OrangeHrmLogin.password)

    def getSubmit(self):
        return self.driver.find_element(*OrangeHrmLogin.submit)

from selenium.webdriver.common.by import By


class OrangeHrmLogin:
    def __init__(self, driver):
        self.driver = driver

    username = (By.CSS_SELECTOR, "input[name='username']")
    password = (By.CSS_SELECTOR, "input[name='password']")
    submit = (By.CSS_SELECTOR, "button[type='submit']")

    def getUserName(self):
        return self.driver.find_element(*OrangeHrmLogin.username)

    def getPassword(self):
        return self.driver.find_element(*OrangeHrmLogin.password)

    def getSubmit(self):
        return self.driver.find_element(*OrangeHrmLogin.submit)

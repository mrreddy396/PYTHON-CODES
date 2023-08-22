from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.XPATH, "//Label [text()='Name']/following-sibling::input")

    email = (By.NAME, "email")

    password = (By.ID, "exampleInputPassword1")

    checkbox = (By.ID, "exampleCheck1")

    gender = (By.ID, "exampleFormControlSelect1")

    status = (By.XPATH, "//input[@value='option1']")

    submit = (By.XPATH, "//input[@type='submit']")

    success = (By.XPATH, "//div[contains(@class,'alert')]")

    date = (By.NAME,"bday")

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def getStatus(self):
        return self.driver.find_element(*HomePage.status)

    def getDate(self):
        return self.driver.find_element(*HomePage.date)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.success)

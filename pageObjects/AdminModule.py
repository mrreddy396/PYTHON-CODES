from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pageObjects.Universal import Universal


class AdminModule:
    def __init__(self, driver):
        self.driver = driver

    admintab = (By.XPATH, "//a[contains(@href,'viewAdminModule')]")
    add = (By.XPATH, "//button[text()=' Add ']")
    UserRole = (By.XPATH, "(//div[@tabindex='0'])[1]")
    UserRoleAdmin = (By.XPATH, "//div[@role='listbox']/div/span[text()='Admin']")
    EmployeeName = (By.XPATH, "//input[contains(@placeholder,'hints')]")
    EmployeeNameInList = (By.XPATH, "(//span[text()='Virat  Kohli'])")
    Status = (By.XPATH, "(//div[@tabindex='0'])[2]")
    error = By.XPATH, "//span[text()='Already exists']"
    StatusOption = (By.XPATH, "(//span[text()='Enabled'])")
    userName = (By.XPATH, "(//input[contains(@class,'oxd-input')])[2]")
    Password = (By.XPATH, "(//input[contains(@class,'oxd-input')])[3]")
    ConfirmPassword = (By.XPATH, "(//input[contains(@class,'oxd-input')])[4]")
    save = (By.XPATH, "//button[@type='submit']")
    records = (By.XPATH, "(//div[@class='oxd-table-cell oxd-padding-cell']/following-sibling::div)[1]")

    def getAdminTab(self):
        return self.driver.find_element(*AdminModule.admintab)

    def getadd(self):
        return self.driver.find_element(*AdminModule.add)

    def getStatus(self):
        return self.driver.find_element(*AdminModule.Status)

    def getUserRole(self):
        return self.driver.find_element(*AdminModule.UserRole)

    def getEmployeeName(self):
        return self.driver.find_element(*AdminModule.EmployeeName)

    def getuserName(self):
        return self.driver.find_element(*AdminModule.userName)

    def getPassword(self):
        return self.driver.find_element(*AdminModule.Password)

    def getConfirmPassword(self):
        return self.driver.find_element(*AdminModule.ConfirmPassword)

    def getUserRoleAdmin(self):
        return self.driver.find_element(*AdminModule.UserRoleAdmin)

    def getEmployeeNameInList(self):
        return self.driver.find_element(*AdminModule.EmployeeNameInList)

    def getStatusOption(self):
        return self.driver.find_element(*AdminModule.StatusOption)

    def getSave(self):
        return self.driver.find_element(*AdminModule.save)

    def getrecords(self):
        return self.driver.find_element(*AdminModule.records)

    def geterror(self):
        return self.driver.find_element(*AdminModule.error)

    def raise_username_exists_exception(self):
        universe = Universal(self.driver)
        log = universe.getLogger()
        try:
            if self.geterror():
                error_message = self.driver.find_element(*self.error).text
                raise Exception(f"Error Occured as: {error_message}")
        except Exception as e:
            print(e)
            log.info(e)
        except NoSuchElementException as b:
            print(f"Selenium's NoSuchElementException {b}")
            log.info(b)

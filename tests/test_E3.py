import logging
import time
import pytest


from pageObjects.AdminModule import AdminModule
from pageObjects.OrangeHrmLogin import OrangeHrmLogin
from pageObjects.Universal import Universal


@pytest.mark.usefixtures("orangehrm")
class TestThree():
    def test_E3(self):
        universe = Universal(self.driver)
        log = universe.getLogger()
        orange = OrangeHrmLogin(self.driver)
        orange.getUserName().send_keys("Admin")
        orange.getPassword().send_keys("admin123")
        orange.getSubmit().click()
        admin = AdminModule(self.driver)
        admin.getAdminTab().click()
        admin.getadd().click()
        admin.getUserRole().click()
        admin.getUserRoleAdmin().click()
        admin.getEmployeeName().send_keys("Virat")
        universe.verifyPresenceOfElement("(//span[text()='Virat  Kohli'])")
        admin.getEmployeeNameInList().click()
        admin.getStatus().click()
        admin.getStatusOption().click()
        admin.getuserName().send_keys("mrreddy1876")
        time.sleep(2)
        admin.raise_username_exists_exception()
        time.sleep(2)
        admin.getPassword().send_keys("Hemanth99488@")
        admin.getConfirmPassword().send_keys("Hemanth99488@")
        admin.getSave().click()
        universe.capture_screenshot("1.png")
        time.sleep(8)
        log.info("User details has been successfully Added")
        admin.getuserName().send_keys("mrreddy1876")
        admin.getSave().click()
        card = admin.getrecords().text
        print(card)
        assert card == 'mrreddy1876'
        log.info("Record found successfully")
        if card == 'mrreddy1876':
            print("Record found successfully")



import time
import logging

import pytest




from pageObjects.OrangeHrmLogin import OrangeHrmLogin
from pageObjects.RecruitmentModule import RecuritmentPage


@pytest.mark.usefixtures("orangehrm")
class TestThree:

    def test_orange(self):
        log = self.getLogger()
        loginPage = OrangeHrmLogin(self.driver)
        time.sleep(2)

        loginPage.getUserName().send_keys("Admin")
        time.sleep(3)
        loginPage.getPassword().send_keys("admin123")
        time.sleep(3)
        loginPage.getSubmit().click()
        time.sleep(3)

        recuritmentPage = RecuritmentPage(self.driver)
        time.sleep(2)
        recuritmentPage.getRecurit().click()
        time.sleep(2)
        recuritmentPage.getActions().click()
        time.sleep(5)


        try:
            recuritmentPage.getReject().click()
        except Exception as e:
            log.error("An error occurred: %s", str(e))



    def getLogger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logFile.log')
        formatter = logging.Formatter("%(asctime)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger











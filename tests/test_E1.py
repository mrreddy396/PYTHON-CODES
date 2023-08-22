import time

import pytest
from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestOne:


    def test1(self):
        homePage = HomePage(self.driver)
        time.sleep(3)
        homePage.getname().send_keys("Hemanth")
        time.sleep(3)
        homePage.getemail().send_keys("Hemanth@gmail.com")
        time.sleep(3)
        homePage.getpassword().send_keys("Hemanth123")
        time.sleep(3)
        homePage.getcheckbox().click()
        time.sleep(3)
        homePage.getGender().click()
        time.sleep(3)
        homePage.getSubmit().click()
        time.sleep(3)
        homePage.getStatus().click()
        time.sleep(3)
        homePage.getDate().send_keys("13-06-2000")
        time.sleep(3)
        msg = homePage.getSuccessMessage().text
        print(msg)


import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmationPage import ConfirmationPage
from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestOne:

    def test1(self):
        log=self.getLogger()
        homePage = HomePage(self.driver)
        log.info("I am in home page")
        # time.sleep(3)
        homePage.getname().send_keys("Hemanth")
        # time.sleep(3)
        homePage.getemail().send_keys("Hemanth@gmail.com")
        # time.sleep(3)
        homePage.getpassword().send_keys("Hemanth123")
        # time.sleep(3)
        homePage.getcheckbox().click()
        # time.sleep(3)
        drop = Select(homePage.getGender())
        drop.select_by_index(1)

        # time.sleep(3)
        homePage.getSubmit().click()
        # time.sleep(3)
        homePage.getStatus().click()
        # time.sleep(3)
        homePage.getDate().send_keys("13-06-2000")
        # time.sleep(3)
        msg = homePage.getSuccessMessage().text
        log.warning("submitted form")
        print(msg)
        homePage.shopItem().click()
        # checkoutpage
        checkoutpage = CheckOutPage(self.driver)
        log.info("I am in Checkout page")
        names = checkoutpage.getCheckOutItems()
        i = -1
        for name in names:
            cardtext = name.text
            i = i + 1
            if cardtext == 'Blackberry':
                checkoutpage.getAddtoCart()[i].click()
        checkoutpage.getCheckOut().click()
        checkoutpage.getFinalCheckOut().click()
        # confirmationpage
        confirmationpage = ConfirmationPage(self.driver)
        log.info("I am in Confirmation page")
        confirmationpage.getlocationbox().send_keys("ind")
        self.verifyPresenceOfElement("India")
        confirmationpage.getCountryValue().click()
        confirmationpage.getcheckbox()
        confirmationpage.getpurchase()
    def verifyPresenceOfElement(self,text):
        element=WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))
    def getLogger(self):
        logger=logging.getLogger(__name__)
        filehandler=logging.FileHandler('logFile.log')
        formatter=logging.Formatter("%(asctime)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
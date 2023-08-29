import time

import pytest

from pageObjects.Greenkart import GreenKart
from pageObjects.GreenkartConfirmationPage import GreenkartConfirmationPage


@pytest.mark.usefixtures("greenkartsetup")
class Testtwo:
    def test_E2(self):
        greenkart = GreenKart(self.driver)
        names = greenkart.getItemNames()
        time.sleep(4)
        i = -1
        for name in names:
            i = i + 1
            cardtext = name.text
            if "Beans" in cardtext:
                time.sleep(4)
                greenkart.getAddToCart()[i].click()

            elif "Brocolli" in cardtext:
                time.sleep(4)
                greenkart.getAddToCart()[i].click()

            elif "Brinjal" in cardtext:
                time.sleep(4)
                greenkart.getAddToCart()[i].click()

            elif "Cucumber" in cardtext:
                time.sleep(4)
                greenkart.getAddToCart()[i].click()
        greenkart.getBag().click()
        time.sleep(4)
        greenkart.getCheckout().click()
        time.sleep(4)
        confirmation = GreenkartConfirmationPage(self.driver)
        sum = 0
        rates = confirmation.getIndividualTotal()
        time.sleep(4)
        for rate in rates:
            sum = sum + int(rate.text)
        print(f"Total amount:'{sum}'")
        a = int(confirmation.getFinalTotal().text)
        print(f"Total Before Discount :'{a}'")
        assert sum == a
        confirmation.getPromoCode().send_keys("rahulshettyacademy")
        confirmation.getApply().click()
        time.sleep(10)
        b = float(confirmation.getTotalAfterDiscount().text)
        time.sleep(4)
        print(f"Total After Discount :'{b}'")
        assert b == a
        time.sleep(3)
        confirmation.getPlaceOrder().click()
        time.sleep(5)
        confirmation.getCountry().click()
        time.sleep(5)
        confirmation.getCheckBox().click()
        time.sleep(5)
        confirmation.getProceed().click()
        time.sleep(5)


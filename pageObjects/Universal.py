import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class Universal:
    def __init__(self, driver):
        self.driver = driver


    def getLogger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logFile.log')
        formatter = logging.Formatter("%(asctime)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
    def verifyPresenceOfElement(self, value):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, value)))
    def capture_screenshot(self, filename):
        self.driver.save_screenshot(filename)
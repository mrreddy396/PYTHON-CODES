
from selenium import webdriver
class ScreenShot:
    driver = webdriver.Chrome()

    def capture_screenshot(filename):
        driver.save(filename)
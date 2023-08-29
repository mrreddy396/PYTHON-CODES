import time

import pytest
from selenium import webdriver

@pytest.mark.usefixtures("setup1")
class test_javaScriptExecutor:
    def test_sample1(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        time.sleep(3)
        driver.execute_script("window.scrollTo(500,500)")
        time.sleep(3)
        driver.get_screenshot_as_file("screenshot.png")

import time

from selenium import webdriver


class Testdemo22:
    def test_dem022(self):
        chrome_options =webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver =webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.execute_script("window.scrollTo(500,500);")
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        driver.get_screenshot_as_file("screenshot1.png")
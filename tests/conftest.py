import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    firefox = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    firefox.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    firefox.maximize_window()
    request.cls.driver = driver
    yield
    print("test ended")
    driver.close()
    firefox.close()


@pytest.fixture()
def greenkartsetup(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    print("test ended")
    driver.close()


@pytest.fixture()
def orangehrm(request):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver = driver
    driver.implicitly_wait(10)


    yield
    print("test ended")
    driver.close()


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://total-qa.com/checkbox-example/")
driver.maximize_window()
time.sleep(3)
#ch = driver.find_element(By.XPATH, "//input[@type='checkbox']")

op2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][3]")
op2.click()
time.sleep(10)
assert op2.is_selected()

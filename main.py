import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
print("current url"+driver.current_url)
print("title"+driver.title)
print("browser name"+driver.name)
txtbox=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
txtbox.send_keys("cars")
time.sleep(3)
gmail=driver.find_element(By.LINK_TEXT,"Gmail")
gmail.click()
time.sleep(3)
signin=driver.find_element(By.LINK_TEXT,"Sign in")
signin.click()
time.sleep(3)
email=driver.find_element(By.XPATH,"//input[@id='identifierId']")
email.send_keys("peram.hemanth99488@gmail.com")
time.sleep(3)



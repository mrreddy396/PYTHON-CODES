import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
time.sleep(1)
radiobutton=driver.find_element(By.XPATH,'//label[contains(@for,"7_1")]')

time.sleep(3)
radiobutton.click()
time.sleep(5)

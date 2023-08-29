import time
#from telnetlib import EC

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(5)
#checkbox=WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//label[contains(@for,"8_5")]')))
checkbox=driver.find_element(By.XPATH,'//label[contains(@for,"8_5")]')

checkbox.click()
time.sleep(3)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
time.sleep(3)
Dropdown=Select(driver.find_element(By.CSS_SELECTOR,"select[id*='RESULT']"))
time.sleep(3)
Dropdown.select_by_index(3)
time.sleep(3)
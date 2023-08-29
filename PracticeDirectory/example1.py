from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (replace 'chromedriver_path' with the actual path)

driver = webdriver.Chrome()

# Open a sample web page with radio buttons and checkboxes
driver.get("https://www.example.com/radios_and_checkboxes")

# Selecting Radio Buttons
radio_button1 = driver.find_element(By.ID, "radio_button1")
radio_button2 = driver.find_element(By.ID, "radio_button2")

radio_button1.click()  # Select the first radio button
time.sleep(1)
radio_button2.click()  # Select the second radio button
time.sleep(1)

# Selecting Checkboxes
checkbox1 = driver.find_element(By.ID, "checkbox1")
checkbox2 = driver.find_element(By.ID, "checkbox2")

checkbox1.click()  # Check the first checkbox
time.sleep(1)
checkbox2.click()  # Check the second checkbox
time.sleep(1)

# Deselecting Checkboxes
checkbox1.click()  # Uncheck the first checkbox
time.sleep(1)
checkbox2.click()  # Uncheck the second checkbox
time.sleep(1)

# Close the browser window
driver.quit()

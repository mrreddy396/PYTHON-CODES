import time

from behave import *
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
use_step_matcher("re")
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
def after_scenario(context, scenario):
    context.driver.quit()


@given("the user is on the registration page")
def step_impl(context):
      driver.get('https://sso.teachable.com/secure/9521/identity/sign_up/email')



@when("they enter (?P<username>.+) and (?P<email>.+)")
def step_impl(context, username, email):
    username_input = driver.find_element(By.XPATH,'//input[@id="user_name"]')
    email_input = driver.find_element(By.XPATH,'//input[@id="user_email"]')
    username_input.send_keys(username)
    email_input.send_keys(email)
    time.sleep(5)



@step("they set the password to (?P<password>.+)")
def step_impl(context, password):
    password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_input.send_keys(password)
@then("the registration should be successful")
def step_impl(context):
    driver.find_element(By.XPATH, '//input[contains(@value,"Sign")]').click()
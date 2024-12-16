from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('The user is on the home page')
def Homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/test/newtours/")


@when('The user entered the valid username and password')
def EnteringCredentials(context):
    context.driver.find_element(By.NAME,"userName").send_keys("mercury")
    context.driver.find_element(By.NAME, "password").send_keys("mercury")
    context.driver.find_element(By.NAME, "submit").click()

# https://www.youtube.com/watch?v=7g032_syktE&list=PLQKDzuA2cCjqfJih_wCRcGTfFhFnvbyR3&index=3
@then('The user should land on the login screen')
def Login_Screen(context):
    name = context.driver.title
    print(name)


@when('The user entered the valid "{username}" and "{password}"')
def Entering_Username_Password(context, username, password):
    context.driver.find_element(By.NAME, "userName").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.NAME, "submit").click()



@when('The user entered the valid the username and password')
def table_data_validation(context):
    for r in context.table:
        context.driver.find_element(By.NAME, "userName").send_keys(r["username"])
        context.driver.find_element(By.NAME, "password").send_keys(r["password"])
        context.driver.find_element(By.NAME, "submit").click()
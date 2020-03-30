import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click delete button')
def step_impl(context):

    page = UserPage(context)
    page.click_delete_btn()
    pass
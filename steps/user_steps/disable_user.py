import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click disable button')
def step_impl(context):

    page = UserPage(context)
    page.click_disable_btn()
    pass
import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click delete role button')
def step_impl(context):

    page = RolePage(context)
    page.click_delete_role_btn()
    pass

@then('user will find "{details}" in Role page')
def step_impl(context, details):

    page = RolePage(context)
    page.find_role_key(details)
    pass
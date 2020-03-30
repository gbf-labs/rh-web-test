import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@when('user in update user page')
def step_impl(context):
    
    page = UserPage(context)
    page.validate_update_user_page()
    pass

@then('user will click edit button')
def step_impl(context):

    page = UserPage(context)
    page.click_edit_btn()
    pass

@then('user will click update user')
def step_impl(context):

    page = UserPage(context)
    page.click_update_user_btn()
    pass

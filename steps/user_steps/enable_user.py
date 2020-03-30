import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will navigates to Users page')
def step_impl(context):

    page = UserPage(context)
    page.visit_user_page()
    pass

@when('user in Users page')
def step_impl(context):

    page = UserPage(context)
    page.validate_user_page()
    pass

@then('user will find "{details}" in Users page')
def step_impl(context, details):

    page = UserPage(context)
    page.find_user_key(details)
    pass

@then('user will click enable button')
def step_impl(context):

    page = UserPage(context)
    page.click_enable_btn()
    pass
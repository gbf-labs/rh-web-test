import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click delete permission button')
def step_impl(context):

    page = PermissionPage(context)
    page.click_delete_permission_btn()
    pass

@then('user will find "{details}"')
def step_impl(context, details):

    page = PermissionPage(context)
    page.find_permission_key(details)
    pass
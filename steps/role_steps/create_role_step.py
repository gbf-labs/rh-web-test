import time
from pages import *
from behave import *
from selenium import webdriver

@then('user will navigates to role page')
def step_impl(context):

    page = RolePage(context)
    page.visit_role_page()
    pass

@when('user in Role page')
def step_impl(context):

    page = RolePage(context)
    page.validate_role_page()
    pass

@then('user will click create role button')
def step_impl(context):

    page = RolePage(context)
    page.click_role_btn()
    pass

@When('user in create role page')
def step_impl(context):

    page = RolePage(context)
    page.validate_create_role_page()
    pass

@then('user type "{role}" in name input textbox role')
def step_impl(context, role):
    
    page = RolePage(context)
    page.enter_role_name(role)
    pass

@then('user type "{details}" in details input textbox role')
def step_impl(context, details):

    page = RolePage(context)
    page.enter_role_detail(details)
    pass

@then('user will select "{permissions}" in "{process}" permissions selection role')
def step_impl(context, permissions, process):

    page = RolePage(context)
    page.select_role_permissions(permissions, process)
    pass

@then('user will save the new role')
def step_impl(context):

    page = RolePage(context)
    page.click_submit_create_role()
    pass
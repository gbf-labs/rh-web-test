import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@when('user in invite user page')
def step_impl(context):
    
    page = UserPage(context)
    page.validate_invite_user_page()
    pass

@then('user will click invite button')
def step_impl(context):

    page = UserPage(context)
    page.click_invite_btn()
    pass
@then('user type "{first_name}" in first name')
def step_impl(context, first_name):
    
    page = UserPage(context)
    page.enter_first_name(first_name)
    pass

@then('user type "{middle_name}" in middle name')
def step_impl(context, middle_name):
    
    page = UserPage(context)
    if middle_name not in ['nothing', 0 , '']:
        page.enter_middle_name(middle_name)
    pass

@then('user type "{last_name}" in last name')
def step_impl(context, last_name):
    
    page = UserPage(context)
    page.enter_last_name(last_name)
    pass

@then('user type "{email}" in email address')
def step_impl(context, email):
    
    page = UserPage(context)
    page.enter_email(email)
    pass

@then('user type "{company}" in autocomplete textbox company')
def step_impl(context, company):
    
    page = UserPage(context)
    page.enter_user_company(company)
    pass

@then('user "{details}" allow VPN access if vessel "{vessel}" exists')
def step_impl(context, details, vessel):
    
    page = UserPage(context)
    page.allow_vpn_access(details, vessel)
    pass

@then('user type "{role}" in autocomplete textbox role')
def step_impl(context, role):
    
    page = UserPage(context)
    page.enter_user_role(role)
    pass

@then('user will click send invite')
def step_impl(context):

    page = UserPage(context)
    page.click_send_invite_btn()
    pass

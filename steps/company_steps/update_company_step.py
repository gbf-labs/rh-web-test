import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click edit company button')
def step_impl(context):

    page = CompanyPage(context)
    page.click_edit_company_btn()
    pass

@When('user in edit company page')
def step_impl(context):
    
    page = CompanyPage(context)
    page.validate_update_company_page()
    pass

@then('user will update the company')
def step_impl(context):

    page = CompanyPage(context)
    page.click_submit_update_company()
    pass
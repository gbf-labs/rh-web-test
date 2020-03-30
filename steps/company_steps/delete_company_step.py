import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click delete company button')
def step_impl(context):

    page = CompanyPage(context)
    page.click_delete_company_btn()
    pass

@then('user will find "{details}" in Company page')
def step_impl(context, details):

    page = CompanyPage(context)
    page.find_company_key(details)
    pass
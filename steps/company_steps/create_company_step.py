import time
from pages import *
from behave import *
from selenium import webdriver

@then('user will navigates to company page')
def step_impl(context):

    page = CompanyPage(context)
    page.visit_company_page()
    pass

@when('user in company page')
def step_impl(context):

    page = CompanyPage(context)
    page.validate_company_page()
    pass

@then('user will click create company button')
def step_impl(context):

    page = CompanyPage(context)
    page.click_company_btn()
    pass

@When('user in create company page')
def step_impl(context):

    page = CompanyPage(context)
    page.validate_create_company_page()
    pass

@then('user type "{company}" in name input textbox company')
def step_impl(context, company):

    page = CompanyPage(context)
    page.enter_company_name(company)
    pass

@then('user type "{vessel}" in vessels autocomplete textbox company')
def step_impl(context, vessel):
    
    page = CompanyPage(context)
    page.enter_company_vessel(vessel)
    pass

@then('user will save the new company')
def step_impl(context):

    page = CompanyPage(context)
    page.click_submit_create_company()
    pass
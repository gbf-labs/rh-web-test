import time
from pages import *
from behave import *
from selenium import webdriver

@then('user will navigates to Sub Category page')
def step_impl(context):

    page = SubCategoryPage(context)
    page.visit_subcategory_page()
    pass

@when('user in Sub Category page')
def step_impl(context):

    page = SubCategoryPage(context)
    page.validate_subcategory_page()
    pass

@then('user will click create subcategory button')
def step_impl(context):

    page = SubCategoryPage(context)
    page.click_subcategory_btn()
    pass

@When('user in create subcategory page')
def step_impl(context):

    page = SubCategoryPage(context)
    page.validate_create_subcategory_page()
    pass

@then('user type "{name}" in subcategory name input textbox')
def step_impl(context, name):
    
    page = SubCategoryPage(context)
    page.enter_subcategory_name(name)
    pass

@then('user select "{options}" in "{process}" options selection')
def step_impl(context, options, process):

    page = SubCategoryPage(context)
    page.select_subcategory_options(options, process)
    pass

@then('user will save the new subcategory')
def step_impl(context):

    page = SubCategoryPage(context)
    page.click_submit_create_subcategory()
    pass
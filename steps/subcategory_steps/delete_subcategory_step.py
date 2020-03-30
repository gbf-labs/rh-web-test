import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click delete subcategory button')
def step_impl(context):

    page = SubCategoryPage(context)
    page.click_delete_subcategory_btn()
    pass

@then('user will find "{details}" in Sub Category page')
def step_impl(context, details):

    page = SubCategoryPage(context)
    page.find_subcategory_key(details)
    pass
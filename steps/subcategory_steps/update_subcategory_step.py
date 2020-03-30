import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click edit subcategory button')
def step_impl(context):

	page = SubCategoryPage(context)
	page.click_edit_subcategory_btn()
	pass

@When('user in edit subcategory page')
def step_impl(context):
	page = SubCategoryPage(context)
	page.validate_update_subcategory_page()
	pass

@then('user will update the subcategory')
def step_impl(context):

	page = SubCategoryPage(context)
	page.click_submit_update_subcategory()
	pass
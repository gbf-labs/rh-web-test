import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click edit role button')
def step_impl(context):

	page = RolePage(context)
	page.click_edit_role_btn()
	pass

@When('user in edit role page')
def step_impl(context):
	page = RolePage(context)
	page.validate_update_role_page()
	pass

@then('user will update the role')
def step_impl(context):

	page = RolePage(context)
	page.click_submit_update_role()
	pass
import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click edit permission button')
def step_impl(context):

	page = PermissionPage(context)
	page.click_edit_permission_btn()
	pass

@When('user in edit permission page')
def step_impl(context):
	page = PermissionPage(context)
	page.validate_update_permission_page()
	pass

@then('user will update the permission')
def step_impl(context):

	page = PermissionPage(context)
	page.click_submit_update_permission()
	pass
import time
from pages import *
from behave import *
from selenium import webdriver

@then('user will navigates to Permission page')
def step_impl(context):

	page = PermissionPage(context)
	page.visit_permission_page()
	pass

@when('user in Permission page')
def step_impl(context):

	page = PermissionPage(context)
	page.validate_permission_page()
	pass

@then('user will click create permission button')
def step_impl(context):

	page = PermissionPage(context)
	page.click_permission_btn()
	pass

@When('user in create permission page')
def step_impl(context):
	page = PermissionPage(context)
	page.validate_create_permission_page()
	pass

@then('user type "{prmssn}" in name input textbox')
def step_impl(context, prmssn):
	page = PermissionPage(context)
	page.enter_permission_name(prmssn)
	pass

@then('user type "{details}" in details input textbox')
def step_impl(context, details):

	page = PermissionPage(context)
	page.enter_permission_detail(details)
	pass

@then('user will save the new permission')
def step_impl(context):

	page = PermissionPage(context)
	page.click_submit_create_permission()
	pass

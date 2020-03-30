import time
from pages import *
from behave import *
from selenium import webdriver

@then('user will navigates to Vessel page')
def step_impl(context):

	page = VesselPage(context)
	page.visit_vessel_page()
	pass

@when('user in Vessel page')
def step_impl(context):

	page = VesselPage(context)
	page.validate_vessel_page()
	pass

@then('user will click create vessel button')
def step_impl(context):

	page = VesselPage(context)
	page.click_vessel_btn()
	pass

@When('user in create vessel page')
def step_impl(context):
	page = VesselPage(context)
	page.validate_create_vessel_page()
	pass

@then('user type "{prmssn}" in vessel name input textbox')
def step_impl(context, prmssn):
	page = VesselPage(context)
	page.enter_vessel_name(prmssn)
	pass

@then('user type "{details}" in vessel imo input textbox')
def step_impl(context, details):

	page = VesselPage(context)
	page.enter_vessel_imo(details)
	pass

@then('user will save the new vessel')
def step_impl(context):

	page = VesselPage(context)
	page.click_submit_create_vessel()
	pass

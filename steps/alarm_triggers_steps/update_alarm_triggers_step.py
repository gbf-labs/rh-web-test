import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click update button in alarm trigger page')
def step_impl(context):

	page = AlarmTriggersPage(context)
	page.click_edit_alarm_trigger_btn()
	pass

@When('user in update alarm triggers')
def step_impl(context):
	page = AlarmTriggersPage(context)
	page.validate_update_alarm_trigger_page()
	pass

@then('user will update the alarm trigger')
def step_impl(context):

	page = AlarmTriggersPage(context)
	page.click_submit_update_alarm_trigger()
	pass
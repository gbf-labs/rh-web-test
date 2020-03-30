import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click update button in alarm value page')
def step_impl(context):

	page = AlarmValuesPage(context)
	page.click_edit_alarm_value_btn()
	pass

@When('user in update alarm values')
def step_impl(context):
	page = AlarmValuesPage(context)
	page.validate_update_alarm_value_page()
	pass

@then('user will update the alarm value')
def step_impl(context):

	page = AlarmValuesPage(context)
	page.click_submit_update_alarm_value()
	pass
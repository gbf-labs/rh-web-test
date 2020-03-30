import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click update button in alarm condition page')
def step_impl(context):

	page = AlarmConditionsPage(context)
	page.click_edit_alarm_condition_btn()
	pass

@When('user in update alarm conditions')
def step_impl(context):
	page = AlarmConditionsPage(context)
	page.validate_update_alarm_condition_page()
	pass

@then('user will update the alarm condition')
def step_impl(context):

	page = AlarmConditionsPage(context)
	page.click_submit_update_alarm_condition()
	pass
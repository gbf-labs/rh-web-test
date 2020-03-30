import time
from pages import *
from behave import *
from selenium import webdriver

@then('user will navigates to Alarm Conditions page')
def step_impl(context):

    page = AlarmConditionsPage(context)
    page.visit_alarm_condition_page()
    pass

@when('user in Alarm Conditions page')
def step_impl(context):

    page = AlarmConditionsPage(context)
    page.validate_alarm_condition_page()
    pass

@then('user will click create button in alarm condition page')
def step_impl(context):

    page = AlarmConditionsPage(context)
    page.click_alarm_condition_btn()
    pass

@When('user in create alarm conditions')
def step_impl(context):

    page = AlarmConditionsPage(context)
    page.validate_create_alarm_condition_page()
    pass

@then('user type "{details}" in comment input textbox')
def step_impl(context, details):
    
    page = AlarmConditionsPage(context)
    page.enter_alarm_condition_comment(details)
    pass

@then('user select "{details}" in "{transac}" Operator')
def step_impl(context, details, transac):

    page = AlarmConditionsPage(context)
    page.enter_alarm_operator(details, transac)
    pass

@then('user select "{details}" in parameter 1')
def step_impl(context, details):
    
    page = AlarmConditionsPage(context)
    page.enter_alarm_param1(details)
    pass

@then('user select "{details}" in parameter 2')
def step_impl(context, details):
    
    page = AlarmConditionsPage(context)
    page.enter_alarm_param2(details)
    pass

@then('user select "{details}" in parameter 3')
def step_impl(context, details):
    
    page = AlarmConditionsPage(context)
    page.enter_alarm_param3(details)
    pass

@then('user will save the new alarm condition')
def step_impl(context):

    page = AlarmConditionsPage(context)
    page.click_submit_create_alarm_condition()
    time.sleep(10)
    pass
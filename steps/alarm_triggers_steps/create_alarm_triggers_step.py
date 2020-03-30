import time
from pages import *
from behave import *
from selenium import webdriver

@then('user will navigates to Alarm Triggers page')
def step_impl(context):

    page = AlarmTriggersPage(context)
    page.visit_alarm_trigger_page()
    pass

@when('user in Alarm Triggers page')
def step_impl(context):

    page = AlarmTriggersPage(context)
    page.validate_alarm_trigger_page()
    pass

@then('user will click create button in Alarm Trigger page')
def step_impl(context):

    page = AlarmTriggersPage(context)
    page.click_alarm_trigger_btn()
    pass

@When('user in create alarm triggers')
def step_impl(context):

    page = AlarmTriggersPage(context)
    page.validate_create_alarm_trigger_page()
    pass

@then('user type "{details}" in label input textbox alarm trigger')
def step_impl(context, details):
    
    page = AlarmTriggersPage(context)
    page.enter_alarm_trigger_label(details)
    pass

@then('user type "{details}" in description input textbox alarm trigger')
def step_impl(context, details):
    
    page = AlarmTriggersPage(context)
    page.enter_alarm_trigger_desc(details)
    pass

@then('user "{details}" the alarm enable toggle alarm trigger')
def step_impl(context, details):
    
    page = AlarmTriggersPage(context)
    page.alarm_enable(details)
    pass

@then('user "{details}" the alarm acknowledge toggle alarm trigger')
def step_impl(context, details):
    
    page = AlarmTriggersPage(context)
    page.alarm_acknowledge(details)
    pass

@then('user select "{alarm_type}" in "{transac}" Alarm Types')
def step_impl(context, alarm_type, transac):
    
    page = AlarmTriggersPage(context)
    page.select_alarm_type(alarm_type, transac)
    pass

@then('user select "{alarm_condition}" in "{transac}" Alarm Conditions')
def step_impl(context, alarm_condition, transac):
    
    page = AlarmTriggersPage(context)
    page.select_alarm_condition(alarm_condition, transac)
    pass

@then('user will save the new alarm trigger')
def step_impl(context):

    page = AlarmTriggersPage(context)
    page.click_submit_create_alarm_trigger()
    pass
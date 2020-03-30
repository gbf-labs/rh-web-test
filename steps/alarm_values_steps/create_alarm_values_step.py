import time
from pages import *
from behave import *
from selenium import webdriver

@then('user will navigates to Alarm Values page')
def step_impl(context):

    page = AlarmValuesPage(context)
    page.visit_alarm_value_page()
    pass

@when('user in Alarm Values page')
def step_impl(context):

    page = AlarmValuesPage(context)
    page.validate_alarm_value_page()
    pass

@then('user will click create button in alarm value page')
def step_impl(context):

    page = AlarmValuesPage(context)
    page.click_alarm_value_btn()
    pass

@When('user in create alarm values')
def step_impl(context):

    page = AlarmValuesPage(context)
    page.validate_create_alarm_value_page()
    pass

@then('user type "{details}" in name input textbox alarm value')
def step_impl(context, details):
    
    page = AlarmValuesPage(context)
    page.enter_alarm_value_name(details)
    pass

@then('user type "{details}" in vessel input textbox "{transac}" alarm value')
def step_impl(context, details, transac):
    page = AlarmValuesPage(context)
    if details not in ['nothing', 0 , '']:
        page.enter_alarm_value_vessel(details, transac)
    pass

@then('user type "{details}" in device input textbox "{transac}" alarm value')
def step_impl(context, details, transac):
    
    page = AlarmValuesPage(context)
    if details not in ['nothing', 0 , '']:
        page.enter_alarm_value_device(details, transac)
    pass

@then('user type "{details}" in device type input textbox "{transac}" alarm value')
def step_impl(context, details, transac):
    
    page = AlarmValuesPage(context)
    if details not in ['nothing', 0 , '']:
        page.enter_alarm_value_device_type(details, transac)
    pass

@then('user type "{details}" in module input textbox "{transac}" alarm value')
def step_impl(context, details, transac):
    
    page = AlarmValuesPage(context)
    if details not in ['nothing', 0 , '']:
        page.enter_alarm_value_module(details, transac)
    pass

@then('user type "{details}" in option input textbox "{transac}" alarm value')
def step_impl(context, details, transac):
    
    page = AlarmValuesPage(context)
    page.enter_alarm_value_option(details, transac)
    pass

@then('user type "{details}" in value input textbox "{transac}" alarm value')
def step_impl(context, details, transac):
    
    page = AlarmValuesPage(context)
    page.enter_alarm_value(details, transac)
    pass

@then('user will save the new alarm value')
def step_impl(context):

    page = AlarmValuesPage(context)
    page.click_submit_create_alarm_value()
    time.sleep(10)
    pass
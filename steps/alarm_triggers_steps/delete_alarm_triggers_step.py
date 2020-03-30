import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click delete alarm trigger button')
def step_impl(context):

    page = AlarmTriggersPage(context)
    page.click_delete_alarm_trigger_btn()
    pass

@then('user will find "{details}" in Alarm Triggers page')
def step_impl(context, details):

    page = AlarmTriggersPage(context)
    page.find_alarm_trigger_key(details)
    pass
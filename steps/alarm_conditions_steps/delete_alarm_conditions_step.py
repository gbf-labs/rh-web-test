import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click delete alarm condition button')
def step_impl(context):

    page = AlarmConditionsPage(context)
    page.click_delete_alarm_condition_btn()
    pass

@then('user will find "{details}" in Alarm Conditions page')
def step_impl(context, details):

    page = AlarmConditionsPage(context)
    page.find_alarm_condition_key(details)
    pass
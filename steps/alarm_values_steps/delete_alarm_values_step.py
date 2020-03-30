import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click delete alarm value button')
def step_impl(context):

    page = AlarmValuesPage(context)
    page.click_delete_alarm_value_btn()
    pass

@then('user will find "{details}" in Alarm Values page')
def step_impl(context, details):

    page = AlarmValuesPage(context)
    page.find_alarm_value_key(details)
    pass
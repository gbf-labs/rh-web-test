import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will click delete vessel button')
def step_impl(context):

    page = VesselPage(context)
    page.click_delete_vessel_btn()
    pass

@then('user will find "{details}" in Vessel page')
def step_impl(context, details):

    page = VesselPage(context)
    page.find_vessel_key(details)
    pass
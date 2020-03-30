import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will confirm delete of device image')
def step_impl(context):

    page = DeviceImagePage(context)
    page.confirm_delete_image()
    pass

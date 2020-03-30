import time
from pages import *
from behave import *
from selenium import webdriver
from steps import *

@then('user will navigates to Admin Devices page')
def step_impl(context):

    page = DeviceImagePage(context)
    page.visit_device_image_page()
    pass

@then('user find "{vessel}" in Admin Device List')
def step_impl(context, vessel):

    page = DeviceImagePage(context)
    page.find_vessel_key(vessel)
    pass

# @when('user in "ALP Winger" tab')
# def step_impl(context):

#     page = DeviceImagePage(context)
#     page.click_delete_image()
#     pass

@then('user will look for "{device}" device in "{vessel}" tab and "{transact}"')
def step_impl(context, device, vessel, transact):

    page = DeviceImagePage(context)
    page.find_device_image(vessel, device, transact)
    pass

# @when('user in Upload Device Image page')
# def step_impl(context):
#     page = DeviceImagePage(context)
#     page.validate_upload_device_image()
#     pass


@then('user will choose file to upload')
def step_impl(context):

    page = DeviceImagePage(context)
    page.select_device_image()
    pass

@then('user will click upload')
def step_impl(context):

    page = DeviceImagePage(context)
    page.upload_device_image()
    pass

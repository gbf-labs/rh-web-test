import time
from pages import *
from behave import *
from selenium import webdriver

# import config
from configparser import ConfigParser
from library.config_parser import configSectionParser


# INIT CONFIG
config = ConfigParser()
# CONFIG FILE
config.read("config/config.cfg")

protocol = configSectionParser(config, "SERVER")['protocol']
host = configSectionParser(config, "SERVER")['host']

@given('a user will logged in')
def step_impl(context):

    page = LoginPage(context)

    url = protocol + "://" + host + "/signin"
    print("url: ", url)
    page.visit_login_page(url)

    #page.enter_credentials("gbfdummy2019@gmail.com","trustno@1")
    page.enter_credentials("gbfdummy2019@gmail.com","trustno@1")
    time.sleep(5)
    pass

# @when('we implement {number:d} tests')
@then('after {number:d} seconds user clicks the maps')
def step_impl(context, number):  # -- NOTE: number is converted into integer

    time.sleep(number)
    page = MapsPage(context)
    page.visit_map_page()
    time.sleep(number)
    pass

@then('user will navigates to Dashboard page')
def step_impl(context):

	page = DashboardPage(context)
	page.visit_dashboard_page()
	pass

@when('user in "{details}" page')
def step_impl(context, details):
    page = BreadCrumbs(context)
    page.verify_landing_page(details)
    pass

@then('user will logout')
def step_impl(context):
    time.sleep(5)
    page = LoginPage(context)
    page.logout()
    pass
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
email_address = configSectionParser(config,"RECEIVER")['email']

@given('a user will login to gmail')
def step_impl(context):

    page = EmailPage(context)
    page.login_gmail()
    time.sleep(5)
    pass

@then('user will check the "{subject}" email and login to RH site')
def step_impl(context, subject):
    
    page = EmailPage(context)
    time.sleep(5)
    
    email_password = page.check_email_password(subject)
    print("^^^^^^")
    print(email_password)
    print("^^^^^^")

    if email_password is not "":

        page = LoginPage(context)

        url = protocol + "://" + host + "/signin"

        page.visit_login_page(url)
        page.enter_credentials(email_address, email_password)
        time.sleep(15)


    else:
        print("Pass")
        pass

# @when('user in "{details}" page')
# def step_impl(context, details):
#     page = EmailPage(context)
#     page.verify__page(details)
#     pass
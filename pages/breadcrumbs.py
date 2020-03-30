#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import gmail
import configparser
import os
import html2text

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from library.locators import *
from .common import Page
from library.config_parser import configSectionParser

#INIT CONFIG
config = configparser.ConfigParser()
config.read("config/config.cfg")

#CONFIG
receiver_email = configSectionParser(config,"RECEIVER")['email']
receiver_password = configSectionParser(config,"RECEIVER")['password']
sender_email = configSectionParser(config,"SENDER")['email']

class BreadCrumbs(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)
        
    
    def verify_landing_page(self, details):

        if details.upper() == "PERMISSION":
            loc = PermissionLocators.PERMISSION_BREADCRUMB
            page_name = 'RBAC Permissions'

        elif details.upper() == "CREATE PERMISSION":
            loc = PermissionLocators.CREATE_PERMISSION_PAGE
            page_name = "Create Permission"

        elif details.upper() == "EDIT PERMISSION":
            loc = PermissionLocators.UPDATE_PERMISSION_PAGE
            page_name = "Edit Permission"
        
        elif details.upper() == "ROLE":
            loc = RoleLocators.ROLE_BREADCRUMB
            page_name = "RBAC Roles"

        elif details.upper() == "CREATE ROLE":
            loc = RoleLocators.CREATE_ROLE_PAGE
            page_name = "Create Role"
    
        elif details.upper() == "EDIT ROLE":
            loc = RoleLocators.UPDATE_ROLE_PAGE
            page_name = "Create Role"

        elif details.upper() == "COMPANY":
            loc = RoleLocators.ROLE_BREADCRUMB
            page_name = "Admin Company"

        elif details.upper() == "CREATE COMPANY":
            loc = RoleLocators.CREATE_ROLE_PAGE
            page_name = "Create Company"
    
        elif details.upper() == "EDIT COMPANY":
            loc = RoleLocators.UPDATE_ROLE_PAGE
            page_name = "Update Company"

        elif details.upper() == "USERS":
            loc = UsersLocators.USERS_BREADCRUMB
            page_name = "RBAC Users"

        elif details.upper() == "INVITE USER":
            loc = UsersLocators.INVITE_USER
            page_name = "Invite User"
    
        elif details.upper() == "UPDATE USER":
            loc = UsersLocators.UPDATE_USER
            page_name = "Update User"

        elif details.upper() == "ALARM VALUES":
            loc = AlarmValuesLocators.ALARM_VALUES_BREADCRUMB
            page_name = "Alarm Values"

        elif details.upper() == "CREATE ALARM VALUES":
            loc = AlarmValuesLocators.CREATE_ALARM_VALUE_PAGE
            page_name = "Create Alarm Values"
    
        elif details.upper() == "UPDATE ALARM VALUES":
            loc = AlarmValuesLocators.UPDATE_ALARM_VALUE_PAGE
            page_name = "Update Alarm Values"

        elif details.upper() == "ALARM CONDITIONS":
            loc = AlarmConditionsLocators.ALARM_CONDITIONS_BREADCRUMB
            page_name = "Alarm Conditions"

        elif details.upper() == "CREATE ALARM CONDITIONS":
            loc = AlarmConditionsLocators.CREATE_ALARM_CONDITION_PAGE
            page_name = "Create Alarm Conditions"
    
        elif details.upper() == "UPDATE ALARM CONDITIONS":
            loc = AlarmConditionsLocators.UPDATE_ALARM_CONDITION_PAGE
            page_name = "Update Alarm Conditions"

        elif details.upper() == "ALARM TRIGGERS":
            loc = AlarmTriggersLocators.ALARM_TRIGGERS_BREADCRUMB
            page_name = "Alarm Triggers"

        elif details.upper() == "CREATE ALARM TRIGGERS":
            loc = AlarmTriggersLocators.CREATE_ALARM_TRIGGER_PAGE
            page_name = "Create Alarm Trigger"
    
        elif details.upper() == "UPDATE ALARM TRIGGERS":
            loc = AlarmTriggersLocators.UPDATE_ALARM_TRIGGER_PAGE
            page_name = "Update Alarm Trigger"

        elif details.upper() == "VESSEL":
            print(details)
            loc = VesselLocators.VESSEL_BREADCRUMB
            page_name = "Admin Vessels"

        elif details.upper() == "CREATE VESSEL":
            loc = VesselLocators.CREATE_VESSEL_PAGE
            page_name = "Create Vessel"
        
        elif details.upper() == "SUB CATEGORY":
            loc = SubCategoryLocators.SUBCATEGORY_BREADCRUMB
            page_name = "Sub Category"

        elif details.upper() == "CREATE SUB CATEGORY":
            loc = SubCategoryLocators.CREATE_SUBCATEGORY_PAGE
            page_name = "Create Sub Category"

        elif details.upper() == "UPDATE SUB CATEGORY":
            loc = SubCategoryLocators.UPDATE_SUBCATEGORY_PAGE
            page_name = "Update Sub Category"

        elif details.upper() == "UPDATE SUB CATEGORY":
            loc = SubCategoryLocators.UPDATE_SUBCATEGORY_PAGE
            page_name = "Update Sub Category"

        elif details.upper() == "ADMIN DEVICES":
            loc = DeviceImageLocators.DEVICE_IMAGE_BREADCRUMB
            page_name = "Admin Devices"

        elif details.upper() == "UPLOAD DEVICE IMAGE":
            loc = DeviceImageLocators.UPLOAD_DEVICE_IMAGE
            page_name = "Upload Device Image"

        elif details.upper() == "MAPS":
            loc = MapsLocators.MAPS_BREADCRUMB
            page_name = "Maps"

        # assert(self.find_element(*UsersLocators.MAPS_BREADCRUMB))
        print("L O C: ", loc)
        breadcrumbs = self.browser.find_element_by_xpath(loc).text
        print("****",breadcrumbs)
        
        if breadcrumbs == page_name:
            print("On Page")
            # CHECK IF THERE'S SOMETHING WRONG
            print("------", details)
            if details in ['Permission', 'Role', 'Company', 'Alarm Values',
                           'Alarm Conditions', 'Alarm Triggers', 'Maps', 'Users',
                           'Vessel', 'Sub Category', 'SubCategory', 'Admin Devices'
                          ]:
                print("Checker ***")
                # self.check_something_wrong()

            else:
                print("Checker pass")

        else:
            raise Exception("Something Went Wrong")



    def check_something_wrong(self):

        snackbar = self.find_element_exist(*CommonLocators.MESSAGE_BAR)
        print("Snackbar:", snackbar)

        # CHECK SNACKBAR FOR 5 SECS
        for _ in range(1, 3):

            self.sleeper(1)
            if snackbar:
                print("Something Went Wrong")
                raise Exception("Something Went Wrong")
            else:
                print("No issue found")

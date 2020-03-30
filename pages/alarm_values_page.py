#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from library.locators import *
from .common import Page
import time

# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class AlarmValuesPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_alarm_value_page(self):
        self.sleeper(20)
        try:

            self.find_element(*NavigationPageLocators.ALARM_DOWN).click()
            self.find_element(*NavigationPageLocators.ALARM_VALUES).click()
            self.sleeper(2)#WAIT TO SHOW ALARM_VALUES TABLE

        except:

            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION
            self.find_element(*NavigationPageLocators.ALARM_DOWN).click()
            self.find_element(*NavigationPageLocators.ALARM_VALUES).click()
        


    def validate_alarm_value_page(self):
        assert(self.find_element(*AlarmValuesLocators.ALARM_VALUES_BREADCRUMB))
        print(*AlarmValuesLocators.ALARM_VALUES_BREADCRUMB)

    def validate_create_alarm_value_page(self):
        assert(self.find_element(*AlarmValuesLocators.CREATE_ALARM_VALUE_PAGE))

    def click_alarm_value_btn(self):
        self.find_element_down(*AlarmValuesLocators.CREATE_ALARM_VALUE_BTN)
        self.sleeper(2)

    def enter_alarm_value_name(self, name):
        self.clear_input_field(*AlarmValuesLocators.INPUT_ALARM_VALUE_NAME)
        self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_NAME).send_keys(name)
        
    def enter_alarm_value_vessel(self, vessel, transac):
        if transac == "update":
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_VESSEL_DELETE).click()
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_VESSEL).click()
        
        self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_VESSEL_AUTO).send_keys(vessel)
        self.sleeper(1)
        self.tab_xpath(*AlarmValuesLocators.INPUT_ALARM_VALUE_VESSEL_AUTO)
        self.sleeper(2)

    def enter_alarm_value_device(self, device, transac):
        if transac == "update":
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_DEVICE_DELETE).click()
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_DEVICE).click()
        self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_DEVICE_AUTO).send_keys(device)
        self.sleeper(1)
        self.tab_xpath(*AlarmValuesLocators.INPUT_ALARM_VALUE_DEVICE_AUTO)
        self.sleeper(2)

    def enter_alarm_value_device_type(self, device_type, transac):
        if transac == "update":
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_DEVICE_TYPE_DELETE).click()
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_DEVICE_TYPE).click()
        self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_DEVICE_TYPE_AUTO).send_keys(device_type)
        self.sleeper(1)
        self.tab_xpath(*AlarmValuesLocators.INPUT_ALARM_VALUE_DEVICE_TYPE_AUTO)
        self.sleeper(2)
    
    def enter_alarm_value_module(self, module, transac):

        if transac == "update":
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_MODULE_DELETE).click()
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_MODULE).click()
            print("Clear Module--------")
        self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_MODULE_AUTO).send_keys(module)
        self.sleeper(1)
        self.tab_xpath(*AlarmValuesLocators.INPUT_ALARM_VALUE_MODULE_AUTO)
        self.sleeper(2)

    def enter_alarm_value_option(self, option, transac):
        if transac == "update":
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_OPTION_DELETE).click()
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_OPTION).click()
        self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_OPTION_AUTO).send_keys(option)
        self.sleeper(1)
        self.tab_xpath(*AlarmValuesLocators.INPUT_ALARM_VALUE_OPTION_AUTO)
        self.sleeper(2)

    def enter_alarm_value(self, val, transac):
        if transac == "update":
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_DELETE).click()
            self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE).click()
        self.find_element(*AlarmValuesLocators.INPUT_ALARM_VALUE_AUTO).send_keys(val)
        self.sleeper(1)
        self.tab_xpath(*AlarmValuesLocators.INPUT_ALARM_VALUE_AUTO)
        self.sleeper(2)

    def click_submit_create_alarm_value(self):
        self.find_element(*AlarmValuesLocators.CREATE_SUBMIT_BTN).click()
        self.sleeper(2)

    def click_delete_alarm_value_btn(self):
        self.find_element_down(*AlarmValuesLocators.DELETE_ALARM_VALUE_BTN)
        self.sleeper(2)

    def find_alarm_value_key(self, details):
        
        # CHECK NUMBER OF ITEMS
        self.move_to_element(*AlarmValuesLocators.TOTAL_ITEMS)
        pagination = self.find_element(*AlarmValuesLocators.TOTAL_ITEMS).text
        print(pagination)

        if pagination:
            count = pagination.split()
            item_counts = count[0].split('-')
            items = int(item_counts[-1])
            item_start = int(item_counts[0])
            print("items", items)
            print("item_start", item_start)
            if items > 10:
                items = (items - item_start) + 1

            item_count = int(count[len(count)-1])
            print("---->", item_count)
            
            if items > 1:
            
                BEFORE_XPATH_KEY = AlarmValuesLocators.BEFORE_XPATH_KEY
                AFTER_XPATH_KEY = AlarmValuesLocators.AFTER_XPATH_KEY
                AFTER_XPATH_CHECKBOX = AlarmValuesLocators.AFTER_XPATH_CHECKBOX

                find = self.find_dynamic_element(BEFORE_XPATH_KEY, AFTER_XPATH_KEY, 
                                            AFTER_XPATH_CHECKBOX, details, items)

                print("****", find)

                if not find:
                    next_page = self.check_button_enabled(*AlarmValuesLocators.NEXT_PAGINATION)

                    if next_page:

                        print("Next page Enabled")
                        self.find_element_down(*AlarmValuesLocators.NEXT_PAGINATION)
                        self.find_alarm_value_key(details)

                    else:

                        print("Next page disabled")
                        raise Exception("Key not found")
                else:
                    return 1
            else:

                key = self.find_element(*AlarmValuesLocators.ITEM_KEY).text

                if key == details:
                    self.find_element(*AlarmValuesLocators.ITEM_BOX).click()
                    return 1
                else:
                    return 0

        self.sleeper(2)

    def validate_update_alarm_value_page(self):
        assert(self.find_element(*AlarmValuesLocators.UPDATE_ALARM_VALUE_PAGE))

    def click_edit_alarm_value_btn(self):
        self.find_element_down(*AlarmValuesLocators.UPDATE_ALARM_VALUE_BTN)
        self.sleeper(2)

    def click_submit_update_alarm_value(self):
        self.find_element(*AlarmValuesLocators.UPDATE_SUBMIT_BTN).click()
        self.sleeper(2)

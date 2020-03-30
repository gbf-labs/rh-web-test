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

class AlarmTriggersPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_alarm_trigger_page(self):
        self.sleeper(10)
        try:

            self.find_element(*NavigationPageLocators.ALARM_DOWN).click()
            self.find_element(*NavigationPageLocators.ALARM_TRIGGERS).click()
            self.sleeper(2)#WAIT TO SHOW ALARM_TRIGGERS TABLE

        except:

            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION
            self.find_element(*NavigationPageLocators.ALARM_DOWN).click()
            self.find_element(*NavigationPageLocators.ALARM_TRIGGERS).click()

    def validate_alarm_trigger_page(self):
        assert(self.find_element(*AlarmTriggersLocators.ALARM_TRIGGERS_BREADCRUMB))
        print(*AlarmTriggersLocators.ALARM_TRIGGERS_BREADCRUMB)

    def validate_create_alarm_trigger_page(self):
        assert(self.find_element(*AlarmTriggersLocators.CREATE_ALARM_TRIGGER_PAGE))

    def click_alarm_trigger_btn(self):
        self.find_element_down(*AlarmTriggersLocators.CREATE_ALARM_TRIGGER_BTN)
        self.sleeper(2)

    def enter_alarm_trigger_label(self, label):
        self.clear_input_field(*AlarmTriggersLocators.INPUT_ALARM_TRIGGER_LABEL)
        self.find_element(*AlarmTriggersLocators.INPUT_ALARM_TRIGGER_LABEL).send_keys(label)

    def enter_alarm_trigger_desc(self, desc):
        self.clear_input_field(*AlarmTriggersLocators.INPUT_ALARM_TRIGGER_DESC)
        self.find_element(*AlarmTriggersLocators.INPUT_ALARM_TRIGGER_DESC).send_keys(desc)

    def alarm_enable(self, toggle):
        self.find_toggle(AlarmTriggersLocators.INPUT_ALARM_ENABLED, toggle)
        self.sleeper(2)

    def alarm_acknowledge(self, toggle):
        print(toggle)
        self.find_toggle(AlarmTriggersLocators.INPUT_ALARM_ACKNOWLEDGE, toggle)
        self.sleeper(2)

    def select_alarm_type(self, alarm_type, transac):
        if transac == "update":
            self.find_element(*AlarmTriggersLocators.INPUT_ALARM_TYPE_DELETE).click()
            self.find_element(*AlarmTriggersLocators.INPUT_ALARM_TYPE).click()
        self.find_element(*AlarmTriggersLocators.INPUT_ALARM_TYPE_AUTO).send_keys(alarm_type)
        self.sleeper(1)
        self.tab_xpath(*AlarmTriggersLocators.INPUT_ALARM_TYPE_AUTO)
        self.sleeper(2)

    def select_alarm_condition(self, condition, transac):
        if transac == "update":
            self.find_element(*AlarmTriggersLocators.INPUT_ALARM_CONDITION_DELETE).click()
            self.find_element(*AlarmTriggersLocators.INPUT_ALARM_CONDITION).click()
        self.find_element(*AlarmTriggersLocators.INPUT_ALARM_CONDITION_AUTO).send_keys(condition)
        self.sleeper(1)
        self.tab_xpath(*AlarmTriggersLocators.INPUT_ALARM_CONDITION_AUTO)
        self.sleeper(2)

    def click_submit_create_alarm_trigger(self):
        self.find_element(*AlarmTriggersLocators.CREATE_SUBMIT_BTN).click()
        self.sleeper(2)

    def click_delete_alarm_trigger_btn(self):
        self.find_element_down(*AlarmTriggersLocators.DELETE_ALARM_TRIGGER_BTN)
        self.sleeper(2)

    def find_alarm_trigger_key(self, details):

        # CHECK NUMBER OF ITEMS
        self.move_to_element(*AlarmConditionsLocators.TOTAL_ITEMS)
        pagination = self.find_element(*AlarmConditionsLocators.TOTAL_ITEMS).text
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
        
                BEFORE_XPATH_KEY = AlarmTriggersLocators.BEFORE_XPATH_KEY
                AFTER_XPATH_KEY = AlarmTriggersLocators.AFTER_XPATH_KEY
                AFTER_XPATH_CHECKBOX = AlarmTriggersLocators.AFTER_XPATH_CHECKBOX

                find = self.find_dynamic_element(BEFORE_XPATH_KEY, AFTER_XPATH_KEY, 
                                            AFTER_XPATH_CHECKBOX, details, items)
                if not find:
                    next_page = self.check_button_enabled(*AlarmTriggersLocators.NEXT_PAGINATION)

                    if next_page:
                        self.find_element_down(*AlarmTriggersLocators.NEXT_PAGINATION)
                        self.find_alarm_trigger_key(details)

                    else:
                        raise Exception("Key not found")
                else:
                    return 1
            else:
                
                key = self.find_element(*AlarmTriggersLocators.ITEM_KEY).text

                if key == details:
                    self.find_element(*AlarmTriggersLocators.ITEM_BOX).click()
                    return 1
                else:
                    return 0

        self.sleeper(2)

    def validate_update_alarm_trigger_page(self):
        assert(self.find_element(*AlarmTriggersLocators.UPDATE_ALARM_TRIGGER_PAGE))

    def click_edit_alarm_trigger_btn(self):
        self.find_element_down(*AlarmTriggersLocators.UPDATE_ALARM_TRIGGER_BTN)
        self.sleeper(2)

    def click_submit_update_alarm_trigger(self):
        self.find_element(*AlarmTriggersLocators.UPDATE_SUBMIT_BTN).click()
        self.sleeper(2)

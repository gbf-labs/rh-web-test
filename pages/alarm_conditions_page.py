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

class AlarmConditionsPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_alarm_condition_page(self):
        self.sleeper(10)
        try:
            if self.find_element(*NavigationPageLocators.ALARM_DOWN):
                self.find_element(*NavigationPageLocators.ALARM_DOWN).click()

            self.find_element(*NavigationPageLocators.ALARM_CONDITIONS).click()
            self.sleeper(2)#WAIT TO SHOW ALARM_CONDITIONS TABLE

        except:

            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION
            self.find_element(*NavigationPageLocators.ALARM_DOWN).click()
            self.find_element(*NavigationPageLocators.ALARM_CONDITIONS).click()

    def validate_alarm_condition_page(self):
        assert(self.find_element(*AlarmConditionsLocators.ALARM_CONDITIONS_BREADCRUMB))
        print(*AlarmConditionsLocators.ALARM_CONDITIONS_BREADCRUMB)

    def validate_create_alarm_condition_page(self):
        assert(self.find_element(*AlarmConditionsLocators.CREATE_ALARM_CONDITION_PAGE))

    def click_alarm_condition_btn(self):
        self.find_element_down(*AlarmConditionsLocators.CREATE_ALARM_CONDITION_BTN)
        self.sleeper(2)

    def enter_alarm_condition_comment(self, comment):
        self.clear_input_field(*AlarmConditionsLocators.INPUT_ALARM_COMMENT)
        self.find_element(*AlarmConditionsLocators.INPUT_ALARM_COMMENT).send_keys(comment)
        
    def enter_alarm_operator(self, vessel, transac):
        if transac == "update":
            self.find_element(*AlarmConditionsLocators.INPUT_ALARM_OPERATOR_DELETE).click()
            self.find_element(*AlarmConditionsLocators.INPUT_ALARM_OPERATOR).click()
        self.find_element(*AlarmConditionsLocators.INPUT_ALARM_OPERATOR_AUTO).send_keys(vessel)
        self.sleeper(1)
        self.tab_xpath(*AlarmConditionsLocators.INPUT_ALARM_OPERATOR_AUTO)
        self.sleeper(2)

    def enter_alarm_param1(self, param):
        self.find_element(*AlarmConditionsLocators.INPUT_ALARM_PARAM1_DEL).click()
        self.find_element_down(*AlarmConditionsLocators.INPUT_ALARM_PARAM1)
        self.find_element(*AlarmConditionsLocators.INPUT_PARAM1_AUTO).send_keys(param)
        self.sleeper(1)
        self.tab_alarm_xpath(*AlarmConditionsLocators.INPUT_PARAM1_AUTO)
        self.sleeper(2)

    def enter_alarm_param2(self, param):
        self.find_element(*AlarmConditionsLocators.INPUT_ALARM_PARAM2_DEL).click()
        self.find_element_down(*AlarmConditionsLocators.INPUT_ALARM_PARAM2)
        self.find_element(*AlarmConditionsLocators.INPUT_PARAM2_AUTO).send_keys(param)
        self.find_element(*AlarmConditionsLocators.INPUT_PARAM2_AUTO)

        self.sleeper(1)
        self.tab_alarm_xpath(*AlarmConditionsLocators.INPUT_PARAM2_AUTO)
        self.sleeper(2)
    
    def enter_alarm_param3(self, param):
        self.find_element(*AlarmConditionsLocators.INPUT_ALARM_PARAM3_DEL).click()
        self.find_element_down(*AlarmConditionsLocators.INPUT_ALARM_PARAM3)
        self.find_element(*AlarmConditionsLocators.INPUT_PARAM3_AUTO).send_keys(param)
        self.sleeper(1)
        self.tab_xpath(*AlarmConditionsLocators.INPUT_PARAM3_AUTO)
        self.sleeper(2)

    def click_submit_create_alarm_condition(self):
        self.find_element(*AlarmConditionsLocators.CREATE_SUBMIT_BTN).click()
        self.sleeper(2)

    def click_delete_alarm_condition_btn(self):
        self.find_element_down(*AlarmConditionsLocators.DELETE_ALARM_CONDITION_BTN)
        self.sleeper(2)

    def find_alarm_condition_key(self, details):

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
            print("Final item", items)
            item_count = int(count[len(count)-1])
            print("---->", item_count)
            
            if items > 1:

                BEFORE_XPATH_KEY = AlarmConditionsLocators.BEFORE_XPATH_KEY
                AFTER_XPATH_KEY = AlarmConditionsLocators.AFTER_XPATH_KEY
                AFTER_XPATH_CHECKBOX = AlarmConditionsLocators.AFTER_XPATH_CHECKBOX

                find = self.find_dynamic_element(BEFORE_XPATH_KEY, AFTER_XPATH_KEY, 
                                            AFTER_XPATH_CHECKBOX, details, items)
                print("*****", find)
                if not find:
                    next_page = self.check_button_enabled(*AlarmConditionsLocators.NEXT_PAGINATION)

                    if next_page:
                        self.find_element_down(*AlarmConditionsLocators.NEXT_PAGINATION)
                        self.find_alarm_condition_key(details)

                    else:
                        raise Exception("Key not found")
                else:
                    return 1
            else:
                
                key = self.find_element(*AlarmConditionsLocators.ITEM_KEY).text

                if key == details:
                    print("Match")
                    self.find_element(*AlarmConditionsLocators.ITEM_BOX).click()
                    return 1
                else:
                    print("Can't Find")
                    return 0

        self.sleeper(2)

    def validate_update_alarm_condition_page(self):
        assert(self.find_element(*AlarmConditionsLocators.UPDATE_ALARM_CONDITION_PAGE))

    def click_edit_alarm_condition_btn(self):
        self.find_element_down(*AlarmConditionsLocators.UPDATE_ALARM_CONDITION_BTN)
        self.sleeper(2)

    def click_submit_update_alarm_condition(self):
        self.find_element(*AlarmConditionsLocators.UPDATE_SUBMIT_BTN).click()
        self.sleeper(2)

#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from library.locators import *
from .common import Page
import time

# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class VesselPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_vessel_page(self):
        self.sleeper(20)
        try:

            self.find_element(*NavigationPageLocators.ADMIN_DOWN).click()
            self.find_element(*NavigationPageLocators.VESSEL).click()
            self.sleeper(2)#WAIT TO SHOW VESSEL TABLE

        except:
         
            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION

            self.find_element(*NavigationPageLocators.ADMIN_DOWN).click()
            self.find_element(*NavigationPageLocators.VESSEL).click()

    def validate_vessel_page(self):
        self.sleeper(30)
        assert(self.find_element(*VesselLocators.VESSEL_BREADCRUMB))

    def validate_create_vessel_page(self):
        self.sleeper(15)
        assert(self.find_element(*VesselLocators.CREATE_VESSEL_PAGE))

    def click_vessel_btn(self):

        self.find_element_down(*VesselLocators.CREATE_VESSEL_BTN)
        self.sleeper(2)
    
    def enter_vessel_name(self, name):
        self.clear_input_field(*VesselLocators.INPUT_VESSEL_NAME)
        self.find_element(*VesselLocators.INPUT_VESSEL_NAME).send_keys(name)
    
    def enter_vessel_imo(self, details):
        self.clear_input_field(*VesselLocators.INPUT_VESSEL_IMO)
        self.find_element(*VesselLocators.INPUT_VESSEL_IMO).send_keys(details)
        self.sleeper(2)

    def click_submit_create_vessel(self):

        self.find_element(*VesselLocators.CREATE_SUBMIT_BTN).click()
        self.sleeper(2)

    def click_delete_vessel_btn(self):
        self.find_element_down(*VesselLocators.DELETE_VESSEL_BTN)
        self.sleeper(2)
        self.find_element_down(*VesselLocators.CONFIRM_DELETE)
        self.sleeper(2)

    def find_vessel_key(self, details):
        self.sleeper(20)
        # CHECK NUMBER OF ITEMS
        self.move_to_element(*VesselLocators.TOTAL_ITEMS)
        pagination = self.find_element(*VesselLocators.TOTAL_ITEMS).text
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
                BEFORE_XPATH_KEY = VesselLocators.BEFORE_XPATH_KEY
                AFTER_XPATH_KEY = VesselLocators.AFTER_XPATH_KEY
                AFTER_XPATH_CHECKBOX = VesselLocators.AFTER_XPATH_CHECKBOX

                find = self.find_dynamic_element(BEFORE_XPATH_KEY, AFTER_XPATH_KEY, 
                                            AFTER_XPATH_CHECKBOX, details, items)
                if not find:
                    next_page = self.check_button_enabled(*VesselLocators.NEXT_PAGINATION)

                    if next_page:
                        self.find_element_down(*VesselLocators.NEXT_PAGINATION)
                        self.find_vessel_key(details)

                    else:
                        raise Exception("Key not found")
                else:
                    return 1
            else:

                key = self.find_element(*VesselLocators.ITEM_KEY).text

                if key == details:
                    self.find_element(*VesselLocators.ITEM_BOX).click()
                    return 1
                else:
                    return 0

        self.sleeper(2)
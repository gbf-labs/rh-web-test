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

class PermissionPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_permission_page(self):
        self.sleeper(20)
        try:

            self.find_element(*NavigationPageLocators.RBAC_DOWN).click()
            self.find_element(*NavigationPageLocators.PERMISSION).click()
            self.sleeper(2)#WAIT TO SHOW PERMISSION TABLE

        except:
         
            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION

            self.find_element(*NavigationPageLocators.RBAC_DOWN).click()
            self.find_element(*NavigationPageLocators.PERMISSION).click()

    def validate_permission_page(self):
        assert(self.find_element(*PermissionLocators.PERMISSION_BREADCRUMB))

    def validate_create_permission_page(self):
        assert(self.find_element(*PermissionLocators.CREATE_PERMISSION_PAGE))

    def click_permission_btn(self):

        self.find_element_down(*PermissionLocators.CREATE_PERMISSION_BTN)
        self.sleeper(2)

    def enter_permission_name(self, name):
        self.clear_input_field(*PermissionLocators.INPUT_PERMISSION_NAME)
        self.find_element(*PermissionLocators.INPUT_PERMISSION_NAME).send_keys(name)
    
    def enter_permission_detail(self, details):
        self.clear_input_field(*PermissionLocators.INPUT_PERMISSION_DETAILS)
        self.find_element(*PermissionLocators.INPUT_PERMISSION_DETAILS).send_keys(details)
        self.sleeper(2)

    def click_submit_create_permission(self):

        self.find_element(*PermissionLocators.CREATE_SUBMIT_BTN).click()
        self.sleeper(2)

    def click_delete_permission_btn(self):
        self.find_element_down(*PermissionLocators.DELETE_PERMISSION_BTN)
        self.sleeper(2)

    def find_permission_key(self, details):
        
        # CHECK NUMBER OF ITEMS
        self.move_to_element(*PermissionLocators.TOTAL_ITEMS)
        pagination = self.find_element(*PermissionLocators.TOTAL_ITEMS).text
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
                BEFORE_XPATH_KEY = PermissionLocators.BEFORE_XPATH_KEY
                AFTER_XPATH_KEY = PermissionLocators.AFTER_XPATH_KEY
                AFTER_XPATH_CHECKBOX = PermissionLocators.AFTER_XPATH_CHECKBOX

                find = self.find_dynamic_element(BEFORE_XPATH_KEY, AFTER_XPATH_KEY, 
                                            AFTER_XPATH_CHECKBOX, details, items)
                if not find:
                    next_page = self.check_button_enabled(*PermissionLocators.NEXT_PAGINATION)

                    if next_page:
                        self.find_element_down(*PermissionLocators.NEXT_PAGINATION)
                        self.find_permission_key(details)

                    else:
                        raise Exception("Key not found")
                else:
                    return 1
            else:

                key = self.find_element(*PermissionLocators.ITEM_KEY).text

                if key == details:
                    self.find_element(*PermissionLocators.ITEM_BOX).click()
                    return 1
                else:
                    return 0

        self.sleeper(2)

    def validate_update_permission_page(self):
        assert(self.find_element(*PermissionLocators.UPDATE_PERMISSION_PAGE))

    def click_edit_permission_btn(self):
        self.find_element_down(*PermissionLocators.UPDATE_PERMISSION_BTN)
        self.sleeper(2)

    def click_submit_update_permission(self):
        self.find_element(*PermissionLocators.UPDATE_SUBMIT_BTN).click()
        self.sleeper(2)
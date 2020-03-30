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

class RolePage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_role_page(self):
        self.sleeper(20)
        try:

            self.find_element(*NavigationPageLocators.RBAC_DOWN).click()
            self.find_element(*NavigationPageLocators.ROLE).click()
            self.sleeper(2)#WAIT TO SHOW ROLE TABLE

        except:

            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION
            self.find_element(*NavigationPageLocators.RBAC_DOWN).click()
            self.find_element(*NavigationPageLocators.ROLE).click()

    def validate_role_page(self):
        assert(self.find_element(*RoleLocators.ROLE_BREADCRUMB))
        print(*RoleLocators.ROLE_BREADCRUMB)

    def validate_create_role_page(self):
        assert(self.find_element(*RoleLocators.CREATE_ROLE_PAGE))

    def click_role_btn(self):
        self.find_element_down(*RoleLocators.CREATE_ROLE_BTN)
        self.sleeper(2)

    def enter_role_name(self, name):
        self.clear_input_field(*RoleLocators.INPUT_ROLE_NAME)
        self.find_element(*RoleLocators.INPUT_ROLE_NAME).send_keys(name)

    def enter_role_detail(self, details):
        self.clear_input_field(*RoleLocators.INPUT_ROLE_DETAILS)
        self.find_element(*RoleLocators.INPUT_ROLE_DETAILS).send_keys(details)
        self.sleeper(2)

    def select_role_permissions(self, details, process):
        self.find_element_down(*RoleLocators.SELECT_PERMISSIONS)

        count = self.count_permission(*RoleLocators.SELECT_PERMISSION_UL)

        if process == "update":
            self.unselect_role_permissions(count)
            self.find_element_down(*RoleLocators.SELECT_PERMISSIONS)

        BEFORE_SELECT_PERMISSION = RoleLocators.BEFORE_PERMISSION_PATH
        AFTER_SELECT_KEY = RoleLocators.AFTER_PERMISSION_KEY
        AFTER_SELECT_PERMISSION = RoleLocators.AFTER_PERMISSION_PATH

        self.select_list(BEFORE_SELECT_PERMISSION, AFTER_SELECT_KEY,
                                   AFTER_SELECT_PERMISSION, details, count)
        self.sleeper(2)


    def click_submit_create_role(self):
        self.find_element(*RoleLocators.CREATE_SUBMIT_BTN).click()
        self.sleeper(2)

    def click_delete_role_btn(self):
        self.find_element_down(*RoleLocators.DELETE_ROLE_BTN)
        self.sleeper(2)

    def find_role_key(self, details):
        
        # CHECK NUMBER OF ITEMS
        self.move_to_element(*RoleLocators.TOTAL_ITEMS)
        pagination = self.find_element(*RoleLocators.TOTAL_ITEMS).text
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
                BEFORE_XPATH_KEY = RoleLocators.BEFORE_XPATH_KEY
                AFTER_XPATH_KEY = RoleLocators.AFTER_XPATH_KEY
                AFTER_XPATH_CHECKBOX = RoleLocators.AFTER_XPATH_CHECKBOX

                find = self.find_dynamic_element(BEFORE_XPATH_KEY, AFTER_XPATH_KEY, 
                                            AFTER_XPATH_CHECKBOX, details, items)
                if not find:
                    next_page = self.check_button_enabled(*RoleLocators.NEXT_PAGINATION)

                    if next_page:
                        self.find_element_down(*RoleLocators.NEXT_PAGINATION)
                        self.find_role_key(details)

                    else:
                        raise Exception("Key not found")
                else:
                    return 1
            else:

                key = self.find_element(*RoleLocators.ITEM_KEY).text

                if key == details:
                    self.find_element(*RoleLocators.ITEM_BOX).click()
                    return 1
                else:
                    return 0
    
        self.sleeper(2)

    def validate_update_role_page(self):
        assert(self.find_element(*RoleLocators.UPDATE_ROLE_PAGE))

    def click_edit_role_btn(self):
        self.find_element_down(*RoleLocators.UPDATE_ROLE_BTN)
        self.sleeper(2)

    def click_submit_update_role(self):
        self.find_element(*RoleLocators.UPDATE_SUBMIT_BTN).click()
        self.sleeper(2)

    def unselect_role_permissions(self, count):

        BEFORE_SELECT_PERMISSION = RoleLocators.BEFORE_PERMISSION_PATH
        AFTER_SELECT_PERMISSION = RoleLocators.AFTER_PERMISSION_PATH

        self.uncheck_input_checked(BEFORE_SELECT_PERMISSION, AFTER_SELECT_PERMISSION, count)
        self.sleeper(2)
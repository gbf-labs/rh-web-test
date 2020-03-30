#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from library.locators import *
from .common import Page
import time


class UserPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_user_page(self):
        self.sleeper(20)
        try:

            self.find_element(*NavigationPageLocators.RBAC_DOWN).click()
            self.find_element(*NavigationPageLocators.USERS).click()
            self.sleeper(2)#WAIT TO SHOW PERMISSION TABLE

        except:
         
            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION

            self.find_element(*NavigationPageLocators.RBAC_DOWN).click()
            self.find_element(*NavigationPageLocators.USERS).click()

    def validate_user_page(self):
        assert(self.find_element(*UsersLocators.USERS_BREADCRUMB))
        print(*UsersLocators.USERS_BREADCRUMB)

    def validate_invite_user_page(self):
        assert(self.find_element(*UsersLocators.INVITE_USER))
    
    def validate_update_user_page(self):
        assert(self.find_element(*UsersLocators.UPDATE_USER))

    def click_invite_btn(self):
        self.find_element_down(*UsersLocators.INVITE_BTN)
        self.sleeper(2)

    def click_resend_invite_btn(self):
        self.find_element_down(*UsersLocators.RESEND_INVITE_BTN)
        self.find_element_down(*UsersLocators.CONFIRM_RESEND)
        self.sleeper(2)

    def click_edit_btn(self):
        self.find_element_down(*UsersLocators.EDIT_BTN)
        self.sleeper(2)

    def click_enable_btn(self):
        self.find_element_down(*UsersLocators.ENABLE_BTN)
        self.find_element_down(*UsersLocators.CONFIRM_ENABLE)
        self.sleeper(2)

    def click_disable_btn(self):
        self.find_element_down(*UsersLocators.DISABLE_BTN)
        self.find_element_down(*UsersLocators.CONFIRM_DISABLE)
        self.sleeper(2)

    def click_delete_btn(self):
        self.find_element_down(*UsersLocators.DELETE_BTN)
        self.find_element_down(*UsersLocators.CONFIRM_DELETE)
        self.sleeper(2)

    def find_user_key(self, details):

        # CHECK NUMBER OF ITEMS
        self.move_to_element(*UsersLocators.TOTAL_ITEMS)
        pagination = self.find_element(*UsersLocators.TOTAL_ITEMS).text
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
                BEFORE_XPATH_KEY = UsersLocators.BEFORE_XPATH_KEY
                AFTER_XPATH_KEY = UsersLocators.AFTER_XPATH_KEY
                AFTER_XPATH_CHECKBOX = UsersLocators.AFTER_XPATH_CHECKBOX

                find = self.find_dynamic_element(BEFORE_XPATH_KEY, AFTER_XPATH_KEY, 
                                            AFTER_XPATH_CHECKBOX, details, items)
                if not find:
                    next_page = self.check_button_enabled(*UsersLocators.NEXT_PAGINATION)

                    if next_page:
                        self.find_element_down(*UsersLocators.NEXT_PAGINATION)
                        self.find_user_key(details)

                    else:
                        raise Exception("Key not found")
                else:
                    return 1
            else:

                key = self.find_element(*UsersLocators.ITEM_KEY).text

                if key == details:
                    self.find_element(*UsersLocators.ITEM_BOX).click()
                    return 1
                else:
                    return 0

        self.sleeper(2)

    def enter_first_name(self, first_name):
        self.clear_input_field(*UsersLocators.INPUT_FIRST_NAME)
        self.find_element(*UsersLocators.INPUT_FIRST_NAME).send_keys(first_name)
    
    def enter_middle_name(self, middle_name):
        self.clear_input_field(*UsersLocators.INPUT_MIDDLE_NAME)
        self.find_element(*UsersLocators.INPUT_MIDDLE_NAME).send_keys(middle_name)

    def enter_last_name(self, last_name):
        self.clear_input_field(*UsersLocators.INPUT_LAST_NAME)
        self.find_element(*UsersLocators.INPUT_LAST_NAME).send_keys(last_name)

    def enter_email(self, email):
        self.clear_input_field(*UsersLocators.INPUT_EMAIL)
        self.find_element(*UsersLocators.INPUT_EMAIL).send_keys(email)

    def enter_user_company(self, details):
        self.clear_input_field(*UsersLocators.INPUT_COMPANY)
        self.find_element(*UsersLocators.INPUT_COMPANY).send_keys(details)
        self.tab(UsersLocators.SELECT_COMPANY)
        self.sleeper(2)

    def enter_user_role(self, details):
        self.clear_input_field(*UsersLocators.INPUT_ROLE)
        self.find_element(*UsersLocators.INPUT_ROLE).send_keys(details)
        self.tab(UsersLocators.SELECT_ROLE)
        self.sleeper(2)

    def allow_vpn_access(self, details, vessel):
        vessel_table = self.find_element_exist(*UsersLocators.VESSEL_TABLE)
        print(vessel_table)
 
        if vessel_table:
            BEFORE_XPATH_KEY = UsersLocators.BEFORE_XPATH_TABLE
            AFTER_XPATH_KEY = UsersLocators.AFTER_XPATH_TABLE
            AFTER_XPATH_TOG = UsersLocators.AFTER_XPATH_TOGGLE

            for i in range(1,4):
                print(i)

                after_path = "{0}{1}{2}".format(BEFORE_XPATH_KEY,i,AFTER_XPATH_KEY)
                input_path = "{0}{1}{2}".format(BEFORE_XPATH_KEY,i,AFTER_XPATH_TOG)
                print(after_path)

                #CLEAR FIRST
                element = self.browser.find_element_by_xpath(input_path)
                input_checked = element.get_property('checked')

                if input_checked:
                    self.browser.find_element_by_xpath(input_path).click()

                vessel_name = self.browser.find_element_by_xpath(after_path).text
                print(vessel_name)
                
                if vessel_name == vessel:
                    if details == "enable":
                        self.browser.find_element_by_xpath(input_path).click()
                        return 1
                else:
                    return 0
        else:
            return 0
        self.sleeper(2)

    def click_update_user_btn(self):
        self.find_element_down(*UsersLocators.UPDATE_USER_BTN)
        self.sleeper(2)

    def click_send_invite_btn(self):
        self.find_element_down(*UsersLocators.SEND_INVITE_BTN)
        self.sleeper(30)
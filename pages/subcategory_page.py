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

class SubCategoryPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_subcategory_page(self):
        self.sleeper(30)
        check_device_image = self.browser.find_elements_by_xpath("//*[contains(text(), 'Devices')]")
        print("----------------")
        print(check_device_image)
        try:
            print("Try")
            self.find_element(*NavigationPageLocators.ADMIN_DOWN).click()
            if check_device_image:
                self.find_element(*NavigationPageLocators.SUBCATEGORY).click()
            else:
                self.find_element(*NavigationPageLocators.ADMIN_DEVICES).click()
            self.sleeper(2)#WAIT TO SHOW ROLE TABLE

        except:
            print("Catch")
            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION
            self.find_element(*NavigationPageLocators.ADMIN_DOWN).click()
            if check_device_image:
                self.find_element(*NavigationPageLocators.SUBCATEGORY).click()
            else:
                self.find_element(*NavigationPageLocators.ADMIN_DEVICES).click()

    def validate_subcategory_page(self):
        assert(self.find_element(*SubCategoryLocators.SUBCATEGORY_BREADCRUMB))
        print(*SubCategoryLocators.SUBCATEGORY_BREADCRUMB)

    def validate_create_subcategory_page(self):
        assert(self.find_element(*SubCategoryLocators.CREATE_SUBCATEGORY_PAGE))

    def click_subcategory_btn(self):
        self.find_element_down(*SubCategoryLocators.CREATE_SUBCATEGORY_BTN)
        self.sleeper(2)

    def enter_subcategory_name(self, name):
        print("Name: ", name)
        self.clear_input_field(*SubCategoryLocators.INPUT_SUBCATEGORY_NAME)
        self.find_element(*SubCategoryLocators.INPUT_SUBCATEGORY_NAME).send_keys(name)

    def select_subcategory_options(self, details, process):
        if process == "update":
            self.find_element(*SubCategoryLocators.SELECT_OPTION_DELETE).click()
            self.find_element(*SubCategoryLocators.SELECT_OPTION).click()
        self.find_element(*SubCategoryLocators.SELECT_OPTION_AUTO).send_keys(details)
        self.sleeper(1)
        self.tab_xpath(*SubCategoryLocators.SELECT_OPTION_AUTO)
        self.sleeper(2)


    def click_submit_create_subcategory(self):
        self.find_element(*SubCategoryLocators.CREATE_SUBMIT_BTN).click()
        self.sleeper(2)

    def click_delete_subcategory_btn(self):
        self.find_element_down(*SubCategoryLocators.DELETE_SUBCATEORY_BTN)
        self.sleeper(2)

    def find_subcategory_key(self, details):
        
        # CHECK NUMBER OF ITEMS
        self.move_to_element(*SubCategoryLocators.TOTAL_ITEMS)
        pagination = self.find_element(*SubCategoryLocators.TOTAL_ITEMS).text
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
                BEFORE_XPATH_KEY = SubCategoryLocators.BEFORE_XPATH_KEY
                AFTER_XPATH_KEY = SubCategoryLocators.AFTER_XPATH_KEY
                AFTER_XPATH_CHECKBOX = SubCategoryLocators.AFTER_XPATH_CHECKBOX

                find = self.find_dynamic_element(BEFORE_XPATH_KEY, AFTER_XPATH_KEY, 
                                            AFTER_XPATH_CHECKBOX, details, items)
                if not find:
                    next_page = self.check_button_enabled(*SubCategoryLocators.NEXT_PAGINATION)

                    if next_page:
                        self.find_element_down(*SubCategoryLocators.NEXT_PAGINATION)
                        self.find_subcategory_key(details)

                    else:
                        raise Exception("Key not found")
                else:
                    return 1
            else:

                key = self.find_element(*SubCategoryLocators.ITEM_KEY).text

                if key == details:
                    self.find_element(*SubCategoryLocators.ITEM_BOX).click()
                    return 1
                else:
                    return 0
    
        self.sleeper(2)

    def validate_update_subcategory_page(self):
        assert(self.find_element(*SubCategoryLocators.UPDATE_SUBCATEGORY_PAGE))

    def click_edit_subcategory_btn(self):
        self.find_element_down(*SubCategoryLocators.UPDATE_SUBCATEGORY_BTN)
        self.sleeper(2)

    def click_submit_update_subcategory(self):
        self.find_element(*SubCategoryLocators.UPDATE_SUBMIT_BTN).click()
        self.sleeper(2)

    # def unselect_subcategory_permissions(self, count):

    #     BEFORE_SELECT_PERMISSION = SubCategoryLocators.BEFORE_PERMISSION_PATH
    #     AFTER_SELECT_PERMISSION = SubCategoryLocators.AFTER_PERMISSION_PATH

    #     self.uncheck_input_checked(BEFORE_SELECT_PERMISSION, AFTER_SELECT_PERMISSION, count)
    #     self.sleeper(2)
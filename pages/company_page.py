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

class CompanyPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_company_page(self):
        self.sleeper(20)
        try:

            self.find_element(*NavigationPageLocators.ADMIN_DOWN).click()
            self.find_element(*NavigationPageLocators.COMPANY).click()
            self.sleeper(2)#WAIT TO SHOW COMPANY TABLE

        except:
            
            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION

            self.find_element(*NavigationPageLocators.ADMIN_DOWN).click()
            self.find_element(*NavigationPageLocators.COMPANY).click()

    def validate_company_page(self):
        assert(self.find_element(*CompanyLocators.COMPANY_BREADCRUMB))

    def validate_create_company_page(self):
        assert(self.find_element(*CompanyLocators.CREATE_COMPANY_PAGE))

    def click_company_btn(self):

        self.find_element_down(*CompanyLocators.CREATE_COMPANY_BTN)
        self.sleeper(2)

    def enter_company_name(self, name):
        self.clear_input_field(*CompanyLocators.INPUT_COMPANY_NAME)
        self.find_element(*CompanyLocators.INPUT_COMPANY_NAME).send_keys(name)
        self.sleeper(2)
    
    def enter_company_vessel(self, details):
        self.clear_input_field(*CompanyLocators.INPUT_COMPANY_VESSEL)
        self.find_element(*CompanyLocators.INPUT_COMPANY_VESSEL).send_keys(details)
        self.tab(CompanyLocators.SELECT_COMPANY_VESSEL)
        self.sleeper(2)

    def click_submit_create_company(self):

        self.find_element(*CompanyLocators.CREATE_SUBMIT_BTN).click()
        self.sleeper(2)

    def click_delete_company_btn(self):
        self.find_element_down(*CompanyLocators.DELETE_COMPANY_BTN)
        self.sleeper(2)

    def find_company_key(self, details):
        # CHECK NUMBER OF ITEMS
        self.move_to_element(*CompanyLocators.TOTAL_ITEMS)
        pagination = self.find_element(*CompanyLocators.TOTAL_ITEMS).text
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
                BEFORE_XPATH_KEY = CompanyLocators.BEFORE_XPATH_KEY
                AFTER_XPATH_KEY = CompanyLocators.AFTER_XPATH_KEY
                AFTER_XPATH_CHECKBOX = CompanyLocators.AFTER_XPATH_CHECKBOX

                find = self.find_dynamic_element(BEFORE_XPATH_KEY, AFTER_XPATH_KEY, 
                                            AFTER_XPATH_CHECKBOX, details, items)
                if not find:
                    next_page = self.check_button_enabled(*CompanyLocators.NEXT_PAGINATION)

                    if next_page:
                        self.find_element_down(*CompanyLocators.NEXT_PAGINATION)
                        self.find_company_key(details)

                    else:
                        raise Exception("Key not found")
                else:
                    return 1
            else:

                key = self.find_element(*CompanyLocators.ITEM_KEY).text

                if key == details:
                    self.find_element(*CompanyLocators.ITEM_BOX).click()
                    return 1
                else:
                    return 0

        self.sleeper(2)


    def validate_update_company_page(self):
        assert(self.find_element(*CompanyLocators.UPDATE_COMPANY_PAGE))

    def click_edit_company_btn(self):
        self.find_element_down(*CompanyLocators.UPDATE_COMPANY_BTN)
        self.sleeper(2)

    def click_submit_update_company(self):
        self.find_element(*CompanyLocators.UPDATE_SUBMIT_BTN).click()
        self.sleeper(2)
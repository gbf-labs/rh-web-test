#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from library.locators import *
from .common import Page
import os
import time

# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class DeviceImagePage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_device_image_page(self):
        self.sleeper(30)
        try:
            print("Try")
            self.find_element(*NavigationPageLocators.ADMIN_DOWN).click()
            self.find_element(*NavigationPageLocators.ADMIN_DEVICES).click()
            self.sleeper(2)#WAIT TO SHOW ROLE TABLE

        except:
            print("Catch")
            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION
            self.find_element(*NavigationPageLocators.ADMIN_DOWN).click()
            self.find_element(*NavigationPageLocators.ADMIN_DEVICES).click()

    def find_vessel_key(self, vessel):
        vessel_tab = self.browser.find_elements_by_xpath("//*[contains(text(), '{0}')]".format(vessel))
        vessel_tab[0].click()
        self.sleeper(30)

    def find_device_image(self, vessel, device, transact):

        BEFORE_TABLE_KEY = DeviceImageLocators.BEFORE_TABLE_KEY
        AFTER_TABLE_KEY = DeviceImageLocators.AFTER_TABLE_KEY
        ROW_BEFORE = DeviceImageLocators.ROW_BEFORE_KEY
        ROW_AFTER = DeviceImageLocators.ROW_DEVICE_AFTER_KEY
        ROW_DELETE_UPLOAD = DeviceImageLocators.DELETE_UPLOAD
        ROW_ICON_UPLOAD = DeviceImageLocators.ROW_ICON_UPLOAD_KEY

        vessel_device_table = "{0}{1}{2}".format(BEFORE_TABLE_KEY, vessel, AFTER_TABLE_KEY)
        print("Vs: ", vessel_device_table)
        # print("-----")
        # print("{0}{1}".format(vessel_device_table, '/tr'))
        # tr = "{0}{1}".format(vessel_device_table, '/tr')
        # print("TR:", tr)
        # counter = self.browser.find_elements_by_xpath(tr)
        # count = len(counter)
        # print("Count:", count)
        # print("Test", self.find_element(*DeviceImageLocators.TEST))
        row = "{0}{1}".format(vessel_device_table, ROW_BEFORE)
        print("Row: ", row)
        for i in range(1, 3):

            input_path = "{0}{1}{2}".format(row,i,ROW_AFTER)
            delete_path = "{0}{1}{2}{3}".format(row,i,']/', ROW_DELETE_UPLOAD)
            upload_path = "{0}{1}{2}".format(row,i,ROW_ICON_UPLOAD)

            device_name = self.browser.find_element_by_xpath(input_path).text
 
            if device_name.upper() == device.upper():
                if transact == "delete":
                    self.delete_device_image(delete_path)
                else:
                    self.click_upload(upload_path)


    def delete_device_image(self, path):
        self.move_to_xpath_element(path)


    def confirm_delete_image(self):
        self.find_element(*DeviceImageLocators.DELETE_DEVICE_IMAGE).click()
        self.sleeper(10)

    def click_upload(self, path):
        self.browser.find_element_by_xpath(path).click()
        self.sleeper(10)
    
    def select_device_image(self):
        file_upload = os.path.abspath("uploads\\NMEA2.png")
        print("Path", file_upload)
        # file_upload = "{0}{1}".format(path,'\uploads\NMEA2.png')
        self.find_element(*DeviceImageLocators.UPLOAD_IMG).send_keys(file_upload)
        self.sleeper(10)

    def upload_device_image(self):
        # self.find_element(*DeviceImageLocators.UPLOAD_DEVICE_IMAGE_BUTTON)
        self.browser.find_element_by_css_selector('button.btn.btn-info').click()
        self.sleeper(10)
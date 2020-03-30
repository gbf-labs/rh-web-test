#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .common import Page
from library.locators import *
from selenium.webdriver.support.ui import WebDriverWait
import time

from selenium.webdriver.support.select import Select

# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class LoginPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_login_page(self, url):
        print(self.browser.current_url)

        print("URL", url)
        current_url = self.browser.current_url

        if current_url != 'data:,':
            if current_url != url:
                self.logout()

        self.browser.get(url)
    


    def enter_credentials(self,username,password):
        self.execute_element()
        try:
        
            self.find_element(*LoginPageLocators.USERNAME).send_keys(username)
            self.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
            self.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        except:
        
            return True 

    def logout(self):

        self.find_element_down(*LoginPageLocators.LOGOUT)
        return True
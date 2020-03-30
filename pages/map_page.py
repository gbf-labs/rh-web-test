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

class MapsPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)

    def visit_map_page(self):

        try:

            self.find_element(*NavigationPageLocators.MAPS).click()

        except:

            self.find_element(*NavigationPageLocators.NAVIGATION_BUTTON).click()
            self.sleeper(2)#WAIT TO SHOW THE NAVIGATION
            self.find_element(*NavigationPageLocators.MAPS).click()

        assert(self.find_element(*MapsLocators.MAPS_BREADCRUMB))

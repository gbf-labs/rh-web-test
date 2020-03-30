#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import gmail
import configparser
import os
import html2text
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from library.locators import *
from .common import Page
from library.config_parser import configSectionParser

#INIT CONFIG
config = configparser.ConfigParser()
config.read("config/config.cfg")

#CONFIG
receiver_email = configSectionParser(config,"RECEIVER")['email']
receiver_password = configSectionParser(config,"RECEIVER")['password']
sender_email = configSectionParser(config,"SENDER")['email']

class EmailPage(Page):

    def __init__(self, context):

        Page.__init__(self, context.browser)
        
    def login_gmail(self):
        email = gmail.login(receiver_email, receiver_password)

        if not email:
            return 0
        else:
            return 1

        
    def check_email_password(self, email_subject):
        # Check Email and Return Password
        self.sleeper(480)
        email = gmail.login(receiver_email, receiver_password)
        unread = email.inbox().mail(sender=sender_email, prefetch=True, unread=True)

        password = ""
        if len(unread) > 0:
        # while not password:
            for message in unread:
                sent_date = str(message.sent_at.date())
                current_date = str(date.today())
                print(".....................")
                print(message.sent_at)
                print(sent_date)
                print(current_date)
                print(message.subject)
                print(self.locate_password(message.body))
                print(".....................")
                if sent_date == current_date:
                    if message.subject == email_subject:
                        print(message.subject)
                        password = self.locate_password(message.body)
                        message.read()
                else:
                    pass

            # UNFORTUNATELY SPAM MAIL IS NOT WORKING
            # if password == "":
            #     password = self.check_spam(email_subject)
        return password

    def check_spam(self, email_subject):
        # Check Email and Return Password
        email = gmail.login(receiver_email, receiver_password)
        unread = email.spam().mail(sender=sender_email, prefetch=True, unread=True)

        password = ""
        if len(unread) > 0:

            for message in unread:
                date = message.sent_at
                print("-----------SPAM--------------")
                print(date.date())
                if date.date() == date.today():
                    if message.subject == email_subject:
                        password = self.locate_password(message.body)
            
        return password
    
    def locate_password(self, email_content):
        assert email_content, "Email Content is required."

        format_message = html2text.html2text(str(email_content, 'UTF8'))
        list_message = format_message.split()

        # Return next word or password
        password = list_message[list_message.index('password:') + 1]

        return password

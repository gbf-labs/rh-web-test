from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
import random
import string
import time

# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):
    def __init__(self, browser):
        self.browser = browser
        self.timeout = 30

    def find_element(self, *locator):
        print("Loc****", *locator)
        self.browser.implicitly_wait(10)
        return self.browser.find_element(*locator)

    def find_element_down(self, *locator):
        self.browser.implicitly_wait(10)
        element = self.find_element(*locator)
        target = ActionChains(self.browser).move_to_element(element).click()
        return target.perform()

    def execute_element(self):
        print("Iframe 123")

        tawk = self.browser.find_elements_by_tag_name("iframe")
        self.sleeper(5)
        # print(tawk)
        # for t in tawk:
        #     print(t.get_attribute('id'))
        tawk_id = 0
        if tawk:
            iframe_id = tawk[0].get_attribute('id')
            print("Iframe ID", iframe_id)
            iframe_path = '//*[@id="{0}"]'.format(iframe_id)

            iframe = self.browser.find_element_by_xpath(iframe_path)
            tawk_id = iframe.find_element_by_xpath('..')
            self.browser.execute_script("arguments[0].remove()", tawk_id)
        return tawk_id

    # def open(self,url):
    #     url = self.base_url + url
    #     self.browser.get(url)
        
    def get_title(self):
        return self.browser.title
        
    def get_url(self):
        return self.browser.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.browser).move_to_element(element)
        hover.perform()

    def generate_random_num_with_x_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    def generate_random_char(self, y):
        return ''.join(random.choice(string.lowercase) for x in range(y))

    def sleeper(self, seconds):
        time.sleep(seconds)

    def switch_to(self):
        self.browser.implicitly_wait(10)
        return self.browser.switch_to.alert

    def switch_to_new_window(self):
        window_after = self.browser.window_handles[1]
        self.browser.switch_to_window(window_after)

    def generate_random_time(self, start, stop):
        result = random.randrange(start, stop)
        if result < 10:
            result = "0" + str(result)
        return result

    def generate_random_days(self):
        result = random.randrange(1, 8)
        result = random.sample(range(7), result)
        return result

    def generate_random_sample(self,count):
        result = random.randrange(1, (count+1))
        result = random.sample(range(count), result)
        return result

    def find_element_exist(self, *locator):
        try:
            self.browser.implicitly_wait(10)
            self.browser.find_element(*locator)
            return True
        except:
            return False
        
    def find_dynamic_element(self,before_loc, after_key, after_loc, details, items):
        print("Find Table Key")
        for i in range(1, items+1):
            print(i)
            after_path = "{0}{1}{2}".format(before_loc,i,after_key)
            input_path = "{0}{1}{2}".format(before_loc,i,after_loc)
            print(after_path)

            inline_name = self.browser.find_element_by_xpath(after_path).text
            print(inline_name)

            if inline_name == details:
                self.browser.find_element_by_xpath(input_path).click()
                return 1
        return 0

    
    def check_button_enabled(self, *locator):
        self.browser.implicitly_wait(10)
        element = self.find_element(*locator)
        button = element.get_property('disabled')

        if button:
            return 0
        else:
            return 1

    def clear_input_field(self, *locator):
        self.browser.find_element(*locator).send_keys(Keys.HOME,(Keys.SHIFT + Keys.END))
        # self.browser.find_element(*locator).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*locator).send_keys(Keys.DELETE)

    def clear_dynamic(self,*locator):
        print("clear d")
        print(locator)
        self.browser.find_element(*locator).send_keys(Keys.DELETE)

    def tab(self, loc):
        print("---", loc)
        self.browser.find_element_by_xpath(loc).send_keys(Keys.TAB)

    def tab_xpath(self, *loc):
        print(loc[1])
        return self.browser.find_element_by_xpath(loc[1]).send_keys(Keys.TAB)

    def tab_alarm_xpath(self, *loc):
        print(loc[1])
        self.browser.find_element_by_xpath(loc[1]).send_keys(Keys.DOWN)
        return self.browser.find_element_by_xpath(loc[1]).send_keys(Keys.TAB)

    def select_list(self, before_loc, after_key, after_loc, details, count):

        for i in range(1, count+1):
            after_path = "{0}{1}{2}".format(before_loc,i,after_key)
            input_path = "{0}{1}{2}".format(before_loc,i,after_loc)

            select_name = self.browser.find_element_by_xpath(after_path).text
     
            if select_name == details:
                self.browser.find_element_by_xpath(input_path).click()
                self.tab(input_path)

                return 1
        return 0

    def count_permission(self, *locator):

        select = self.browser.find_element(*locator)
        items = select.find_elements_by_tag_name("li")
        return len(items)

    def uncheck_input_checked(self, before_loc, after_loc, count):

        for i in range(1, count+1):
            print(i)
            input_path = "{0}{1}{2}".format(before_loc,i,after_loc)
            element = self.browser.find_element_by_xpath(input_path)
            input_checked = element.get_property('checked')

            if input_checked:
                self.browser.find_element_by_xpath(input_path).click()
                self.tab(input_path)
                return 1
        return 0

    
    def find_toggle(self, locator, enable):
        print("Toggle---->", locator)
        print("Toggle---->", locator[1])
        print("Enable", enable)

        #CLEAR FIRST
        element = self.browser.find_element_by_xpath(locator[1])
        input_checked = element.get_property('checked')

        if input_checked:
            self.browser.find_element_by_xpath(locator[1]).click()

        if enable == "enable":
            return  self.browser.find_element_by_xpath(locator[1]).click()
        else:
            return 1

    def move_to_element(self, *locator):
        self.browser.implicitly_wait(10)
        element = self.find_element(*locator)
        target = ActionChains(self.browser).move_to_element(element)
        return target.perform()

    def move_to_xpath_element(self, loc):
        self.browser.implicitly_wait(5)
        element = self.browser.find_element_by_xpath(loc)
        target = ActionChains(self.browser).move_to_element(element).click()
        return target.perform()
from sys import platform as _platform

from selenium import webdriver
import sys, traceback
from datetime import datetime

def before_all (context):

    driver = ""

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    #options.add_argument('--disable-gpu')

    if _platform == "linux" or _platform == "linux2":
        options.add_argument("--headless")
        options.add_argument("window-size=1280,800")
        driver = "./drivers/linux/chromedriver"

    elif _platform == "darwin":
        options.add_argument("--kiosk")
        driver = "./drivers/mac/chromedriver"

    elif _platform == "win32":
        # Windows
        options.add_argument("--kiosk")
        options.add_argument("window-size=1280,800")
        driver = './drivers/windows/chromedriver.exe'

    elif _platform == "win64":
        # Windows 64-bit
        options.add_argument("--kiosk")
        driver = './drivers/windows/chromedriver.exe'

    context.browser = webdriver.Chrome(chrome_options=options, executable_path=driver)

def after_all(context):

    context.browser.quit()

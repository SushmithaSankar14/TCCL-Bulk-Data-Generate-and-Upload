from lib2to3.pgen2 import driver
from behave import given, when, then

from requests import options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import logging
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.pages.customer_page import CustomerPage
from utils.data import Add_Customer
from features.pages.stb_page import stbPage
from selenium.webdriver.remote.webelement import WebElement

from utils.config_reader import ConfigReader
import os
import time
from utils.locators import *
import autoit


config_reader = ConfigReader()


@then("After login Click STB Module")
def steps_After_login_click_STB_Module(context):
    context.stb_page.clicksTBModule_page(context, "STB menu")


@then("add New Stb")
def steps_add_new_stb(context):
    context.stb_page.add_STB(context)
    context.stb_page.select_Server_Type(context, "Sumavision")
    context.stb_page.chip_ID(context)
    context.stb_page.cas_ID(context)
    context.stb_page.select_Model(context)
    context.stb_page.select_STB_Type(context)
    context.stb_page.stb_Submit(context)
    context.stb_page.back_Stb_List(context)

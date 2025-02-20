from lib2to3.pgen2 import driver
from behave import given, when, then
from requests import options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from selenium.webdriver.remote.webelement import WebElement
from utils.config_reader import ConfigReader
import os
import time
from utils.locators import *
from features.pages.stb_Menu_page import stbPageMenu
from selenium.webdriver.common.action_chains import ActionChains


import autoit

config_reader = ConfigReader()


@then("Verify STB BredCrumb")
def steps_Verify_stb_bredcrumb(context):
    context.stb_Menu_page.stb_BreadCrumb(context)
    context.stb_Menu_page.stbList_Table(context)


# @then("Click Create STB")
# def stpes_create_stb(context):
#     context.stb_Menu_page.steps_click_create_stb(context, "Create STB")
#     context.stb_Menu_page.click_new_stb(context)
#     context.stb_Menu_page.bulk_upload_stb(context)


@then("Verify Stb BulkOperations")
def step_then(context):
    context.stb_Menu_page.click_stb_BulkOperations(
        context, "Bulk Operations")
    context.stb_Menu_page.uploadLog_BredCrumb(context)
    context.stb_Menu_page.stbUploadLog_Table(context)


@then('Verify Stb VCPairing')
def step_then(context):
    context.stb_Menu_page.click_stb_VCPairing(
        context, "STB VC Pairing/Unpairing")
    context.stb_Menu_page.vcPairing_BredCrumb(context)
    context.stb_Menu_page.stbVCPairing_Table(context)

    time.sleep(5)

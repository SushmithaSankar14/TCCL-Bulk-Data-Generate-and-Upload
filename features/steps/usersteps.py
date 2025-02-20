from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import logging
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.pages.users_page import UsersPage
from utils.config_reader import ConfigReader
import os
import time
from utils.locators import *



config_reader = ConfigReader()

# @given("Launch browser")
# def stepLaunchbrowser(context):
#     context.env = os.getenv("ENV")
#     print(context.env)

# @then("user move to tccl url")
# def steps_user_naviagtes_to_tccl_SMS_loginPage(context):
#     context.login_page.naviagte_to_tccl_SMS_login(
#         context, config_reader.get_tccl_SMS_URL(context.env)
#     )

@then("After login Click Users Module")
def steps_enter_continueBtn_for_SMS_user(context):
    context.users_page.users_list_page(context)
    
@then("Click download Users list PDF icon")
def steps_click_download_userlist_pdf (context):
    context.login_page.click_userlistpdf(context)  


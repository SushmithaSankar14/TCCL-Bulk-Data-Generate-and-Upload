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
from features.actions.broadcasterCreateActions import BroadcasterCreateActions
from utils.data import Add_Customer
from selenium.webdriver.remote.webelement import WebElement

from utils.config_reader import ConfigReader
import os
import time
from utils.locators import *
import autoit


config_reader = ConfigReader()


@then("move to channels")
def steps_move_to_channels(context):
    context.broadcasterList_page.moveToChannels(context)


@then("move to broadcasterList in channels module")
def steps_move_to_broadcasterList_in_Channels(context):
    context.broadcasterList_page.moveToBroadcasterList(context)


@then("click create broadcaster button")
def steps_click_create_broadcaster_button(context):
    context.broadcasterList_page.clickCreateBroadcasterBtn(context)


@then("enter all the fields with valid data")
def steps_to_entervalid_data_in_the_broadcasterCreation(context):
    context.broadcasterList_page.enterBroadcasterName(
        context, BroadcasterCreateActions.generateRandomBroadcasterName()
    )
    context.broadcasterList_page.enterContactName(
        context, BroadcasterCreateActions.generateContactName()
    )
    context.broadcasterList_page.enterBroadcasterMobileNumber(context, "8610980828")
    context.broadcasterList_page.enterContactPhoneNumber(context, "8610980828")
    context.broadcasterList_page.enterEmail(context, "automation@gmail.com")
    context.broadcasterList_page.enterAddress1(context, "Test address 1")
    context.broadcasterList_page.enterAddress2(context, "Test address 2")
    context.broadcasterList_page.enterAddress3(context, "Test address 3")
    context.broadcasterList_page.enterCity(context, "Chennai")
    context.broadcasterList_page.enterPin(context, "600017")
    time.sleep(2)
    context.broadcasterList_page.enterDistrict(context, "Chennai")
    context.broadcasterList_page.enterState(context, "Tamil nadu")
    context.broadcasterList_page.enterCountry(context, "India")
    time.sleep(1)


@then("click create button when enabled for broadcaster creation")
def steps_to_click_create_enabled_broadcasterCreation(context):
    context.broadcasterList_page.clickCreate(context)
    time.sleep(3)


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
from selenium.webdriver.remote.webelement import WebElement

from utils.config_reader import ConfigReader
import os
import time
from utils.locators import *
import autoit


config_reader = ConfigReader()


@then("After login Click Customer Module")
def steps_After_login_click_Customer_Module(context):
    context.customer_page.CustomerModule_page(context)


@then('Add New Customer')
def steps_Add_New_Customer(context):
    context.customer_page.AddNew_Customer(context)


@given('User Details')
def steps_User_Details(context):
    context.customer_page.selectPrefix(context, "Mr")
    context.customer_page.Customer_First_Name(context)
    context.customer_page.Customer_Last_Name(context)
    context.customer_page.cutomer_Gender(context, "Female")
    context.customer_page.cutomer_LCO(
        context, "AbiramiDistributorKannanSubDistributor08360797689794 - Test LCO User")
    context.customer_page.cutomer_Type(context, "Hotel")
    context.customer_page.billing_Type(context, "Prepaid")
    context.customer_page.sLA(context, "Standard")
    context.customer_page.Customer_User_Name(context)
    context.customer_page.customer_Password(context)
    context.customer_page.Customer_Address_Line1(context)
    context.customer_page.Customer_Address_Line2(context)
    context.customer_page.customer_PinCode(context)
    context.customer_page.customer_City(context)
    context.customer_page.customer_Mobile_Number(context)
    context.customer_page.next_Arrow(context)
    context.customer_page.customer_ID_Type(context, "PAN")
    context.customer_page.customer_ID_Number(context)
    # Define folderPath and fileName
    folderPath = "\\features\\utils\\files\\"
    fileName = "exported-image (1).png"
    context.customer_page.customer_ID_Proof_Upload(
        context, folderPath, fileName)
    context.customer_page.customer_Details_saved(context)
    time.sleep(10)

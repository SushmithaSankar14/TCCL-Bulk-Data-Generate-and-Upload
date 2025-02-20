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
from utils.data import payment_data
from selenium.webdriver.remote.webelement import WebElement
from features.pages.payments_page import paymentPage
from utils.config_reader import ConfigReader
import os
import time
from utils.locators import *
import autoit


config_reader = ConfigReader()


@then("After Click Payments Module")
def steps_Affter_Click_Payments_Module(context):
    context.payments_page.clickPaymentModule_page(context, "payment")
    context.payments_page.clickSubMenu_Individual_LCO_Deposit(
        context, "Individual LCO Deposit")
    context.payments_page.selectUserType(
        context, "LCO")
    context.payments_page.selectBusinessName(
        context, "AutomationLCO")
    context.payments_page.clickApplyBtn(context)
    context.payments_page.clickWalletImg(context)
    context.payments_page.enterAmount(
        context, payment_data.amount)
    context.payments_page.selectPaymentMode(
        context, "Cash")
    context.payments_page.enterRecipteNo(
        context, payment_data.ReceiptNo)
    context.payments_page.enterRemarks(
        context, payment_data.remarks)
    context.payments_page.clickDepositBtn(context)
    context.payments_page.clickAfterMoneyDeposit(context)

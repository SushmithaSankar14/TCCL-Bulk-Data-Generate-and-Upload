from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import logging
from features.pages.base_page import BasePage
from features.pages.customer_page import CustomerPage
from features.pages.login_page import LoginPage
from features.pages.payments_page import paymentPage
from features.pages.stb_Menu_page import stbPageMenu
from features.pages.stb_page import stbPage
from features.pages.users_page import UsersPage
from features.pages.broadcasterList_page import BroadcasterListPage
from features.pages.bulkdatagenerate_page import BulkDataGenerator
from features.pages.bulkupload_page import bulkUpload
from features.pages.subscriberBulkCreate_page import bulkUploadSubscriberCreatePage
from features.pages.bulkTestAPI_page import APIrsponseCheck
from features.pages.STB_Search_page import SearchPage
from features.pages.transferSTB_page import transferSTBVerifyPage
from features.pages.bulkproductcreate_page import bulkProductPage
from features.pages.ProductVerification_page import productVerification
from utils.config_reader import ConfigReader
import os
import time
from utils.locators import *
from features.pages.subscriberID_search_page import subscriberIDVerifyPage

config_reader = ConfigReader()


@given("Launch browser")
def step(context):
    context.logger = logging.getLogger()
    # chromeDriver_install
    context.logger = logging.getLogger()
    context.env = os.getenv("ENV")
    try:
        try:
            old_Chrome_driver_path = ChromeDriverManager().install()
            # Create the new file path by replacing 'THIRD_PARTY_NOTICES.chromedriver' with 'chromedriver.exe'
            Chrome_driver_path = old_Chrome_driver_path.replace(
                'THIRD_PARTY_NOTICES.chromedriver', 'chromedriver.exe')

            context.logger.info(
                "Try to get the path of the Chrome driver executable without downloading it again"
            )
        except:
            # If the driver is not already installed, download and install it
            old_Chrome_driver_path = ChromeDriverManager().install()
            # Create the new file path by replacing 'THIRD_PARTY_NOTICES.chromedriver' with 'chromedriver.exe'
            Chrome_driver_path = old_Chrome_driver_path.replace(
                'THIRD_PARTY_NOTICES.chromedriver', 'chromedriver.exe')

            context.logger.info(
                "If the driver is not already installed, download and install it"
            )

        # Create a Service instance using the Firefox driver executable path
        s = Service(executable_path=Chrome_driver_path)
        context.logger.info(
            "Create a Service instance using the Chrome driver executable path"
        )

        # Create a Firefox webdriver instance using the Service
        context.driver = webdriver.Chrome(service=s)

        context.driver.maximize_window()
    except:
        try:
            old_Chrome_driver_path = ChromeDriverManager().install()
            # Create the new file path by replacing 'THIRD_PARTY_NOTICES.chromedriver' with 'chromedriver.exe'
            Chrome_driver_path = old_Chrome_driver_path.replace(
                'THIRD_PARTY_NOTICES.chromedriver', 'chromedriver.exe')
            context.logger.info(
                "Try to get the path of the Chrome driver executable without downloading it again"
            )
        except:
            # If the driver is not already installed, download and install it
            old_Chrome_driver_path = ChromeDriverManager().install()
            # Create the new file path by replacing 'THIRD_PARTY_NOTICES.chromedriver' with 'chromedriver.exe'
            Chrome_driver_path = old_Chrome_driver_path.replace(
                'THIRD_PARTY_NOTICES.chromedriver', 'chromedriver.exe')
            print("If the driver is not already installed, download and install it")
            context.logger.info(
                "If the driver is not already installed, download and install it"
            )

        # Create a Service instance using the Firefox driver executable path
        s = Service(executable_path=Chrome_driver_path)
        context.logger.info(
            "Create a Service instance using the Chrome driver executable path"
        )

        # Create a Firefox webdriver instance using the Service
        context.driver = webdriver.Chrome(service=s)

        context.driver.maximize_window()

    # Set the zoom level to 80%
    context.driver.execute_script("document.body.style.zoom='80%'")

    context.waitdriver = WebDriverWait(context.driver, 30)
    context.filterWaitdriver = WebDriverWait(context.driver, 5)
    # context.waitdriver = WebDriverWait(context.driver, 75)
    context.action = ActionChains(context.driver)
    context.waitForDeleteConfirmation = WebDriverWait(context.driver, 5)

    context.logger.info("Driver Configuration setup successfully completed")

    # driver config
    createObjForCurrentPages(context)

    context.logger.info("Page object created")


def createObjForCurrentPages(context):
    context.login_page = LoginPage()
    context.BasePage = BasePage()
    context.users_page = UsersPage()
    context.customer_page = CustomerPage()
    context.stb_page = stbPage()
    context.broadcasterList_page = BroadcasterListPage()
    context.stb_Menu_page = stbPageMenu()
    context.payments_page = paymentPage()
    context.bulkdatagenerate_page = BulkDataGenerator()
    context.bulkupload_page = bulkUpload()
    context.subscriberBulkCreate_page = bulkUploadSubscriberCreatePage()
    context.api_response_check = APIrsponseCheck()
    context.STB_Search_page = SearchPage()
    context.transferSTB_page = transferSTBVerifyPage()
    context.subscriberID_search_page = subscriberIDVerifyPage()
    context.bulkproductcreate_page = bulkProductPage()
    context.ProductVerification_page = productVerification()


@given("the user is on the login page")
def step_given_user_on_login_page(context):
    context.browser.get("https://example.com/login")


@then("Quit browser")
def step_quit_browser(context):
    context.driver.quit()


@when("the user navigates to TCCL SMS login page")
def steps_user_naviagtes_to_tccl_SMS_loginPage(context):
    context.login_page.naviagte_to_tccl_SMS_login(
        context, config_reader.get_tccl_SMS_URL(context.env)
    )


@then("Enter userName and password")
def steps_enter_userName_and_password(context):
    print("steps_enter_userName_and_password")
    context.login_page.enter_UserName_and_Password(
        context,
        config_reader.get_tccl_SMS_UserName(context.env),
        config_reader.get_tccl_SMS_Password(context.env),
        config_reader,
    )


@then("Click continue button for SMS User Login")
def steps_enter_continueBtn_for_SMS_user(context):
    context.login_page.click_continueBtn(context)


# @then("After login Click Users Module")
# def steps_enter_continue_for_SMS_user(context):
#     context.login_page.click_continueBtn(context)

import time
from utils.locators import *
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import Select
from features.actions.bulkuUploadActions import bulkuploadAction
from multiprocessing import context
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains

from features.actions.bulkuUploadActions import bulkuploadAction
from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage

import os


class bulkUploadSubscriberCreatePage(BasePage):
    def __init__(self):
        # self.driver = driver
        super().__init__()
    context.logger = logging.getLogger()

    # subscriberBulk

    def click_subscriber_Menu(self, context, value):
        bulkuploadAction.clickMenuList(
            context, value)
        # assert breadcrumb text
        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")
        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Subscriber List"
        ), f"Expected 'Subscriber List' but got '{breadcrumb_text}'"
        print("Subscriber List")

    def click_subscriber_bulkOperations(self, context, value):
        bulkuploadAction.click_submenu_list(context, value)
        # assert breadcrumb text
        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")
        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Subscriber Bulk Operations"
        ), f"Expected 'Subscriber Bulk Operations' but got '{breadcrumb_text}'"
        print("Subscriber Bulk Operations")

    def create_bulk_subscriber(self, context, value):
        bulkuploadAction.selectValueFromList(
            context, bulkOperations_Locators.action_Types,
            bulkOperations_Locators.action_Types_List, value, "Create"
        )

    def upload_CreateSubscriber_bulk_file(self, context):
        file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/subscriber_data.csv"


        bulkuploadAction.upload_file(self, context, file_path)
        bulkuploadAction.click_refresh_Btn(self, context)
        bulkuploadAction.assert_process_counts(self, context)

        print("Subscriber Created Successfully")

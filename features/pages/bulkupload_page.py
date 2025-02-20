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
from selenium.common.exceptions import StaleElementReferenceException


from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage

import os


class bulkUpload(BasePage):
    def __init__(self):
        # self.driver = driver
        super().__init__()
    context.logger = logging.getLogger()

    def steps_click_create_stb(self, context, value):

        bulkuploadAction.click_submenu_list(context, value)

        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")

        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Create STB Logs"
        ), f"Expected 'Create STB Logs' but got '{breadcrumb_text}'"
        print("Create STB")

        # verify pdf and csv files

        pdf_file = self.findElementByXpath(
            context, stbMenu_Locators.pdf_icon)
        print("pdf file is displayed")

        csv_file = self.findElementByXpath(
            context, stbMenu_Locators.csv_icon)
        print("csv file is displayed")

    def click_new_stb(self, context):
        click_STB = self.findElementByXpath(
            context, stbMenu_Locators.new_stb)
        click_STB.click()

        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")

        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Create STB - Individual"
        ), f"Expected 'Create STB - Individual' but got '{breadcrumb_text}'"
        print("Create STB - Individual")

        # click bulk stb

        click_bulk_stb = self.findElementByXpath(
            context, stbMenu_Locators.bulk_Button)
        click_bulk_stb.click()

        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")

        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Create STB - Bulk"
        ), f"Expected 'Create STB - Bulk' but got '{breadcrumb_text}'"
        print("Create STB - Bulk")

        # assert bulkstb upload log table

        bulkuploadlogstbTable = self.findElementByXpath(
            context, stbMenu_Locators.bulkstb_uploadlof_table
        )

        context.logger.info(f"StbList:'{bulkuploadlogstbTable}'")

        firstValueofTable = self.findElementByXpath(
            context, stbMenu_Locators.firstvaluof_bulk_uploadlog_table
        )
        # or firstValueofTable.get_attribute('attribute_name') if you're looking for a specific attribute
        TransactionID = firstValueofTable.text
        context.logger.info(f"TransactionID: '{TransactionID}'")

    def bulk_upload_stb(self, context):
        file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/main_data.csv"
        # D: \Automation\tccl-sms\TestAutomation-SMS\TestAutomation-SMS\features\files\main_data.csv
        # # Call upload_file with only the required arguments
        bulkuploadAction.upload_file(self, context, file_path)
    def after_upload_verify(self,context):
        bulkuploadAction.click_refresh_Btn(self, context)
        bulkuploadAction.assert_process_counts(self, context)

        # TransactionID Return from the table
        TransactionID = self.findElementByXpath(
            context, stbMenu_Locators.transactionIDLogs_Locator)

        transactionID_Text = TransactionID.text

        context.logger.info(f"TransactionID: '{transactionID_Text}'")

        return transactionID_Text

    # def bulk_upload_stb(self, context):
    #     file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/main_data.csv"
    #     # D: \Automation\tccl-sms\TestAutomation-SMS\TestAutomation-SMS\features\files\main_data.csv
    #     # # Call upload_file with only the required arguments
    #     bulkuploadAction.upload_file(self, context, file_path)
    #     bulkuploadAction.click_refresh_Btn(self, context)
    #     bulkuploadAction.assert_process_counts(self, context)

    #     # TransactionID Return from the table
    #     TransactionID = self.findElementByXpath(
    #         context, stbMenu_Locators.transactionIDLogs_Locator)

    #     transactionID_Text = TransactionID.text

    #     context.logger.info(f"TransactionID: '{transactionID_Text}'")

    #     return transactionID_Text

        # after upload file search that stb
        # bulkuploadAction.click_submenu_list(context, "Create STB")
        # bulkuploadAction.search_stb(self, context)

    # Trasfer data upload

    def bulkupload_transfer_stb(self, context, value):
        bulkuploadAction.click_submenu_list(context, value)

        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")

        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Stb Transfer Logs"
        ), f"Expected 'Stb Transfer Logs' but got '{breadcrumb_text}'"
        print("Stb Transfer")

        # verify pdf and csv files

        pdf_file = self.findElementByXpath(
            context, transfer_STB_Locators.pdf_icon)
        print("pdf file is displayed")

        csv_file = self.findElementByXpath(
            context, transfer_STB_Locators.csv_icon)
        print("csv file is displayed")

    def click_new_transfer_stb(self, context):
        click_transfer_STB = self.findElementByXpath(
            context, transfer_STB_Locators.Stb_new_transfer)
        click_transfer_STB.click()

        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")

        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Stb Transfer - Bulk"
        ), f"Expected 'Stb Transfer - Bulk' but got '{breadcrumb_text}'"
        print("Stb transfer Bulk")

    def bulk_upload_stb_transfer(self, context):
        file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/transfer_data.csv"


        bulkuploadAction.upload_file(self, context, file_path)
        bulkuploadAction.click_refresh_Btn(self, context)
        bulkuploadAction.assert_process_counts(self, context)
        # TransactionID Return from the table
        TransactionID = self.findElementByXpath(
            context, stbMenu_Locators.transactionIDLogs_Locator)

        transactionID_Text = TransactionID.text

        context.logger.info(f"TransactionID: '{transactionID_Text}'")

        return transactionID_Text

    def upload_activation_data_file(self, context, value):
        bulkuploadAction.selectValueFromList(
            context, bulkOperations_Locators.action_Types,
            bulkOperations_Locators.action_Types_List, value, "Activation"
        )

    def choose_reason_Activate(self, context, value):
        bulkuploadAction.selectValueFromList(
            context, bulkOperations_Locators.reason,
            bulkOperations_Locators.reason_List, value, "Activation Pack Change"
        )

    def bulk_upload_stb_Activation(self, context):
        file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/features/files/activate_data.csv"

        bulkuploadAction.upload_file(self, context, file_path)
        bulkuploadAction.click_refersh_Btn(self, context)
        bulkuploadAction.assert_process_counts(self, context)
        # bulkuploadAction.upload_file(
        #     context=context,
        #     file_path=file_path,
        #     upload_button_locator=stbMenu_Locators.upload_stb_file,
        #     file_input_locator="//input[@id='fileInput']",
        #     import_button_locator=stbMenu_Locators.import_button,
        #     success_msg_locator=stbMenu_Locators.file_uploded_success_msg
        # )
        print("activation Successfully completed")

    # Deactivation

    def upload_Deactive_data_file(self, context, value):
        bulkuploadAction.selectValueFromList(
            context, bulkOperations_Locators.action_Types,
            bulkOperations_Locators.action_Types_List, value, "Deactivation"
        )

    def choose_reason_Deactivate(self, context, value):
        bulkuploadAction.selectValueFromList(
            context, bulkOperations_Locators.reason,
            bulkOperations_Locators.reason_List, value, "Temporary Deactivation"
        )

    def bulk_upload_stb_Deactivation(self, context):
        file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/features/files/activate_data.csv"

        bulkuploadAction.upload_file(self, context, file_path)
        bulkuploadAction.click_refresh_Btn(self, context)
        bulkuploadAction.assert_process_counts(self, context)
        # bulkuploadAction.upload_file(
        #     context=context,
        #     file_path=file_path,
        #     upload_button_locator=stbMenu_Locators.upload_stb_file,
        #     file_input_locator="//input[@id='fileInput']",
        #     import_button_locator=stbMenu_Locators.import_button,
        #     success_msg_locator=stbMenu_Locators.file_uploded_success_msg
        # )
        print("Deactivation Successfully completed")

        # reactivation

    def upload_reactivate_data_file(self, context, value):
        bulkuploadAction.selectValueFromList(
            context, bulkOperations_Locators.action_Types,
            bulkOperations_Locators.action_Types_List, value, "Reactivation"
        )

    def choose_reason_Reactivate(self, context, value):
        bulkuploadAction.selectValueFromList(
            context, bulkOperations_Locators.reason,
            bulkOperations_Locators.reason_List, value, "Activation Pack Change"
        )

    def bulk_upload_stb_Reactivation(self, context):
        file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/features/files/reactivate_data.csv"

        bulkuploadAction.upload_file(self, context, file_path)
        bulkuploadAction.click_refresh_Btn(self, context)
        bulkuploadAction.assert_process_counts(self, context)
        # bulkuploadAction.upload_file(
        #     context=context,
        #     file_path=file_path,
        #     upload_button_locator=stbMenu_Locators.upload_stb_file,
        #     file_input_locator="//input[@id='fileInput']",
        #     import_button_locator=stbMenu_Locators.import_button,
        #     success_msg_locator=stbMenu_Locators.file_uploded_success_msg
        # )
        print("Reactivation Successfully completed")

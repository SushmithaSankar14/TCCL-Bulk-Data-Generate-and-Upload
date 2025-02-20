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
from features.utils.ProductLocators import ProductLocators
from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage
import os


class bulkProductPage(BasePage):
    def __init__(self):
        # self.driver = driver
        super().__init__()
    context.logger = logging.getLogger()

    def click_products_menu(self,context,value):
        bulkuploadAction.clickMenuList(
            context, value)
        # assert breadcrumb text
        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")
        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Home"
        ), f"Expected 'Home' but got '{breadcrumb_text}'"
        print("Home")
    # def create_bulk_subscriber(self, context, value):
    #     bulkuploadAction.selectValueFromList(
    #         context, bulkOperations_Locators.action_Types,
    #         bulkOperations_Locators.action_Types_List, value, "Create"
    #     )
    def click_add_product(self, context):
        click_STB = self.findElementByXpath(
            context, ProductLocators.add_Product)
        click_STB.click()

        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")

        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Add Product Individual"
        ), f"Expected 'Add Product Individual' but got '{breadcrumb_text}'"
        print("Add Product Individual")

        # click bulk stb

        click_bulk_stb = self.findElementByXpath(
            context, ProductLocators.bulk_Button)
        click_bulk_stb.click()

        breadcrumb_text = bulkuploadAction.breadcrumb_validation(self, context)
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")

        # Assert that the text matches the expected values
        assert (
            breadcrumb_text == "Add Product Bulk"
        ), f"Expected 'Add Product Bulk' but got '{breadcrumb_text}'"
        print("Add Product Bulk")

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
    def create_bulk_product(self, context, value):
        bulkuploadAction.selectValueFromList(
            context, ProductLocators.server_types,
            ProductLocators.server_type_List, value,"Sumavision"
        )
        # bulkuploadAction.selectValueFromList(
        #     context, bulkOperations_Locators.action_Types,
        #     bulkOperations_Locators.action_Types_List, value, "Sumavision"
        # )

    def upload_Product_bulk_file(self, context):
        file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/product_create_data.csv"


        bulkuploadAction.upload_file(self, context, file_path)
        bulkuploadAction.click_refresh_Btn(self, context)
        bulkuploadAction.product_assert_process_counts(self, context)

        print("Product Created Successfully")




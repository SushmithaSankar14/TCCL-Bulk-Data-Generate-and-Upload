import time
from utils.locators import *
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import Select
from features.actions.stbMenuActions import stbMenuListAction
from multiprocessing import context
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains

# from features.utils import stbMenu_Locators
from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage

import os


class stbPageMenu(BasePage):
    def __init__(self):
        # self.driver = driver
        super().__init__()
    context.logger = logging.getLogger()

    def stb_BreadCrumb(self, context):
        # Locate the breadcrumb elements
        stbList_BreadCrumb = self.findElementByXpath(
            context, stbMenu_Locators.STB_BredCrumb
        )
        # Get the text from the located elements
        STBList_text = stbList_BreadCrumb.text
        context.logger.info(f"Retrieved breadcrumb text: '{STBList_text}'")

        # Assert that the text matches the expected values
        assert (
            STBList_text == "STB List"
        ), f"Expected 'STB List' but got '{STBList_text}'"

    def stbList_Table(self, context):

        stbListTable = self.findElementByXpath(
            context, stbMenu_Locators.STB_Table
        )

        context.logger.info(f"StbList:'{stbListTable}'")

        firstValueofTable = self.findElementByXpath(
            context, stbMenu_Locators.STBList_FirstValueChipID
        )
        # or firstValueofTable.get_attribute('attribute_name') if you're looking for a specific attribute
        chipID = firstValueofTable.text
        context.logger.info(f"ChipID: '{chipID}'")

    def click_stb_BulkOperations(self, context, value):

        stbMenuListAction.click_submenu_list(
            context, value)

    def uploadLog_BredCrumb(self, context):

        uploadLog_BredCrumb = self.findElementByXpath(
            context, stbMenu_Locators.STB_Uploadlog_BredCrumb
        )
        UploadLog_text = uploadLog_BredCrumb.text
        context.logger.info(f"Retrieved breadcrumb text: '{UploadLog_text}'")

        # Assert that the text matches the expected values
        assert (
            UploadLog_text == "Upload Log"
        ), f"Expected 'Upload Log' but got '{UploadLog_text}'"

    def stbUploadLog_Table(self, context):

        uploadLogTable = self.findElementByXpath(
            context, stbMenu_Locators.UploadLog_Table
        )

        context.logger.info(f"UploadLogTable:'{uploadLogTable}'")

        firstValueofTable = self.findElementByXpath(
            context, stbMenu_Locators.FirstValue_TransactionID
        )
        # or firstValueofTable.get_attribute('attribute_name') if you're looking for a specific attribute
        TransactionID = firstValueofTable.text
        context.logger.info(f"TransactionID: '{TransactionID}'")

    def click_stb_VCPairing(self, context, value):

        stbMenuListAction.click_submenu_list(
            context, value)

    def vcPairing_BredCrumb(self, context):

        vcPairing_BredCrumb = self.findElementByXpath(
            context, stbMenu_Locators.STB_VCPairing_BredCrumb
        )
        STBVcPairing_text = vcPairing_BredCrumb.text
        context.logger.info(f"Retrieved breadcrumb text:'{STBVcPairing_text}'")

        # Assert that the text matches the expected values

        assert (
            STBVcPairing_text == "STB Vc Pairing Log"
        ), f"Expected 'STB Vc Pairing Log' but got '{STBVcPairing_text}'"

    def stbVCPairing_Table(self, context):

        stbVCPairingTable = self.findElementByXpath(
            context, stbMenu_Locators.STB_VCPairing_Table
        )

        context.logger.info(f"VCPairingtable:'{stbVCPairingTable}'")

        firstValueofTable = self.findElementByXpath(
            context, stbMenu_Locators.STBVCPairing_FirstValueChipID
        )
        # or firstValueofTable.get_attribute('attribute_name') if you're looking for a specific attribute
        ChipID = firstValueofTable.text
        context.logger.info(f"ChipID: '{ChipID}'")

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
from features.pages.bulkupload_page import bulkUpload


from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage

import os
import csv


class SearchPage(BasePage):

    def __init__(self):
        # self.driver = driver
        super().__init__()
    context.logger = logging.getLogger()


    def get_serial_numbers_from_csv(file_path):
        """
        Extracts the 'Serial Number' column from the CSV file.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        serial_numbers = []
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)  # Use DictReader for column names
                if "Serial Number*" not in reader.fieldnames:
                    raise ValueError("'Serial Number' column not found in CSV file")

                for row in reader:
                    serial_numbers.append(row["Serial Number*"])
        except Exception as e:
            raise Exception(f"Error reading the file for Serial Numbers: {e}")

        return serial_numbers

    def afterUpload_TransactionID_Search(self, context, transactionID_Text):
        bulkuploadAction.click_submenu_list(context, "Create STB")

        clickFilter = self.findElementByXpath(
            context, stbMenu_Locators.filter_Locator)

        clickFilter.click()

        bulkuploadAction.enterValue(
            context, stbMenu_Locators.transactionID_locator, transactionID_Text
        )
        time.sleep(2)
        print("Transaction ID entered")

        click_Apply_Btn = self.findElementByXpath(
            context, stbMenu_Locators.apply_Btn_Locator)
        click_Apply_Btn.click()

        time.sleep(3)

        verifySerialNumber = self.findElementByXpath(
            context, stbMenu_Locators.serialnumber_List_Locator)

        serialNumberList = verifySerialNumber.text

        context.logger.info("Serial Number List: " + serialNumberList)
    def after_TransactionID_Search_SerialNumberverify(self, context):
        """
        Verifies that the 'Serial Number' from the UI matches the values in the CSV file.
        """
        file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/main_data.csv"
        # Get serial numbers from the CSV file
        csv_serial_numbers = SearchPage.get_serial_numbers_from_csv(file_path)
        context.logger.info(f"Serial Numbers from CSV: {csv_serial_numbers}")

        # Get serial numbers from the UI (adjust XPath as needed)
        ui_serial_numbers = []
        rows = self.findElementsByXpath(context, "//tbody/tr/td[3]/div[1]/app-table-column-format[1]/div[1]/div[1]")

        # Log the number of elements found
        context.logger.info(f"Number of rows found: {len(rows)}")

        for idx, row in enumerate(rows, start=1):
            value = row.text.strip()
            ui_serial_numbers.append(value)
            context.logger.info(f"Row {idx}: '{value}'")

        context.logger.info(f"Serial Numbers from UI: {ui_serial_numbers}")

        # Sort both lists for comparison
        sorted_csv_serial_numbers = sorted(csv_serial_numbers)
        sorted_ui_serial_numbers = sorted(ui_serial_numbers)

        # Log sorted lists for debugging
        context.logger.info(f"Sorted Serial Numbers from CSV: {sorted_csv_serial_numbers}")
        context.logger.info(f"Sorted Serial Numbers from UI: {sorted_ui_serial_numbers}")

        # Compare both lists
        if sorted_csv_serial_numbers == sorted_ui_serial_numbers:
            context.logger.info("Serial Numbers in UI match the values in the CSV file.")
        else:
            raise AssertionError(
                f"Serial Numbers do not match!\nCSV: {csv_serial_numbers}\nUI: {ui_serial_numbers}"
            )

    def verify_serial_number_search_from_csv(self, context, file_path):
        """
        Reads serial numbers from a CSV file and searches them one by one in the UI.
        Verifies that the searched serial number appears correctly in the UI results.
        """
        # Get serial numbers from the CSV file
        csv_serial_numbers = SearchPage.get_serial_numbers_from_csv(file_path)
        random.shuffle(csv_serial_numbers)  # Shuffle serial numbers to search in random order

        context.logger.info(f"Randomized Serial Numbers from CSV: {csv_serial_numbers}")

        # Navigate to the submenu
        bulkuploadAction.click_submenu_list(context, "STB List")

        mismatched_serials = []  # To keep track of mismatches

        for serial_number in csv_serial_numbers:
            context.logger.info(f"Searching for Serial Number: {serial_number}")

            dynamic_xpath = "//input[contains(@id, 'chipId')]"  # Dynamic XPath

            chip_id_field = self.findElementByXpath(context, dynamic_xpath)
            chip_id_field.clear()
            chip_id_field.send_keys(serial_number)

            context.logger.info(f"Entered Chip ID: {serial_number}")

            # Click Apply button
            apply_button = self.findElementByXpath(context, stbMenu_Locators.apply_Btn_Locator)
            apply_button.click()
            print("apply button clicked")
            time.sleep(3)

            dynamic_xpath = f"//tbody/tr/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1][normalize-space()='{serial_number}']"


            ui_serial_number = self.findElementByXpath(context, dynamic_xpath).text.strip()

            if serial_number == ui_serial_number:
                context.logger.info(f"Serial Number '{serial_number}' found successfully in UI.")
            else:
                mismatch_message = f"Mismatch! Expected: '{serial_number}', Found: '{ui_serial_number}'"
                context.logger.error(mismatch_message)
                mismatched_serials.append(mismatch_message)

        # Clear the search field for the next iteration
        clear_button = self.findElementByXpath(context, stbMenu_Locators.clear_Btn_Locator)
        clear_button.click()

        # Final validation
        if mismatched_serials:
            context.logger.error(f"Mismatches found: {mismatched_serials}")
            raise AssertionError("Serial number mismatches detected:\n" + "\n".join(mismatched_serials))
        else:
            context.logger.info("All serial numbers from CSV file have been successfully verified in the UI.")







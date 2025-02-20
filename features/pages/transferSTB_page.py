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


class transferSTBVerifyPage(BasePage):

    def __init__(self):
        # self.driver = driver
        super().__init__()
    context.logger = logging.getLogger()


    def get_destinationLCO_and_SerialNumber_from_csv(file_path):
        """
        Extracts the 'STB ID(Serial Number/VC Number)*' and 'Destination*' columns from the CSV file.
        Returns a list of dictionaries where each dictionary contains the 'STB ID(Serial Number/VC Number)*' and 'Destination*' values.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        extracted_data = []
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)  # Use DictReader for column names
                # Check if required columns exist in the CSV
                if "STB ID(Serial Number/VC Number)*" not in reader.fieldnames or "Destination*" not in reader.fieldnames:
                    raise ValueError(
                        "'STB ID(Serial Number/VC Number)*' or 'Destination*' column not found in CSV file"
                    )

                for row in reader:
                    # Append both columns as a dictionary
                    extracted_data.append({
                        "STB ID(Serial Number/VC Number)*": row["STB ID(Serial Number/VC Number)*"],
                        "Destination*": row["Destination*"]
                    })
        except Exception as e:
            raise Exception(f"Error reading the file for Serial Numbers and Destinations: {e}")

        return extracted_data


    def afterUpload_TransactionID_Search(self, context, transactionID_Text):
        bulkuploadAction.click_submenu_list(context, "Transfer STB")

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
            context, transfer_STB_Locators.STBID_Locator)

        serialNumberList = verifySerialNumber.text

        context.logger.info("Serial Number List: " + serialNumberList)
    def after_TransactionID_and_SerialNumberverify(self, context, file_path):
        """
        Verifies that the 'STB ID(Serial Number/VC Number)*' and 'Destination*' from the UI match the values in the CSV file.
        """
        # Get data from the CSV file
        csv_data = transferSTBVerifyPage.get_destinationLCO_and_SerialNumber_from_csv(file_path)
        context.logger.info(f"Data from CSV: {csv_data}")

        # Prepare the expected data structure for comparison
        expected_serial_numbers = [item["STB ID(Serial Number/VC Number)*"] for item in csv_data]
        expected_destinations = [item["Destination*"] for item in csv_data]

        # Get data from the UI
        ui_serial_numbers = []
        ui_destinations = []
        rows_serial_number = self.findElementsByXpath(
            context,
            "//tbody/tr/td[4]/div[1]/app-table-column-format[1]/div[1]/div[1]"
        )
        rows_destination = self.findElementsByXpath(
            context,
            "//tbody/tr/td[6]/div[1]/app-table-column-format[1]/div[1]/div[1]"
        )

        # Log the number of elements found
        context.logger.info(f"Number of serial number rows found: {len(rows_serial_number)}")
        context.logger.info(f"Number of destination rows found: {len(rows_destination)}")

        # Extract text for both Serial Numbers and Destinations
        for idx, row in enumerate(rows_serial_number, start=1):
            serial_number = row.text.strip()
            ui_serial_numbers.append(serial_number)
            context.logger.info(f"Serial Number Row {idx}: '{serial_number}'")

        for idx, row in enumerate(rows_destination, start=1):
            destination = row.text.strip()
            ui_destinations.append(destination)
            context.logger.info(f"Destination Row {idx}: '{destination}'")

        # Log UI data
        context.logger.info(f"Serial Numbers from UI: {ui_serial_numbers}")
        context.logger.info(f"Destinations from UI: {ui_destinations}")

        # Sort both lists for comparison
        sorted_csv_serial_numbers = sorted(expected_serial_numbers)
        sorted_ui_serial_numbers = sorted(ui_serial_numbers)
        sorted_csv_destinations = sorted(expected_destinations)
        sorted_ui_destinations = sorted(ui_destinations)

        # Log sorted lists for debugging
        context.logger.info(f"Sorted Serial Numbers from CSV: {sorted_csv_serial_numbers}")
        context.logger.info(f"Sorted Serial Numbers from UI: {sorted_ui_serial_numbers}")
        context.logger.info(f"Sorted Destinations from CSV: {sorted_csv_destinations}")
        context.logger.info(f"Sorted Destinations from UI: {sorted_ui_destinations}")

        # Compare both Serial Numbers and Destinations
        if sorted_csv_serial_numbers == sorted_ui_serial_numbers and sorted_csv_destinations == sorted_ui_destinations:
            context.logger.info("Serial Numbers and Destinations in UI match the values in the CSV file.")
        else:
            raise AssertionError(
                f"Data mismatch!\nCSV Serial Numbers: {sorted_csv_serial_numbers}\nUI Serial Numbers: {sorted_ui_serial_numbers}\n"
                f"CSV Destinations: {sorted_csv_destinations}\nUI Destinations: {sorted_ui_destinations}"
            )

    def verify_serial_number_and_lco_from_csv(self, context, file_path):
        """
        Reads serial numbers and destination LCO codes from a CSV file and verifies them in the UI.
        """
        # Step 1: Get serial numbers and LCO codes from the CSV file
        csv_data = transferSTBVerifyPage.get_destinationLCO_and_SerialNumber_from_csv(file_path)
        random.shuffle(csv_data)  # Shuffle serial numbers to search in random order

        context.logger.info(f"Randomized Serial Numbers from CSV: {csv_data}")

        # Step 2: Navigate to the submenu (STB List)
        bulkuploadAction.click_submenu_list(context, "STB List")
        mismatched_serials = []

        # Step 3: Loop through each serial number and LCO code
        for item in csv_data:
            serial_number = item["STB ID(Serial Number/VC Number)*"]
            csv_lco_code = item["Destination*"]

            # Enter the serial number into the search field
            dynamic_xpath = "//input[contains(@id, 'chipId')]"  # Dynamic XPath

            chip_id_field = self.findElementByXpath(context, dynamic_xpath)
            chip_id_field.clear()
            chip_id_field.send_keys(serial_number)

            context.logger.info(f"Entered Chip ID: {serial_number}")

            # Click Apply button
            apply_button = self.findElementByXpath(context, stbMenu_Locators.apply_Btn_Locator)
            apply_button.click()
            print("Apply button clicked")
            time.sleep(3)

            try:
                # Get the serial number and LCO code displayed in the UI
                ui_serial_number = self.findElementByXpath(
                    context, f"//tbody/tr/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1][normalize-space()='{serial_number}']"
                ).text.strip()
                ui_lco_code = self.findElementByXpath(
                    context, f"//tbody/tr[1]/td[8]/div[1]/app-table-column-format[1]/div[1]/div[1][normalize-space()='{csv_lco_code}']"
                ).text.strip()

                context.logger.info(f"UI Serial Number: {ui_serial_number}")
                context.logger.info(f"UI Destination LCO Code: {ui_lco_code}")

                # Verify the serial number and LCO code
                if serial_number == ui_serial_number and csv_lco_code == ui_lco_code:
                    context.logger.info(
                        f"Serial Number: '{serial_number}', LCO Code: '{csv_lco_code}' verified successfully."
                    )
                else:
                    mismatched_serials.append(
                        f"Expected: Serial Number '{serial_number}', LCO Code '{csv_lco_code}'. "
                        f"Found: Serial Number '{ui_serial_number}', LCO Code '{ui_lco_code}'."
                    )

            except Exception as e:
                mismatched_serials.append(f"Serial Number '{serial_number}' not found in UI. Error: {e}")

        # Clear the search for the next iteration
        clear_button = self.findElementByXpath(context, stbMenu_Locators.clear_Btn_Locator)
        clear_button.click()

        # Log mismatches after iteration
        if mismatched_serials:
            context.logger.error("Mismatches found:")
            for mismatch in mismatched_serials:
                context.logger.error(mismatch)
        else:
            context.logger.info("All serial numbers and destination LCO codes from CSV file have been successfully verified in the UI.")





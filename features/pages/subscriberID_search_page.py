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
from features.utils.ProductLocators import ProductLocators
from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage
import os
import csv


class subscriberIDVerifyPage(BasePage):

    def __init__(self):
        # self.driver = driver
        super().__init__()
    context.logger = logging.getLogger()

    def get_subscriber_first_name_from_csv(file_path):
        """
        Extracts the 'First Name*' column from the CSV file.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        subscriber_first_name = []
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)  # Use DictReader for column names
                if "First Name*" not in reader.fieldnames:
                    raise ValueError("'First Name*' column not found in CSV file")

                for row in reader:
                    subscriber_first_name.append(row["First Name*"])
        except Exception as e:
            raise Exception(f"Error reading the file for product name: {e}")

        return subscriber_first_name

    def afterUpload_Search_SubName(self,context,file_path):

        # Extract data from the CSV file for the specified column
        csv_data = subscriberIDVerifyPage.get_subscriber_first_name_from_csv(file_path)
        random.shuffle(csv_data)
        # expected_values = [item[column_name] for item in csv_data]

        # Log the extracted data
        # context.logger.info(f"Data from CSV ({column_name}): {expected_values}")

        # Step 2: Navigate to the subscribermenu (subscriber List)
        bulkuploadAction.click_submenu_list(context, "Subscriber List")

        clickFilter = self.findElementByXpath(context, ProductLocators.filter_Locator)
        clickFilter.click()
        time.sleep(1)

        mismatch_subscriber_firstname = []

        # Step 3: Loop through each Subscriber First Name and LCO code
        for row_data in csv_data:
            # subscriber_name = row_data["First Name*"]
            context.logger.info(f"Searching for Subscriber FirstName: {row_data}")

            # Enter the Subscriber First Name into the search field
            # bulkuploadAction.enterValue(context, subscriber_Locators.subscriber_First_name, subscriber_name)
            dynamic_xpath = "//input[contains(@id, 'firstName')]"
            product_name_field = self.findElementByXpath(context, dynamic_xpath)
            product_name_field.clear()
            product_name_field.send_keys(row_data)
            apply_button = self.findElementByXpath(context, stbMenu_Locators.apply_Btn_Locator)
            apply_button.click()
            time.sleep(2)

            # Get the Subscriber First Name and LCO code displayed in the UI
            ui_subscriber_first_name = self.findElementByXpath(
                context, "//tbody/tr[1]/td[4]/div[1]/app-table-column-format[1]/div[1]/div[1][normalize-space()='{row_data}']"
            ).text.strip()
            context.logger.info(f"UI Subscriber First Name: {ui_subscriber_first_name}")


            # Verify the Subscriber First Name
            if row_data == ui_subscriber_first_name:
                context.logger.info(
                    f"matches successfully. Subscriber First Name: '{row_data}'."
                )
            else:
                raise AssertionError(
                    f"Expected: Subscriber First Name '{row_data}'. "
                    f"Found: Subscriber First Name '{ui_subscriber_first_name}'."
                )

        # Clear the search for the next iteration
        clear_button = self.findElementByXpath(context, stbMenu_Locators.clear_Btn_Locator)
        clear_button.click()

        # Final validation
        if mismatch_subscriber_firstname:
            context.logger.error(f"Mismatches found: {mismatch_subscriber_firstname}")
            raise AssertionError("Serial number mismatches detected:\n" + "\n".join(mismatch_subscriber_firstname))
        else:
            context.logger.info("All serial numbers from CSV file have been successfully verified in the UI.")

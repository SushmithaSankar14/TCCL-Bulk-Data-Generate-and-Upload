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
from features.utils.ProductLocators import ProductLocators
from features.pages.bulkupload_page import bulkUpload
from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage

import os
import csv


class productVerification(BasePage):

    def __init__(self):
        # self.driver = driver
        super().__init__()
    context.logger = logging.getLogger()

    def get_product_name_from_csv(file_path):
        """
        Extracts the 'Product Name*' column from the CSV file.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        product_name = []
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)  # Use DictReader for column names
                if "Product Name*" not in reader.fieldnames:
                    raise ValueError("'Product Name*' column not found in CSV file")

                for row in reader:
                    product_name.append(row["Product Name*"])
        except Exception as e:
            raise Exception(f"Error reading the file for product name: {e}")

        return product_name

    # def get_productName_in_csv(file_path,column_names):


    #     data = bulkuploadAction.extract_columns_from_csv(file_path, column_names)
    #     print(data)

    def afterUpload_Search_ProductName(self,context,file_path):

        # Extract data from the CSV file for the specified column
        csv_data = productVerification.get_product_name_from_csv(file_path)
        random.shuffle(csv_data)

        # Log the extracted data
        context.logger.info(f"Randomized Serial Numbers from CSV: {csv_data}")

        # Step 2: Navigate to the submenu (STB List)
        bulkuploadAction.click_submenu_list(context, "Product List")
        clickFilter = self.findElementByXpath(context, ProductLocators.filter_Locator)
        clickFilter.click()
        time.sleep(1)

        mismatch_product = []
        # Step 3: Loop through each ProductName and LCO code
        for row_data in csv_data:

            context.logger.info(f"Searching for ProductName: {row_data}")

            # Enter the ProductName  Name into the search field
            # bulkuploadAction.enterValue(context, ProductLocators.productNameLocator, product_name)
            dynamic_xpath = "//input[contains(@id, 'productName')]"
            product_name_field = self.findElementByXpath(context, dynamic_xpath)
            product_name_field.clear()
            product_name_field.send_keys(row_data)
            apply_button = self.findElementByXpath(context, ProductLocators.search_Btn)
            apply_button.click()
            time.sleep(3)

            # Get the ProductName and LCO code displayed in the UI
            ui_product_name = self.findElementByXpath(
                context, f"//tbody/tr[1]/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1][normalize-space()='{row_data}']"
            ).text.strip()
            context.logger.info(f"UI ProductName: {ui_product_name}")


            # Verify the ProductName  Name
            if row_data== ui_product_name:
                context.logger.info(
                    f"matches successfully. ProductName: '{row_data}'."
                )
            else:
                raise AssertionError(
                    f"Expected: ProductName '{row_data}'. "
                    f"Found: ProductName '{ui_product_name}'."
                )

        # Clear the search for the next iteration
        clear_button = self.findElementByXpath(context, stbMenu_Locators.clear_Btn_Locator)
        clear_button.click()

        # Final validation
        if mismatch_product:
            context.logger.error(f"Mismatches found: {mismatch_product}")
            raise AssertionError("Serial number mismatches detected:\n" + "\n".join(mismatch_product))
        else:
            context.logger.info("All serial numbers from CSV file have been successfully verified in the UI.")

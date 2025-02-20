import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from features.utils.ProductLocators import ProductLocators
import csv
from typing import List
import string
import random
import time
from faker import Faker
from utils.locators import *
import re


class bulkuploadAction(BasePage):
    def __init__(self):
        self = self

    def enterValue(context, locator, value):
        fieldElement = context.BasePage.findElementByXpath(context, locator)
        fieldElement.clear()
        fieldElement.send_keys(value)

    def clickElementFound(context, locator):
        currentElementToBeClicked = context.BasePage.findElementByXpath(
            context, locator
        )
        currentElementToBeClicked.click()

    def clickMenuList(context, value):
        # Construct the XPath using the STBmenu text
        menuListElement = f"//img[@alt='{value}']"

        # Find the element using the constructed XPath
        context.BasePage.findElementByXpath(
            context, menuListElement
        )

        # Call clickElementFound with only 2 arguments
        bulkuploadAction.clickElementFound(
            context, menuListElement
        )

        context.logger.info("Menu is Clicked : " + value)

    def click_submenu_list(context, value):
        # Construct XPath for the element
        sub_menu_list_element = f"//span[normalize-space(text())= '{value}']"

        # Find the element using the constructed XPath
        context.BasePage.findElementByXpath(context, sub_menu_list_element)

        # Click the found element
        bulkuploadAction.clickElementFound(
            context, sub_menu_list_element)

        # Log the action
        context.logger.info(f"Menu is clicked: {value}")

    def selectValueFromList(context, InputFieldLocator, listLocator, value, fieldName):
        inputField = context.BasePage.findElementByXpath(
            context, InputFieldLocator)
        # context.BasePage.scrollIntoCenterView(context, inputField)
        inputField.click()
        time.sleep(1)
        inputField.send_keys(value)
        time.sleep(1)

        retry_count = 0
        max_retries = 5
        value_selected = False

        while retry_count < max_retries and not value_selected:
            # Find list of result
            listElements = context.BasePage.findElementsByXpath(
                context, listLocator)
            context.logger.info(
                f"Attempt {retry_count + 1}: Searching for value '{value}' in {fieldName}")

            # Loop through the elements
            for element in listElements:
                # Check if the element's text matches the desired text
                if element.text == str(value):
                    # Click the element
                    element.click()
                    # Indicate the value was successfully selected
                    context.logger.info(
                        f"Value '{value}' selected from {fieldName}"
                    )
                    value_selected = True
                    break

            if not value_selected:
                retry_count += 1
                context.logger.warning(
                    f"Value '{value}' not found in {fieldName}, retrying... ({retry_count}/{max_retries})")

        if not value_selected:
            context.logger.error(
                f"Failed to select value '{value}' from {fieldName} after {max_retries} attempts")
        else:
            context.logger.info(
                f"Value '{value}' successfully selected for {fieldName}")

    def get_row_count(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        try:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                row_count = sum(1 for row in reader) - 1  # Exclude header row
                return row_count
        except Exception as e:
            raise Exception(f"Error reading the file to count rows: {e}")

    def upload_file(self, context, file_path):

        # Verify that the file exists
        if not os.path.exists(file_path):
            context.logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")
        else:
            context.logger.info(
                f"File exists and ready for upload: {file_path}")

        #  # Count rows in the file
        # try:
        #     with open(file_path, "r") as file:
        #         reader = csv.reader(file)
        #         # Subtract 1 to exclude the header row
        #         row_count = sum(1 for row in reader) - 1
        #         context.logger.info(f"Number of rows in the file: {row_count}")
        # except Exception as e:
        #     context.logger.error(f"Error reading the file to count rows: {e}")
        #     raise

        row_count = bulkuploadAction.get_row_count(file_path)
        context.logger.info(f"Number of rows in the file: {row_count}")

        # row_count = bulkuploadAction.upload_file(context, file_path)
        # bulkuploadAction.assert_process_counts(context, row_count=row_count)

        # Wait for the element to be clickable
        upload_button = context.driver.find_element(
            By.XPATH, stbMenu_Locators.upload_stb_file)

        # Ensure the element is visible and interactable
        context.driver.execute_script(
            "arguments[0].scrollIntoView(true);", upload_button)

        # # Use ActionChains to click on the element
        # actions = ActionChains(context.driver)
        # context.logger.info("ActionChains initialized successfully")
        # actions.move_to_element(upload_button).click().perform()

        # Locate the file input element and upload the file
        file_input = context.driver.find_element(
            By.XPATH, "//input[@id='fileInput']")
        file_input.send_keys(file_path)

        # # Optionally, wait for the file to upload
        time.sleep(5)  # Replace with explicit waits if possible

        # Click the import button after uploading the file
        import_button = context.driver.find_element(
            By.XPATH, stbMenu_Locators.import_button)
        import_button.click()
        context.logger.info("File uploaded successfully")

        # Validate the success message
        try:
            # Wait for the success message to appear
            success_message_element = WebDriverWait(context.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, stbMenu_Locators.file_uploded_success_msg))
            )
            success_message_text = success_message_element.text
            context.logger.info(
                f"Retrieved success message: '{success_message_text}'")

            # Assert the text matches the expected value
            assert success_message_text == "Success!", f"Expected 'Success!', got '{success_message_text}'"

            time.sleep(10)

        except Exception as e:
            context.logger.error(
                f"Error while validating success message: {e}")
            raise
        return row_count

    def click_refresh_Btn(self, context):
        """
        Clicks the refresh button with retry mechanism to handle stale elements.
        """
        max_retries = 5
        retries = 0

        while retries < max_retries:
            try:
                # Find the refresh button
                click_refresh = self.findElementByXpath(
                    context, stbMenu_Locators.refersh_btn)

                # Wait for the button to be clickable before interacting
                WebDriverWait(context.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, stbMenu_Locators.refersh_btn))
                )

                # Click the refresh button
                click_refresh.click()
                context.logger.info("Refresh button clicked.")
                # Optional, to wait for the refresh action to complete
                time.sleep(3)
                return  # Exit the function if successful

            except StaleElementReferenceException:
                # Handle stale element by retrying to locate the button
                retries += 1
                context.logger.warning(
                    f"Retrying to click the refresh button... Attempt {retries}/{max_retries}."
                )
                time.sleep(2)  # Short delay before retrying

            except TimeoutException:
                # Handle timeout exception if the button is not clickable
                retries += 1
                context.logger.error(
                    f"Refresh button not clickable. Attempt {retries}/{max_retries}."
                )
                time.sleep(4)

        # If all retries fail, raise an exception
        raise Exception(
            "Failed to click the refresh button after multiple attempts.")

    def assert_process_counts(self, context):
        """
        Asserts and determines the final status based on success, failed counts, and partial errors.
        Compares the computed final status with the status displayed in the UI.

        Args:
            context: The test context object.
            process_locator: XPath locator for the cell containing the counts.
            status_locator: XPath locator for the status element to be asserted.

        Returns:
            final_status: The computed final status.
        """
        max_retries = 5
        retries = 0

        while retries < max_retries:
            try:
                # Locate the element and extract its text for counts
                cell_element = self.findElementByXpath(
                    context, stbMenu_Locators.process_locator)
                # Example: "Partial Error | Total: 10, Success: 9, Failed: 1"
                cell_text = cell_element.text.strip()

                time.sleep(5)

                # Locate the element and extract its text for status
                assert_status_element = self.findElementByXpath(
                    context, stbMenu_Locators.status_Locator)
                assert_status_text = assert_status_element.text.strip()  # Example: "Partial Error"
                time.sleep(5)

                # Extract counts using regex

                match = re.search(
                    r'Total:\s*(\d+),\s*Success:\s*(\d+),\s*Failed:\s*(\d+)', cell_text)
                if match:
                    total_count = int(match.group(1))  # Extracted Total count
                    # Extracted Success count
                    success_count = int(match.group(2))
                    # Extracted Failed count
                    failed_count = int(match.group(3))
                else:
                    raise ValueError(
                        f"Unexpected format for cell text: {cell_text}")

                # if row_count != total_count:
                #     raise AssertionError(
                #         f"Mismatch between file row count ({row_count}) and UI total count ({total_count})"
                #     )
                # else:
                #     context.logger.info(
                #         f"File row count ({row_count}) matches UI total count ({total_count})"
                #     )

                # Determine the final status
                if failed_count > 0:
                    if success_count > 0:
                        final_status = "Partial Error"
                    else:
                        final_status = "Failed"
                elif success_count > 0:
                    final_status = "Success"
                else:
                    final_status = "Unknown"  # Handles cases where both success and failed are 0

                # Log the details
                context.logger.info(f"Cell text: {cell_text}")
                context.logger.info(f"Total count: {total_count}")
                context.logger.info(f"Success count: {success_count}")
                context.logger.info(f"Failed count: {failed_count}")
                context.logger.info(f"Computed final status: {final_status}")
                context.logger.info(
                    f"UI displayed status: {assert_status_text}")

                # Print (optional)
                print(f"Cell text: {cell_text}")
                print(f"Total count: {total_count}")
                print(f"Success count: {success_count}")
                print(f"Failed count: {failed_count}")
                print(f"Computed final status: {final_status}")
                print(f"UI displayed status: {assert_status_text}")

                # Assert if the computed final status matches the UI status
                if final_status != assert_status_text:
                    raise AssertionError(
                        f"Mismatch between computed status ({final_status}) and UI status ({assert_status_text})")

                # Handle error file if needed
                if final_status == "Partial Error" or final_status == "Failed":
                    try:
                        # Wait for the "Error File" link to appear and click it
                        error_file_element = WebDriverWait(context.driver, 10).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//div[normalize-space()='Error File']/ancestor::table//tbody/tr[5]/td[8]/div[1]/app-table-column-format[1]/div[1]/div[1]/div[1]/a[2]/img[1]")
                            )
                        )
                        # Scroll into view and click the "Error File" icon
                        context.driver.execute_script(
                            "arguments[0].scrollIntoView(true);", error_file_element)
                        ActionChains(context.driver).move_to_element(
                            error_file_element).click().perform()
                        context.logger.info(
                            "Clicked on 'Error File' link successfully.")
                    except Exception as e:
                        context.logger.error(
                            f"Failed to click on 'Error File': {e}")
                        raise

                        # assert error file text
                        error_msg_element = self.findElementByXpath(
                            context, stbMenu_Locators.error_file_text)
                        error_msg_text = error_msg_element.text.strip()
                        context.logger.info(
                            f"Error file message: {error_msg_text}")

                        click_close = self.findElementByXpath(
                            context, stbMenu_Locators.close_btn_Locator)

                # Return the final status
                return final_status
            except (StaleElementReferenceException, ValueError, NoSuchElementException, TimeoutException) as e:
                retries += 1
                context.logger.warning(
                    f"Retrying... Attempt {retries}/{max_retries} due to error: {e}")
                if retries < max_retries:
                    self.click_refresh_Btn(context)

        # Raise an error if all retries fail
        raise Exception(
            "Failed to fetch and assert process counts after multiple attempts.")

    #product assert only below function because locator change
    def product_assert_process_counts(self, context):
        """
        Asserts and determines the final status based on success, failed counts, and partial errors.
        Compares the computed final status with the status displayed in the UI.

        Args:
            context: The test context object.
            process_locator: XPath locator for the cell containing the counts.
            status_locator: XPath locator for the status element to be asserted.

        Returns:
            final_status: The computed final status.
        """
        max_retries = 5
        retries = 0

        while retries < max_retries:
            try:
                # Locate the element and extract its text for counts
                cell_element = self.findElementByXpath(
                    context, ProductLocators.process_locator)
                # Example: "Partial Error | Total: 10, Success: 9, Failed: 1"
                cell_text = cell_element.text.strip()

                time.sleep(5)

                # Locate the element and extract its text for status
                assert_status_element = self.findElementByXpath(
                    context, ProductLocators.status_Locator)
                assert_status_text = assert_status_element.text.strip()  # Example: "Partial Error"
                time.sleep(5)

                # Extract counts using regex

                match = re.search(
                    r'Total:\s*(\d+),\s*Success:\s*(\d+),\s*Failed:\s*(\d+)', cell_text)
                if match:
                    total_count = int(match.group(1))  # Extracted Total count
                    # Extracted Success count
                    success_count = int(match.group(2))
                    # Extracted Failed count
                    failed_count = int(match.group(3))
                else:
                    raise ValueError(
                        f"Unexpected format for cell text: {cell_text}")

                # if row_count != total_count:
                #     raise AssertionError(
                #         f"Mismatch between file row count ({row_count}) and UI total count ({total_count})"
                #     )
                # else:
                #     context.logger.info(
                #         f"File row count ({row_count}) matches UI total count ({total_count})"
                #     )

                # Determine the final status
                if failed_count > 0:
                    if success_count > 0:
                        final_status = "Partial Error"
                    else:
                        final_status = "Failed"
                elif success_count > 0:
                    final_status = "Success"
                else:
                    final_status = "Unknown"  # Handles cases where both success and failed are 0

                # Log the details
                context.logger.info(f"Cell text: {cell_text}")
                context.logger.info(f"Total count: {total_count}")
                context.logger.info(f"Success count: {success_count}")
                context.logger.info(f"Failed count: {failed_count}")
                context.logger.info(f"Computed final status: {final_status}")
                context.logger.info(
                    f"UI displayed status: {assert_status_text}")

                # Print (optional)
                print(f"Cell text: {cell_text}")
                print(f"Total count: {total_count}")
                print(f"Success count: {success_count}")
                print(f"Failed count: {failed_count}")
                print(f"Computed final status: {final_status}")
                print(f"UI displayed status: {assert_status_text}")

                # Assert if the computed final status matches the UI status
                if final_status != assert_status_text:
                    raise AssertionError(
                        f"Mismatch between computed status ({final_status}) and UI status ({assert_status_text})")

                # Handle error file if needed
                if final_status == "Partial Error" or final_status == "Failed":
                    try:
                        # Wait for the "Error File" link to appear and click it
                        error_file_element = WebDriverWait(context.driver, 10).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//div[normalize-space()='Error File']/ancestor::table//tbody/tr[5]/td[8]/div[1]/app-table-column-format[1]/div[1]/div[1]/div[1]/a[2]/img[1]")
                            )
                        )
                        # Scroll into view and click the "Error File" icon
                        context.driver.execute_script(
                            "arguments[0].scrollIntoView(true);", error_file_element)
                        ActionChains(context.driver).move_to_element(
                            error_file_element).click().perform()
                        context.logger.info(
                            "Clicked on 'Error File' link successfully.")
                    except Exception as e:
                        context.logger.error(
                            f"Failed to click on 'Error File': {e}")
                        raise

                        # assert error file text
                        error_msg_element = self.findElementByXpath(
                            context, stbMenu_Locators.error_file_text)
                        error_msg_text = error_msg_element.text.strip()
                        context.logger.info(
                            f"Error file message: {error_msg_text}")

                        click_close = self.findElementByXpath(
                            context, stbMenu_Locators.close_btn_Locator)

                # Return the final status
                return final_status
            except (StaleElementReferenceException, ValueError, NoSuchElementException, TimeoutException) as e:
                retries += 1
                context.logger.warning(
                    f"Retrying... Attempt {retries}/{max_retries} due to error: {e}")
                if retries < max_retries:
                    self.click_refresh_Btn(context)

        # Raise an error if all retries fail
        raise Exception(
            "Failed to fetch and assert process counts after multiple attempts.")

    def breadcrumb_validation(self, context):
        """
        Validates and retrieves the breadcrumb text using a common locator.
        """
        # Common locator for all breadcrumbs
        breadcrumb_locator = "//a[@class='breadcrum-text opacity-100']"

        # Locate the breadcrumb element
        breadcrumb_element = self.findElementByXpath(
            context, breadcrumb_locator)

        # Retrieve the text
        breadcrumb_text = breadcrumb_element.text

        # Log the retrieved text
        context.logger.info(f"Retrieved breadcrumb text: '{breadcrumb_text}'")

        # Return the breadcrumb text
        return breadcrumb_text

    def get_serial_and_vc_numbers_from_csv(self, file_path):
        """
        Reads the serial number and VC number from the given CSV file.
        Returns a list of tuples (serial_number, vc_number).
        """
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                data = [(row['serial_number'], row['vc_number'])
                        for row in reader if 'serial_number' in row and 'vc_number' in row]
                return data
        except Exception as e:
            raise Exception(f"Error reading CSV file: {e}")

    def search_stb(context):
        """
        Reads serial numbers and VC numbers from a CSV file and performs the search for each entry.
        """
        # file_path = r"D:\Automation\tccl-sms\TestAutomation-SMS\features\files\main_data.csv"

        try:
            file_path = r"D:\Automation\tccl-sms\TestAutomation-SMS\features\files\main_data.csv"
            data = self.get_serial_and_vc_numbers_from_csv(file_path)
            # Perform search using the data
            for serial_number, vc_number in data:
                context.logger.info(
                    f"Processing Serial Number: {serial_number}, VC Number: {vc_number}")
                try:
                    # Navigate to the submenu list
                    bulkuploadAction.click_submenu_list(context, "STB List")

                    # Enter Serial Number in the search field
                    bulkuploadAction.enterValue(
                        context, create_STBLocators.Chip_id, serial_number)
                    context.logger.info(
                        f"Entered Serial Number: {serial_number}")

                    # Enter VC Number in the search field
                    bulkuploadAction.enterValue(
                        context, create_STBLocators.CAS_id, vc_number)
                    context.logger.info(f"Entered VC Number: {vc_number}")

                    # Click the search button
                    search_button = context.driver.find_element(
                        By.XPATH, create_STBLocators.search_button)
                    search_button.click()
                    context.logger.info("Search button clicked.")

                    # Wait for search results to appear
                    WebDriverWait(context.driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, create_STBLocators.search_results_table)
                        )
                    )
                    context.logger.info("Search results table displayed.")

                except AssertionError as ae:
                    context.logger.error(f"Assertion Error: {ae}")
                except Exception as e:
                    context.logger.error(
                        f"Error during search for Serial Number: {serial_number}, VC Number: {vc_number} - {e}")

        except Exception as e:
            context.logger.error(f"Error in search_stb: {e}")
            raise

    def extract_columns_from_csv(file_path, column_names):
        """
        Extracts specified columns from a CSV file.

        Args:
            file_path (str): Path to the CSV file.
            column_names (list): List of column names to extract.

        Returns:
            list[dict]: A list of dictionaries containing the specified columns and their values.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If any specified column is not found in the CSV file.
            Exception: For any errors during file reading.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        extracted_data = []
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)  # Use DictReader to handle column names

                # Check if all required columns exist in the CSV
                missing_columns = [col for col in column_names if col not in reader.fieldnames]
                if missing_columns:
                    raise ValueError(f"Missing columns in CSV file: {''.join(missing_columns)}")

                for row in reader:
                    # Extract only the specified columns
                    extracted_data.append({col: row[col] for col in column_names})
                print("value extracted")
        except Exception as e:
            raise Exception(f"Error reading the file for columns {column_names}: {e}")

        return extracted_data

    # def get_serial_numbers_from_csv(file_path):
    #     """
    #     Extracts the 'Serial Number' column from the CSV file.
    #     """

    #     if not os.path.exists(file_path):
    #         raise FileNotFoundError(f"File not found: {file_path}")

    #     serial_numbers = []
    #     try:
    #         with open(file_path, "r") as file:
    #             reader = csv.DictReader(file)  # Use DictReader for column names
    #             if "Serial Number*" not in reader.fieldnames:
    #                 raise ValueError("'Serial Number' column not found in CSV file")

    #             for row in reader:
    #                 serial_numbers.append(row["Serial Number*"])
    #     except Exception as e:
    #         raise Exception(f"Error reading the file for Serial Numbers: {e}")

    #     return serial_numbers

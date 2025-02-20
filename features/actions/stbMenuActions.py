import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from typing import List
import string
import random
import time
from faker import Faker


class stbMenuListAction(BasePage):
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
        stbMenuListAction.clickElementFound(
            context, menuListElement
        )

        context.logger.info("Menu is Clicked : " + value)

    def click_submenu_list(context, value):
        # Construct XPath for the element
        sub_menu_list_element = f"//span[normalize-space(text())= '{value}']"

        # Find the element using the constructed XPath
        context.BasePage.findElementByXpath(context, sub_menu_list_element)

        # Click the found element
        stbMenuListAction.clickElementFound(
            context, sub_menu_list_element)

        # Log the action
        context.logger.info(f"Menu is clicked: {value}")

    # def upload_file(context, file_path, upload_button_locator, file_input_locator, import_button_locator, success_msg_locator):
    #     """
    #     Common method for uploading files and validating success.

    #     Args:
    #         context: Test context object containing driver and logger.
    #         file_path: Path of the file to upload.
    #         upload_button_locator: Locator for the button to trigger file upload.
    #         file_input_locator: Locator for the file input element.
    #         import_button_locator: Locator for the import button after uploading.
    #         success_msg_locator: Locator for the success message after upload.

    #     Returns:
    #         str: The success message text.

    #     Raises:
    #         FileNotFoundError: If the file does not exist.
    #         AssertionError: If the success message validation fails.
    #     """
    #     # Verify that the file exists
    #     if not os.path.exists(file_path):
    #         context.logger.error(f"File not found: {file_path}")
    #         raise FileNotFoundError(f"File not found: {file_path}")
    #     else:
    #         context.logger.info(
    #             f"File exists and ready for upload: {file_path}")

    #     # Wait for the element to be clickable
    #     upload_button = context.driver.find_element(
    #         By.XPATH, upload_button_locator)

    #     # Ensure the element is visible and interactable
    #     context.driver.execute_script(
    #         "arguments[0].scrollIntoView(true);", upload_button)

    #     # Use ActionChains to click on the element
    #     actions = ActionChains(context.driver)
    #     context.logger.info("ActionChains initialized successfully")
    #     actions.move_to_element(upload_button).click().perform()

    #     # Locate the file input element and upload the file
    #     file_input = context.driver.find_element(By.XPATH, file_input_locator)
    #     file_input.send_keys(file_path)

    #     # Optionally, wait for the file to upload
    #     time.sleep(5)  # Replace with explicit waits if possible

    #     # Click the import button after uploading the file
    #     import_button = context.driver.find_element(
    #         By.XPATH, import_button_locator)
    #     import_button.click()
    #     context.logger.info("File uploaded successfully")

    #     # Validate the success message
    #     try:
    #         # Wait for the success message to appear
    #         success_message_element = WebDriverWait(context.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.XPATH, success_msg_locator))
    #         )
    #         success_message_text = success_message_element.text
    #         context.logger.info(f"Retrieved success message: '{
    #                             success_message_text}'")

    #         # Assert the text matches the expected value
    #         assert success_message_text == "Success!", f"Expected 'Success!', got '{
    #             success_message_text}'"

    #     except Exception as e:
    #         context.logger.error(
    #             f"Error while validating success message: {e}")
    #         raise

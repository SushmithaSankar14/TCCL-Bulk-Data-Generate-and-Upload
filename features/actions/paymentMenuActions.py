import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from features.utils.paymentLocators import payments_Locators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from typing import List
import string
import random
import time
from faker import Faker


class paymentsActionMenu(BasePage):
    def __init__(self):
        self = self

    def enterValue(context, locator, value):
        # Ensure BasePage is instantiated and findElementByXpath is an instance method
        fieldElement = context.BasePage.findElementByXpath(context, locator)
        fieldElement.clear()
        fieldElement.send_keys(value)

    def clickElementFound(context, locator, about):
        currentElementToBeClicked = context.BasePage.findElementByXpath(
            context, locator
        )
        currentElementToBeClicked.click()
        context.logger.info("Element Clicked : " + about)

    def clickMenuList(context, value):
        # Construct the XPath using the STBmenu text
        menuListElement = f"//img[@alt='{value}']"

        # Find the element using the constructed XPath
        context.BasePage.findElementByXpath(
            context, menuListElement
        )

        # Call clickElementFound with only 2 arguments
        paymentsActionMenu.clickElementFound(
            context, menuListElement, "clickMenuList"
        )

        context.logger.info("Menu is Clicked : " + value)

    def click_submenu_list(context, value):
        # Construct XPath for the element
        sub_menu_list_element = f"//span[normalize-space(text())= '{value}']"

        # Find the element using the constructed XPath
        context.BasePage.findElementByXpath(context, sub_menu_list_element)

        # Click the found element
        paymentsActionMenu.clickElementFound(
            context, sub_menu_list_element, "click_submenu_list")

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
                f"Attempt {retry_count +1}: Searching for value '{value}' in {fieldName}")

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
            context.logger.info(f"Value '{value}' successfully selected for {fieldName}")

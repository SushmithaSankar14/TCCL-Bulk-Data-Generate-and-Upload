import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage

from typing import List
import string
import random
import time
from faker import Faker


class usersMenuListAction(BasePage):
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
        usersMenuListAction.clickElementFound(
            context, menuListElement
        )

        context.logger.info("Menu is Clicked : " + value)

    def click_submenu_list(context, value):
        # Construct XPath for the element
        sub_menu_list_element = f"//span[normalize-space(text())= '{value}']"

        # Find the element using the constructed XPath
        context.BasePage.findElementByXpath(context, sub_menu_list_element)

        # Click the found element
        usersMenuListAction.clickElementFound(
            context, sub_menu_list_element)

        # Log the action
        context.logger.info(f"Menu is clicked: {value}")

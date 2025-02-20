from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.utils.data import Add_Customer
from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage
from features.utils.data import Add_STB
from selenium.webdriver.support.ui import Select
import random
from features.actions.stbMenuActions import stbMenuListAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils.locators import *
import time


class stbPage(BasePage):
    def __init__(self):
        super().__init__()

    def clicksTBModule_page(self, context, value):
        stbMenuListAction.clickMenuList(
            context, value)

    def add_STB(self, context):
        add_STB = self.findElementByXpath(context, create_STBLocators.Add_STB)
        add_STB.click()

    def select_Server_Type(self, context, value):
        self.selectValueFromList(
            context,
            create_STBLocators.Server_Type,
            create_STBLocators.Server_Type_List,
            value,
            "Sumavision",
        )
        print("Sumavision")

    def chip_ID(self, context):
        chip_ID_Locator = self.findElementByXpath(
            context, create_STBLocators.Chip_id)
        childid = Add_STB.Chip_ID
        chip_ID_Locator.send_keys(childid)

    def cas_ID(self, context):
        casID_Locator = self.findElementByXpath(
            context, create_STBLocators.CAS_id)
        casID = Add_STB.Chip_ID
        casID_Locator.send_keys(casID)

    def select_Model(self, context):
        try:
            # Wait for the dropdown element to be clickable and click it
            dropdown_element = WebDriverWait(context.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, create_STBLocators.Select_Model))
            )
            dropdown_element.click()

            # Wait for the options to be visible
            options = WebDriverWait(context.driver, 10).until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, create_STBLocators.Select_Model_List)
                )
            )

            # Extract the text of each option and print available options
            option_texts = [option.text for option in options]
            print("Available options:", option_texts)

            # Select a random option from the list
            selected_option = random.choice(options)

            # Click the selected option
            selected_option.click()

            # Print the selected option's text
            print("Selected option:", selected_option.text)

        except Exception as e:
            print(f"An error occurred: {e}")

        # Optionally, add a sleep to observe the selected option (not recommended for production code)

    def select_STB_Type(self, context):
        try:
            # Wait for the dropdown element to be clickable and click it
            dropdown_element = WebDriverWait(context.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, create_STBLocators.STB_Type))
            )
            dropdown_element.click()

            # Wait for the options to be visible
            options = WebDriverWait(context.driver, 10).until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, create_STBLocators.STB_Type_List)
                )
            )

            # Extract the text of each option and print available options
            option_texts = [option.text for option in options]
            print("Available options:", option_texts)

            # Select a random option from the list
            selected_option = random.choice(options)

            # Click the selected option
            selected_option.click()

            # Print the selected option's text
            print("Selected option:", selected_option.text)

        except Exception as e:
            print(f"An error occurred: {e}")

        # Optionally, add a sleep to observe the selected option (not recommended for production code)

    def stb_Submit(self, context):
        submit_Button = self.findElementByXpath(
            context, create_STBLocators.Submit)
        submit_Button.click()

        print("Successfully create STB")

    def stbValidation_BreadCrumb(self, context):
        # Locate the breadcrumb elements
        success_BreadCrumb = self.findElementByXpath(
            context, create_STBLocators.Success_BredCrumb
        )
        stb_added_successfully_BreadCrumb = self.findElementByXpath(
            context, create_STBLocators.STBaddedsuccessfully_BredCrumb
        )

        # Get the text from the located elements
        success_text = success_BreadCrumb.text
        stb_added_successfully_text = stb_added_successfully_BreadCrumb.text

        # Assert that the text matches the expected values
        assert (
            success_text == "Success!"
        ), f"Expected 'Success!' but got '{success_text}'"

        assert (
            stb_added_successfully_text == "STB added successfully"
        ), f"Expected 'STB added successfully' but got '{stb_added_successfully_text}'"

    def back_Stb_List(self, context):
        stb_List = self.findElementByXpath(
            context, create_STBLocators.STB_List)
        stb_List.click()
        print("STB List")
        time.sleep(10)

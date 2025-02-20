import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
import string
import random
import time
from faker import Faker

import autoit


class BasePage:
    def __init__(self):
        self = self

    def findElementByXpath(self, context, locator):
        try:
            element = context.waitdriver.until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        except Exception as e:
            context.logger.info("findElementByXpath Retry" + str(locator))
            element = context.waitdriver.until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        context.logger.info("Element Found" + str(locator))
        return element

    def findElementsByXpath(self, context, locator):
        try:
            elements = context.waitdriver.until(
                EC.visibility_of_all_elements_located((By.XPATH, locator))
            )
        except Exception as e:
            context.logger.info("findElementsByXpath Retry")
            elements = context.waitdriver.until(
                EC.visibility_of_all_elements_located((By.XPATH, locator))
            )

        return elements

    def findElementByXpathForInvisibility(self, context, locator):
        try:
            element = context.waitdriver.until(
                EC.invisibility_of_element_located((By.XPATH, locator))
            )
        except Exception as e:
            context.logger.info("findElementByXpathForInvisibility Retry")
            element = context.waitdriver.until(
                EC.invisibility_of_element_located((By.XPATH, locator))
            )
        return element

    def generateRandomFirstName(self):
        # Generate a random string of a specified length
        random_string_length = 8
        random_string = "".join(
            random.choice(string.ascii_letters) for _ in range(random_string_length)
        )
        print("Random String:", random_string)
        return random_string

    def generateRandomLastName(self):
        # Generate a random string of a specified length
        random_string_length = 5
        random_string = "".join(
            random.choice(string.ascii_letters) for _ in range(random_string_length)
        )
        print("Random String:", random_string)
        return random_string

    def generateRandomInteger(self):
        # Generate a random integer between a specified range (inclusive)
        random_integer = random.randint(8000000000, 9000000000)
        print("Random Integer:", random_integer)
        return random_integer

    # Other methods in your BasePage class

    def selectDesriedValue(self, context, elements, value):
        # Loop through the elements
        for element in elements:
            # Check if the element's text matches the desired text
            if element.text == str(value):
                # Click the element
                element.click()
                # Break the loop if the desired element is found
                context.logger.info("Value selected is " + str(value))

                break

    def concatFilePathForAddNewCustomer(self, context, folderPath, fileName):
        folderPath = os.getcwd() + folderPath
        # Concatenate folder paths
        full_path = os.path.join(folderPath, fileName)
        context.logger.info(f"Full file path: {full_path}")
        return full_path

    def uploadFileInDesktop(self, filePath):
        autoit.win_wait_active("[Title:Open]", 10)
        autoit.control_send("[Title:Open]", "Edit1", f"{filePath}")
        time.sleep(2)
        autoit.control_click("[Title:Open]", "Button1")

    def selectValueFromList(
        self, context, InputFieldLocator, listLocator, value, fieldName
    ):
        inputField = self.findElementByXpath(context, InputFieldLocator)
        self.scrollIntoCenterView(context, inputField)
        inputField.click()

        # Find list of result
        listElement = self.findElementsByXpath(context, listLocator)
        # self.scrollIntoCenterView(context, listElement)
        context.logger.info("Found " + str(fieldName))

        self.selectDesriedValue(context, listElement, value)
        context.logger.info("value selected for " + str(fieldName))

    def scrollIntoCenterView(self, context, element):
        context.driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });",
            element,
        )
        time.sleep(1)

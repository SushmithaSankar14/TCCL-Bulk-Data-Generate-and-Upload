import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
import string
import random
import time
from faker import Faker


class BroadcasterCreateActions:
    def __init__(self):
        self = self

    def generateRandomBroadcasterName():
        # Initialize a Faker instance
        fake = Faker()

        # Generate a random name
        randomBroadcasterName = fake.name()
        # Concatenate the random name with "Broadcaster"
        fullName = f"{randomBroadcasterName} Broadcaster"

        return fullName

    def generate_random_10_digit_number():
        # The first digit should be between 6 and 9
        first_digit = str(random.randint(6, 9))

        # The remaining 9 digits should be between 0 and 9
        remaining_digits = "".join([str(random.randint(0, 9)) for _ in range(9)])

        # Concatenate the first digit with the remaining digits
        random_10_digit_number = first_digit + remaining_digits

        return random_10_digit_number

    def generateContactName():
        # Initialize a Faker instance
        fake = Faker()

        # Generate a random name
        randomContactName = fake.name()

        return randomContactName

    def enterValue(context, locator, value):
        fieldElement = context.BasePage.findElementByXpath(context, locator)
        fieldElement.clear()
        fieldElement.send_keys(value)

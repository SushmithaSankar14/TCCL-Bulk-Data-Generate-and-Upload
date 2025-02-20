import time
from features.utils.data import payment_data
from utils.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from features.actions.paymentMenuActions import paymentsActionMenu
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.utils.paymentLocators import payments_Locators
import pdb


class paymentPage(BasePage):
    def __init__(self):
        super().__init__()

    def clickPaymentModule_page(self, context, value):
        paymentsActionMenu.clickMenuList(
            context, value)

    def clickSubMenu_Individual_LCO_Deposit(self, context, value):
        paymentsActionMenu.click_submenu_list(
            context, value
        )
        # Assert
        userFilter_BreadCrumb = self.findElementByXpath(
            context, payments_Locators.UserFilter_BredCrumb
        )
        # Get the text from the located elements
        UserFilter_text = userFilter_BreadCrumb.text
        context.logger.info(f"Retrieved breadcrumb text: '{UserFilter_text}'")

        # Assert that the text matches the expected values
        assert (
            UserFilter_text == "User Filter"
        ), f"Expected 'User Filter' but got '{UserFilter_text}'"

    def selectUserType(self, context, value):
        paymentsActionMenu.selectValueFromList(
            context, payments_Locators.UserType_Locator,
            payments_Locators.UserType_List,
            value, "UserType"
        )

    def selectBusinessName(self, context, value):
        paymentsActionMenu.clickElementFound(
            context, payments_Locators.Business_Name, "BusinessName Element click")
        paymentsActionMenu.selectValueFromList(
            context, payments_Locators.Business_Name,
            payments_Locators.BusinessName_List,
            value, "BusinessName"
        )

        time.sleep(3)

    def clickApplyBtn(self, context):
        paymentsActionMenu.clickElementFound(
            context, payments_Locators.Apply_Btn, "ApplyBtn"
        )
        # Assert
        LCOList_BreadCrumb = self.findElementByXpath(
            context, payments_Locators.LCOList_BredCrumb
        )
        # Get the text from the located elements
        LCOList_text = LCOList_BreadCrumb.text
        context.logger.info(f"Retrieved breadcrumb text: '{LCOList_text}'")

        # Assert that the text matches the expected values
        assert (
            LCOList_text == "LCO List"
        ), f"Expected 'Distributor' but got '{LCOList_text}'"

        # Opening balance Check

        # Retrieve the breadcrumb text
        walletBalance_BreadCrumb = self.findElementByXpath(
            context, payments_Locators.Wallet_balance)

        # Remove leading/trailing spaces
        balance_text = walletBalance_BreadCrumb.text.strip().replace(',', '')

        # Log the retrieved balance text
        context.logger.info(f"Retrieved breadcrumb text: '{balance_text}'")

        # Convert the retrieved balance text to a numerical value
        try:
            current_balance = float(balance_text)
        except ValueError:
            context.logger.error(f"Unable to convert'{balance_text}'to a numerical value.")
            raise

        # Define the value to be added
        # Replace this with the actual value you want to add
        added_value = float(payment_data.amount)

        # Calculate the expected balance
        expected_balance = current_balance + added_value

        # Log the calculated expected balance
        context.logger.info(
            f"Calculated expected balance:'{expected_balance}'"
        )
        context.expected_balance = expected_balance

        # Assert that the balance matches the expected value
        assert (expected_balance == (current_balance + added_value)
                ), (f'Expected {expected_balance} but got {current_balance + added_value}')

        # Log the successful addition
        context.logger.info(
            f"Balance updated correctly to:'{expected_balance}'"
        )

    def clickWalletImg(self, context):
        paymentsActionMenu.clickElementFound(
            context, payments_Locators.Wallet_img, "Wallet Img"
        )
        time.sleep(4)

    def enterAmount(self, context, value):
        paymentsActionMenu.enterValue(
            context, payments_Locators.Amount, value
        )
        time.sleep(5)

    def selectPaymentMode(self, context, value):
        paymentsActionMenu.selectValueFromList(
            context, payments_Locators.PaymentMode_DropDown,
            payments_Locators.PaymentMode_DropDown_List,
            value, "PaymentMode"
        )

    def enterRecipteNo(self, context, value):
        paymentsActionMenu.enterValue(
            context, payments_Locators.Recipte_No, value
        )

    def enterRemarks(self, context, value):
        paymentsActionMenu.enterValue(
            context, payments_Locators.Remarks, value
        )

    def clickDepositBtn(self, context):
        paymentsActionMenu.clickElementFound(
            context, payments_Locators.Deposite_Btn, "DepositBtn"
        )

        # Assert
        AfterDeposit_BreadCrumb = self.findElementByXpath(
            context, payments_Locators.MoneyDeposited_Success
        )
        # Get the text from the located elements
        moneyDeposit_text = AfterDeposit_BreadCrumb.text
        context.logger.info(f"Retrieved breadcrumb text:'{moneyDeposit_text}'")

        # Assert that the text matches the expected values
        assert (
            moneyDeposit_text == moneyDeposit_text
        ), f"Expected 'moneyDeposit_text' but got '{moneyDeposit_text}'"

    def clickAfterMoneyDeposit(self, context):
        paymentsActionMenu.clickElementFound(
            context, payments_Locators.Deposite_Okay_Btn, "OkayBtn"
        )
        # Assert
        # Retrieve the breadcrumb text
        afterDepositBalance_BreadCrumb = self.findElementByXpath(
            context, payments_Locators.Wallet_balance)
        # Remove leading/trailing spaces
        balance_text = afterDepositBalance_BreadCrumb.text.strip().replace(',', '')
        context.logger.info(f"Retrieved breadcrumb text: '{balance_text}'")

        # Convert the retrieved balance text to a numerical value
        try:
            after_deposit_balance = float(balance_text)
        except ValueError:
            context.logger.error(f"Unable to convert'{balance_text}' to a numerical value.")
            raise

        # Retrieve the expected balance from context
        expected_balance = getattr(context, 'expected_balance', None)

        # Assert that the balance matches the expected value
        assert after_deposit_balance == expected_balance, f"Expected '{expected_balance}' but got '{after_deposit_balance}'"

        # Log the successful balance verification

        context.logger.info(f"Balance verified successfully as: '{after_deposit_balance}'")

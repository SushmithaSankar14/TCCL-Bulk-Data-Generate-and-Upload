
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.utils.data import Add_Customer
from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage


from utils.locators import *
import time


class CustomerPage(BasePage):
    def __init__(self):
        super().__init__()

    def CustomerModule_page(self, context):
        Customer_ICON = self.findElementByXpath(
            context, CustomerModuleLocators.Customer_Icon)

        Customer_ICON.click()
        time.sleep(3)

    def AddNew_Customer(self, context):
        AddNewBtn = self.findElementByXpath(
            context, CustomerModuleLocators.AddNew_Customer
        )

        AddNewBtn.click()
        time.sleep(2)

    def selectPrefix(self, context, value):
        self.selectValueFromList(
            context,
            CustomerModuleLocators.Tittle,
            CustomerModuleLocators.OptionsList,
            value,
            "Prefix",

        )

    # FIRSTNAME

    def Customer_First_Name(self, context):
        first_name = self.findElementByXpath(
            context, CustomerModuleLocators.First_Name
        )
        first_name.send_keys(context.BasePage.generateRandomFirstName())

        print('Sushmitha')
     # LASTTNAME

    def Customer_Last_Name(self, context):
        last_name = self.findElementByXpath(
            context, CustomerModuleLocators.Last_Name
        )
        last_name.send_keys(context.BasePage.generateRandomLastName())

        print('Sankar')
        time.sleep(5)

    def cutomer_Gender(self, context, value):
        self.selectValueFromList(context,
                                 CustomerModuleLocators.Select_Gender,
                                 CustomerModuleLocators.Select_Gender_List,
                                 value,
                                 "Gender",

                                 )
        print('Gender')

    def cutomer_LCO(self, context, value):
        self.selectValueFromList(context,
                                 CustomerModuleLocators.Select_LCO,
                                 CustomerModuleLocators.select_LCO_List,
                                 value,
                                 "AbiramiDistributorKannanSubDistributor08360797689794 - Test LCO User",

                                 )
        print('AbiramiDistributorKannanSubDistributor08360797689794 - Test LCO User')

    def cutomer_Type(self, context, value):
        self.selectValueFromList(context,
                                 CustomerModuleLocators.Select_Customer_Type,
                                 CustomerModuleLocators.Select_Customer_Type_List,
                                 value,
                                 "Hotel",

                                 )
        print('Hotel')

    def billing_Type(self, context, value):
        self.selectValueFromList(context,
                                 CustomerModuleLocators.Billing_Type,
                                 CustomerModuleLocators.Billing_Type_List,
                                 value,
                                 "Prepaid",

                                 )
        print('Female')

    def sLA(self, context, value):
        self.selectValueFromList(context,
                                 CustomerModuleLocators.SLA,
                                 CustomerModuleLocators.SLA_List,
                                 value,
                                 "Standard",

                                 )
        print('Standard')

        time.sleep(5)

    def Customer_User_Name(self, context):
        user_name = self.findElementByXpath(
            context, CustomerModuleLocators.user_Name
        )
        user_name.send_keys(context.BasePage.generateRandomFirstName())

        print('Username')

    def customer_Password(self, context):
        Password = context.BasePage.findElementByXpath(
            context, CustomerModuleLocators.password
        )
        Password.click()
        customerPassword = Add_Customer.password
        Password.send_keys(customerPassword)
        keyboard.press_and_release('tab')
        print('password')

    def Customer_Address_Line1(self, context):
        address_Line1 = self.findElementByXpath(
            context, CustomerModuleLocators.Addres_Line1
        )
        address_Line1.send_keys(context.BasePage.generateRandomFirstName())

        print('Address1')

    def Customer_Address_Line2(self, context):
        address_Line2 = self.findElementByXpath(
            context, CustomerModuleLocators.Address_Line2
        )
        address_Line2.send_keys(context.BasePage.generateRandomFirstName())

        print('Address2')

    def customer_PinCode(self, context):
        pinCode_Value = context.BasePage.findElementByXpath(
            context, CustomerModuleLocators.Pincode
        )
        pinCode_Value.click()
        customerPincode = Add_Customer.PinCode
        pinCode_Value.send_keys(customerPincode)
        keyboard.press_and_release('tab')
        print('pincode')

    def customer_City(self, context):
        customer_city = self.findElementByXpath(
            context, CustomerModuleLocators.city
        )
        customer_city.send_keys(context.BasePage.generateRandomFirstName())

        print('salem')

    def customer_Mobile_Number(self, context):
        address_Line2 = self.findElementByXpath(
            context, CustomerModuleLocators.Mobile_Number
        )
        address_Line2.send_keys(context.BasePage.generateRandomInteger())

        print('mobilenumber')
        time.sleep(3)

    def next_Arrow(self, context):
        next_Arrow_Element = self.findElementByXpath(
            context, CustomerModuleLocators.next_arrow
        )
        next_Arrow_Element.click()
        time.sleep(5)

    def customer_ID_Type(self, context, value):
        self.selectValueFromList(context,
                                 CustomerModuleLocators.id_Type,
                                 CustomerModuleLocators.id_Type_List,
                                 value,
                                 "PAN",

                                 )
        print('PAN')

    def customer_ID_Number(self, context):
        customer_ID_Number_Element = self.findElementByXpath(
            context, CustomerModuleLocators.id_Number
        )
        customer_ID_Number_Element.send_keys("123434")

    def customer_ID_Proof_Upload(self, context, folderPath, fileName):
        # Correct folderPath
        folderPath = "\\features\\utils\\files\\"
        # Construct the full file path
        full_path = self.concatFilePathForAddNewCustomer(
            context, folderPath, fileName)

        # Find the upload element and click it
        # customer_ID_Proof = self.findElementByXpath(
        #     context, CustomerModuleLocators.id_Proof_Upload
        # )
        # customer_ID_Proof.click()

        # # Wait for the file dialog to open
        # time.sleep(2)
        self.uploadFileInDesktop(full_path)

    def customer_Details_saved(self, context):
        cutomer_Details = self.findElementByXpath(
            context, CustomerModuleLocators.saved_cutomer_Details
        )
        cutomer_Details.click()
        print('Saved Successfully')

        time.sleep(5)

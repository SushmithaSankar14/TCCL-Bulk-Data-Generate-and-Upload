from features.pages.base_page import BasePage
from features.actions.broadcasterCreateActions import BroadcasterCreateActions
from features.pages.login_page import LoginPage
from features.utils.data import Add_Customer
from features.utils.channelsLocators import (
    ChannelsModuleLocator,
    ChannelsBroadcasterList,
    BroadcasterCreationEntryFields,
    PopMessage,
    BroadcasterListCreationBtn,
)
from selenium.webdriver.common.keys import Keys


class BroadcasterListPage(BasePage, BroadcasterCreateActions):
    def __init__(self):
        super().__init__()

    def moveToChannels(self, context):
        channelsElement = self.findElementByXpath(
            context, ChannelsModuleLocator.channelsMainTab
        )
        channelsElement.click()

        # verify redirection with its Menu
        channelsMenuSideTextElement = self.findElementByXpath(
            context, ChannelsModuleLocator.channelsRedirection
        )

    def moveToBroadcasterList(self, context):
        broadcasterListElement = self.findElementByXpath(
            context, ChannelsModuleLocator.broadcasterListMenu
        )
        broadcasterListElement.click()

        # verify BroadcasterList redirection
        broadcasterAppTableTitleElement = self.findElementByXpath(
            context, ChannelsModuleLocator.broadcasterListAppTableRedirection
        )

    def clickCreateBroadcasterBtn(self, context):
        createBroadcasterBtnElement = self.findElementByXpath(
            context, ChannelsBroadcasterList.createBroadcasterBtn
        )
        createBroadcasterBtnElement.click()

        # verify redirection by finding broadcasterName
        broadcasterNameFieldElement = self.findElementByXpath(
            context, BroadcasterCreationEntryFields.broadcasterNameField
        )

    def enterBroadcasterName(self, context, broadcasterName):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.broadcasterNameField,
            broadcasterName,
        )

    def enterContactName(self, context, contactName):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.contactNameField,
            contactName,
        )

    def enterBroadcasterMobileNumber(self, context, broadcasterMobileNumber):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.broadcasterMobileNumberField,
            broadcasterMobileNumber,
        )

    def enterContactPhoneNumber(self, context, contactPhoneNumber):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.contactPhoneNumberField,
            contactPhoneNumber,
        )

    def enterEmail(self, context, email):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.emailField,
            email,
        )

    def enterAddress1(self, context, address1):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.addressLine1Field,
            address1,
        )

    def enterAddress2(self, context, address2):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.addressLine2Field,
            address2,
        )

    def enterAddress3(self, context, address3):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.addressLine3Field,
            address3,
        )

    def enterCity(self, context, city):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.cityField,
            city,
        )

    def enterPin(self, context, Pin):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.pinField,
            Pin,
        )

    def enterDistrict(self, context, District):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.district,
            District,
        )

    def enterState(self, context, State):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.state,
            State,
        )

    def enterCountry(self, context, Country):
        BroadcasterCreateActions.enterValue(
            context,
            BroadcasterCreationEntryFields.country,
            Country,
        )
        context.logger.info("country value entered")

    def clickCreate(self, context):
        createBtn = self.findElementByXpath(
            context, BroadcasterListCreationBtn.enabledCreateBtn
        )
        createBtn.click()
        context.logger.info("Clicked create btn for broadcaster")

        # verify redirection by finding broadcasterName
        successPopMessage = self.findElementByXpath(
            context, PopMessage.broadcasterCreationSuccessfulMessage
        )
        context.logger.info("Broadcaster successfully created")

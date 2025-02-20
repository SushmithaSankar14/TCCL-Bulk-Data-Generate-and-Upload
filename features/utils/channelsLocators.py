class ChannelsModuleLocator:
    channelsMainTab = "//img[@alt='channels']"
    channelsRedirection = "//app-sidebar-menu//ul//li[normalize-space()='Channels']"
    broadcasterListMenu = "//li[normalize-space()='Channels']//..//ul//li//span[normalize-space()='Broadcaster List']"
    broadcasterListAppTableRedirection = (
        "//app-table//div//span[normalize-space()='Broadcaster List']"
    )
    channelListMenu = "//li[normalize-space()='Channels']//..//ul//li//span[normalize-space()='Channel List']"
    channelInfoMenu = "//li[normalize-space()='Channels']//..//ul//li//span[normalize-space()='Channel Info']"


class ChannelsBroadcasterList:
    createBroadcasterBtn = "//button[normalize-space()='+ Create Broadcaster']"
    broadcasterDetailsTitleCreatePage = "//label[@id='broadcasterDetails']"


class BroadcasterCreationEntryFields:
    broadcasterNameField = "//input[@id='broadcasterName']"
    contactNameField = "//input[@id='contactName']"
    broadcasterMobileNumberField = "//input[@id='mobileNumber']"
    contactPhoneNumberField = "//input[@id='phoneNumber']"
    emailField = "//input[@id='email']"
    addressLine1Field = "//input[@id='address1']"
    addressLine2Field = "//input[@id='address2']"
    addressLine3Field = "//input[@id='address3']"
    cityField = "//input[@id='city']"
    pinField = "//input[@id='pincode']"
    district = "//input[@id='district']"
    state = "//input[@id='state']"
    country = "//input[@id='country']"
    bankName = "//input[@id='bankName']"
    branchField = "//input[@id='branchName']"
    ifscCodeField = "//input[@id='ifscCode']"
    AccountNumberField = "//input[@id='accountNumber']"
    gstNumberField = "//input[@id='gstNumber']"


class BroadcasterListCreationBtn:
    enabledCreateBtn = "//button[normalize-space()='Create' and not(@disabled)]"
    cancelBtn = "//button[normalize-space()='Cancel']"
    addChannelsBtn = "//button[normalize-space()='Add Channels']"
    later = "//button[normalize-space()='Later']"


class PopMessage:
    broadcasterCreationSuccessfulMessage = "//div//div[contains(text(),'Broadcaster is created successf')]//..//..//div[normalize-space()='Successful!']"

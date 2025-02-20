class LoginPageLocators:
    """
    Locators for the SMS login page elements.
    """
    userName = "//div//input[@formcontrolname='username']"
    password = "//div//input[@formcontrolname='password']"
    loginBtn = "//button[normalize-space()='Login']"
    loadingInLoginPage = "//span[normalize-space()='Loading...']"
    tcclLogoInTopLeft = (
        "//img[@src='../assets/images/tccl-logo.png' and @alt='tccl logo']"
    )
    userNameAfterLogin = "(//div//p)[1]"


class SMSLoginPageLocators:
    userName = "//div//input[@formcontrolname='username']"
    password = "//div//input[@formcontrolname='password']"
    loginBtn = "//button[normalize-space()='Login']"
    loadingInLoginPage = "//span[normalize-space()='Loading...']"
    tcclLogoInTopLeft = "//img[@alt='tccl logo']"


class UsersModuleLocators:
    Bread_Crumb = "//a[@class='text-bread-cum-title font-bread-cum-title opacity-50 cursor-pointer']"
    Users_ICON = "//li[@class='pt-2']//div/img[@alt='users']"
    Download_PDF_Icon = "//img[@alt='pdf']"
    Download_CSV_Icon = "//img[@alt='csv']"


class UserListLocators:
    addNewUser = "//button[normalize-space()='+ Add New User']"
    userTypesListField = "//label[normalize-space()='User Types*']//..//ng-select//div[@class='ng-input']//input"
    userTypesListValue = "//ng-dropdown-panel//div[@role='option']//span"


class CustomerModuleLocators:

    Customer_Icon = "//img[@alt='subscriber']"
    AddNew_Customer = "//button[@class='primary-action']"
    Tittle = "//ng-select[@id='criteria']//span[@class='ng-arrow-wrapper']"
    OptionsList = "//ng-dropdown-panel[@aria-label='Options list']//span[text()]"
    First_Name = "//input[@id='firstName']"
    Last_Name = "//input[@id='lastName']"
    Select_Gender = "//ng-select[@id='gneder']//span[@class='ng-arrow-wrapper']"
    Select_Gender_List = (
        "//ng-dropdown-panel[@class='ng-dropdown-panel ng-select-bottom']//span[text()]"
    )
    Select_LCO = "//ng-select[@id='lcoId']//span[@class='ng-arrow-wrapper']"
    select_LCO_List = (
        "//ng-dropdown-panel[@class='ng-dropdown-panel ng-select-bottom']//span[text()]"
    )
    Select_Customer_Type = (
        "//ng-select[@id='subscriberType']//span[@class='ng-arrow-wrapper']"
    )
    Select_Customer_Type_List = (
        "//ng-dropdown-panel[@class='ng-dropdown-panel ng-select-bottom']//span[text()]"
    )
    Business_Name = "//input[@id=businessName]"
    Billing_Type = "//ng-select[@id='billingType']//span[@class='ng-arrow-wrapper']"
    Billing_Type_List = (
        "//ng-dropdown-panel[@class='ng-dropdown-panel ng-select-bottom']//span[text()]"
    )
    SLA = "//ng-select[@id='sla']//span[@class='ng-arrow-wrapper']"
    SLA_List = "//div[@class='ng-option ng-option-marked']//span[text()]"
    Addres_Line1 = "//input[@id='address1']"
    Address_Line2 = "//input[@id='address2']"
    Address_Line3 = "//input[@id='pincode']"
    Pincode = "//input[@id='pincode']"
    Mobile_Number = "//input[@id='mobileNumber']"
    city = "//input[@id = 'city']"
    next_arrow = "//img[@alt='right arrow']"
    id_Type = "//span[@class='ng-arrow-wrapper']"
    id_Type_List = "//div[@class='ng-dropdown-panel-items scroll-host']//span[text()]"
    id_Number = "//input[@id='idProofNumber']"
    id_Proof_Upload = "//label[normalize-space()='ID Proof Upload*']//..//span[normalize-space()='Select']"
    saved_cutomer_Details = "//button[@class='primary-action']"
    user_Name = "//input[@formcontrolname='userName']"
    password = "//input[@formcontrolname='password']"


class create_STBLocators:
    STB_Icon = "//img[@alt='STB menu']"
    Add_STB = "//button[@class='primary-action']"
    Server_Type = "//ng-select[@id='serverType']//span[@class='ng-arrow-wrapper']"
    Server_Type_List = (
        "//div[@class='ng-dropdown-panel-items scroll-host']//span[text()]"
    )
    Chip_id = "//input[@id='chipId']"
    CAS_id = "//input[@id='casId']"
    Select_Model = "//ng-select[@id='model']//span[@class='ng-arrow-wrapper']"
    Select_Model_List = (
        "//div[@class='ng-dropdown-panel-items scroll-host']//span[text()]"
    )
    STB_Type = "//ng-select[@id='stbType']//span[@class='ng-arrow-wrapper']"
    STB_Type_List = "//div[@class='ng-dropdown-panel-items scroll-host']//span[text()]"
    Submit = "//button[normalize-space()='Submit']"
    Success_BredCrumb = "//h4[normalize-space()='Success!']"
    STBaddedsuccessfully_BredCrumb = "//p[normalize-space()='STB added successfully']"
    STB_List = "//li[@class='py-2 !px-4 cursor-pointer mt-5 text-balance side-menu-item-active']"


class stbMenu_Locators:
    STB_Icon = "//img[@alt='STB menu']"
    STB_BredCrumb = "//span[@class='py-2']"
    STB_Table = "//table[@class='w-full']"
    STBList_FirstValueChipID = "//tbody/tr[1]/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    STB_BulkOperations = "//span[normalize-space()='Bulk Operations']"
    STB_Uploadlog_BredCrumb = "/html/body/app-root/app-layout/div/div/div/div[2]/main/app-bulk-operations/div/div[1]/app-table/div/div[1]/div[1]/span"
    UploadLog_Table = "//div[@class='relative overflow-x-auto overflow-y-auto shadow-md']"
    FirstValue_TransactionID = "/html/body/app-root/app-layout/div/div/div/div[2]/main/app-bulk-operations/div/div[1]/app-table/div/div[2]/table/tbody/tr[1]/td[2]/div"
    STB_VCPairing = "//span[normalize-space(text())= 'STB VC Pairing/Unpairing']"
    STB_VCPairing_BredCrumb = "/html/body/app-root/app-layout/div/div/div/div[2]/main/app-stb-vc-pairing-list/div/div[2]/app-table/div/div[1]/div[1]/span"
    STB_VCPairing_Table = "//div[@class='relative overflow-x-auto overflow-y-auto shadow-md']"
    STBVCPairing_FirstValueChipID = "//tbody/tr[1]/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    STB_Replace = "//li[@class='py-2 !px-4 cursor-pointer mt-5 rounded-3xl text-balance side-menu-item-active']"
    STB_SendMessage = "//span[normalize-space()='Send Message']"
    STB_Span = "//span[@class='py-2']"
    STB_MessageList_Table = "//div[@class='relative overflow-x-auto overflow-y-auto shadow-md']"
    STB_MessageList_FirstValue = "/html/body/app-root/app-layout/div/div/div/div[2]/main/app-send-message-list/div/div[2]/app-table/div/div[2]/table/tbody/tr[1]/td[2]/div/app-table-column-format/div/div"
    STB_Create = "//span[normalize-space()='Create STB']"
    Create_STB_Log = "//span[normalize-space()='Create STB Log']"
    Create_Stb_Log_table = "//table[@class='w-full']"
    pdf_icon = "//div[@class='cursor-pointer w-8 h-8 pdf-icon']"
    csv_icon = "//div[@class='cursor-pointer w-8 h-8 csv-icon']"
    new_stb = "//button[@class='primary-action']"
    create_individual_stb_Breadcrumb = "//a[@class='breadcrum-text opacity-100']"
    bulk_Button = "//button[normalize-space()='Bulk']"
    create_bulk_stb_breadcrumb = "//a[@class='breadcrum-text opacity-100']"
    upload_stb_file = "//div[@for='fileInput']"
    # "//div[@for='fileInput']"
    #  "//input[@id='fileInput']"
    import_button = "//button[normalize-space()='Import']"
    bulkstb_uploadlof_table = "//table[@class='w-full']"
    firstvaluof_bulk_uploadlog_table = "//tbody/tr[1]/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    file_uploded_success_msg = "//h4[normalize-space()='Success!']"
    file_uploded_successfully = "//p[normalize-space()='File uploaded successfully for STB Create']"
    refersh_btn = "//div[@class='flex items-center tooltip py-2']//*[name()='svg']"
    process_locator = "//div[normalize-space()='Process']/ancestor::table//tbody/tr[1]/td[4]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    status_Locator = "//div[normalize-space()='Status']/ancestor::table//tbody/tr[1]/td[6]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    error_file_Locator = "//div[normalize-space()='Error File']/ancestor::table//tbody/tr[5]/td[8]/div[1]/app-table-column-format[1]/div[1]/div[1]/div[1]/a[2]/img[1]"
    error_file_text = "//div[@class='max-h-64 mt-3 overflow-y-auto sm:ml-4 sm:mt-0 sm:text-left text-center w-full']"
    close_btn_Locator = "//button[normalize-space()='Close']"
    transactionIDLogs_Locator = "//div[normalize-space()='Transaction ID']/ancestor::table//tbody/tr[1]/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    filter_Locator = "//button[normalize-space()='Filter']"
    transactionID_locator = "//input[@id='transactionId']"
    apply_Btn_Locator = "//button[normalize-space()='Apply']"
    serialnumber_List_Locator = "//tbody/tr/td[3]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    clear_Btn_Locator = "//button[normalize-space()='Clear']"



class userMenu_Locators:
    UserList_BredCrumb = "//span[@class='py-2']"
    UserList_Table = "//table[@class='w-full']"
    UserTable_FirstName = "//tbody/tr[1]/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    UploadLog_BredCrumb = "//span[@class='py-2']"
    UploadLog_Table = "//table[@class='w-full']"
    UploadLog_FirstTransactionID = "//tbody/tr[1]/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    LCO_Blocked_Products_List = "//span[@class='py-2']"
    LCO_Blocked_Products_List_Table = "//table[@class='w-full']"
    LCO_Blocked_Products_List_FirstLCOBusinessName = "//tbody/tr[1]/td[2]/div[1]/app-table-column-format[1]/div[1]/div[1]"


class transfer_STB_Locators:
    TransferSTB_Bredcrumb = "//a[@class='breadcrum-text opacity-100']"
    pdf_icon = "//div[@class='cursor-pointer w-8 h-8 pdf-icon']"
    csv_icon = "//div[@class='cursor-pointer w-8 h-8 csv-icon']"
    bulk_transfer_stb_bredcrumb = "//a[@class='breadcrum-text opacity-100']"
    Stb_new_transfer = "//button[@class='primary-action']"
    upload_stb_transfer_file = "//div[@for='fileInput']"
    import_button = "//button[normalize-space()='Import']"
    file_uploded_success_msg = "//h4[normalize-space()='Success!']"
    file_uploded_successfully = "//p[normalize-space()='File uploaded successfully for STB Create']"
    STBID_Locator = "//tbody/tr/td[4]/div[1]/app-table-column-format[1]/div[1]/div[1]"


class bulkOperations_Locators:
    bulkoperations_Bredcrumb = "//a[@class='breadcrum-text opacity-100']"
    uploadlog_Table = "//table[@class='w-full']"
    action_Types = "//ng-select[@id='actionType']//input[@type='text']"
    action_Types_List = "//ng-dropdown-panel[@role='listbox']//span[text()]"
    upload_stb_list_file = "//div[@for='fileInput']"
    reason = "//ng-select[@id='reason']//input[@type='text']"
    reason_List = "//ng-dropdown-panel[@role='listbox']//span[text()]"
    import_button = "//button[normalize-space()='Import']"
    file_uploded_success_msg = "//h4[normalize-space()='Success!']"
    file_uploded_successfully = "//p[normalize-space()='File uploaded successfully for STB Create']"


class subscriber_Locators:
    subscriberList_Bredcrumb = "//a[@class='breadcrum-text opacity-100']"
    subscriber_First_name = "//input[@id='firstName']"

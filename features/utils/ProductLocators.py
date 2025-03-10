class ProductLocators:

    add_Product = "//button[normalize-space()='+ Add Product']"
    bulk_Button = "//button[normalize-space()='Bulk']"
    server_types = "//ng-select[@id='serverTypes']//input[@type='text']"
    server_type_List = "//ng-dropdown-panel[@role='listbox']//div[@role='option']"
    upload_files = "//div[@for='fileInput']"
    import_Btn = "//button[normalize-space()='Import']"
    bulkstb_uploadlod_table = "//table[@class='w-full']"
    file_uploded_success_msg = "//h4[normalize-space()='Success!']"
    file_uploded_successfully = "//p[normalize-space()='File uploaded successfully for STB Create']"
    refersh_btn = "//div[@class='flex items-center tooltip py-2']//*[name()='svg']"
    process_locator = "//div[normalize-space()='Process']/ancestor::table//tbody/tr[1]/td[3]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    status_Locator = "//div[normalize-space()='Status']/ancestor::table//tbody/tr[1]/td[5]/div[1]/app-table-column-format[1]/div[1]/div[1]"
    error_file_Locator = "//div[normalize-space()='Error File']/ancestor::table//tbody/tr[5]/td[8]/div[1]/app-table-column-format[1]/div[1]/div[1]/div[1]/a[2]/img[1]"
    error_file_text = "//div[@class='max-h-64 mt-3 overflow-y-auto sm:ml-4 sm:mt-0 sm:text-left text-center w-full']"
    productNameLocator = "//input[@id='productName']"
    filter_Locator = "//button[normalize-space()='Filter']"
    search_Btn = "//button[normalize-space()='Search']"

from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from utils.locators import UsersModuleLocators
import time


class UsersPage(BasePage):
    def __init__(self):
        super().__init__()

    def users_list_page(self, context):
        Users_ICON = self.findElementByXpath(
            context, UsersModuleLocators.Users_ICON)

        Users_ICON.click()
        time.sleep(5)

    def users_Validate_page(self, context, usersList):
        userValidationPageBreadcrumb = self.findElementByXpath(
            context, UsersModuleLocators.Bread_Crumb
        )
        
        usersList = "User List"
        assert (
            usersList == userValidationPageBreadcrumb.text
         )
        # f"Actual text: {"usersList"}, Expected text: {userValidationPageBreadcrumb.text}"
        time.sleep(5)
        print("userlist successfully")
        
    def steps_click_download_userlist_pdf (self, context):
        Download_PDF_Icon = self.findElementByXpath(
            context, UsersModuleLocators.Download_PDF_Icon)
        
        Download_PDF_Icon.click()
        time.sleep(10)
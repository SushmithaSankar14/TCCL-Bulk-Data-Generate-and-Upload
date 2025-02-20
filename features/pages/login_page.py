# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()

    def naviagte_to_tccl_SMS_login(self, context, tcclSMSLoginUrl):
        print(tcclSMSLoginUrl)
        context.driver.get(tcclSMSLoginUrl)

    def enter_UserName_and_Password(self, context, userName, password, config_reader):
        print("enter_UserName_and_Password")
        print(context.env)
        if context.env == "live":
            userNameField = context.BasePage.findElementByXpath(
                context, LoginPageLocators.userName
            )
            userNameField.send_keys(
                config_reader.get_tccl_SMS_UserName(context.env))
            time.sleep(1)

            passwordField = context.BasePage.findElementByXpath(
                context, LoginPageLocators.password
            )
            passwordField.send_keys(
                config_reader.get_tccl_SMS_Password(context.env))
            time.sleep(1)

        elif context.env == "PreProd":
            userNameField = context.BasePage.findElementByXpath(
                context, LoginPageLocators.userName
            )
            userNameField.send_keys(
                config_reader.get_tccl_SMS_UserName(context.env))
            time.sleep(1)

            passwordField = context.BasePage.findElementByXpath(
                context, LoginPageLocators.password
            )
            passwordField.send_keys(
                config_reader.get_tccl_SMS_Password(context.env))
            time.sleep(1)
        elif context.env == "stage":
            userNameField = context.BasePage.findElementByXpath(
                context, LoginPageLocators.userName
            )
            userNameField.send_keys(
                config_reader.get_tccl_SMS_UserName(context.env))
            time.sleep(1)

            passwordField = context.BasePage.findElementByXpath(
                context, LoginPageLocators.password
            )
            passwordField.send_keys(
                config_reader.get_tccl_SMS_Password(context.env))
            time.sleep(1)

    def click_continueBtn(self, context):
        print("click_continueBtn")
        print(context.env)
        if context.env == "live":
            loginBtn = context.BasePage.findElementByXpath(
                context, LoginPageLocators.loginBtn
            )
            loginBtn.click()

            # validate Redirection
            loadingText = context.BasePage.findElementByXpathForInvisibility(
                context, LoginPageLocators.loadingInLoginPage
            )
            tcclLogo = context.BasePage.findElementByXpath(
                context, LoginPageLocators.tcclLogoInTopLeft
            )
            # userNameAfterLogin = context.BasePage.findElementByXpath(
            #     context, LoginPageLocators.userNameAfterLogin
            # )
            # print(userNameAfterLogin.text)
            time.sleep(5)

        elif context.env == "PreProd":
            loginBtn = context.BasePage.findElementByXpath(
                context, LoginPageLocators.loginBtn
            )
            loginBtn.click()

            # validate Redirection
            loadingText = context.BasePage.findElementByXpathForInvisibility(
                context, LoginPageLocators.loadingInLoginPage
            )
            tcclLogo = context.BasePage.findElementByXpath(
                context, LoginPageLocators.tcclLogoInTopLeft
            )

            # userNameAfterLogin = context.BasePage.findElementByXpath(
            #     context, LoginPageLocators.userNameAfterLogin
            # )
            # print(userNameAfterLogin.text)
            time.sleep(5)

        elif context.env == "stage":
            loginBtn = context.BasePage.findElementByXpath(
                context, LoginPageLocators.loginBtn
            )
            loginBtn.click()

            # validate Redirection
            loadingText = context.BasePage.findElementByXpathForInvisibility(
                context, LoginPageLocators.loadingInLoginPage
            )
            tcclLogo = context.BasePage.findElementByXpath(
                context, LoginPageLocators.tcclLogoInTopLeft
            )

            # userNameAfterLogin = context.BasePage.findElementByXpath(
            #     context, LoginPageLocators.userNameAfterLogin
            # )
            # print(userNameAfterLogin.text)
            time.sleep(5)

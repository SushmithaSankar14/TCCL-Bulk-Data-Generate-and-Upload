from lib2to3.pgen2 import driver
from behave import given, when, then
from requests import options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from selenium.webdriver.remote.webelement import WebElement
from utils.config_reader import ConfigReader
import os
import time
from utils.locators import *

from features.pages.bulkupload_page import bulkUpload
from features.pages.subscriberBulkCreate_page import bulkUploadSubscriberCreatePage
from selenium.webdriver.common.action_chains import ActionChains
from features.pages.bulkdatagenerate_page import DataGenerator
from features.pages.bulkTestAPI_page import APIrsponseCheck


import autoit

config_reader = ConfigReader()


@then("click Create STB")
def steps_create_stb(context):
    context.bulkupload_page.steps_click_create_stb(context, "Create STB")
    context.bulkupload_page.click_new_stb(context)
@then("bulk Upload Create STB")
def steps_bulk_Upload_Create_STB(context):
    context.bulkupload_page.bulk_upload_stb(context)
@then("after Upload Verify the stb")
def steps_after_Upload_Verify_the_STB(context):
    transactionID_Text=context.bulkupload_page.after_upload_verify(context)

    # context.STB_Search_page.afterUpload_TransactionID_Search(
    #     context, transactionID_Text)

    # context.STB_Search_page.after_TransactionID_Search_SerialNumberverify(
    #     context)
    file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/main_data.csv"
    context.STB_Search_page.verify_serial_number_search_from_csv(context,file_path)



# @then("Create STB API Response check")
# def stpes_create_STB_API_check(context):
#     generated_stb_numbers = DataGenerator.generate_bulk_stb_numbers(10)
#     logging.info(f"Generated STB numbers: {generated_stb_numbers}")

#     # Verify STB numbers using the API
#     transaction_id = "82160791730271"
#     final_filtered_stb_numbers = APIrsponseCheck.verify_serial_number_with_pagination(
#         transaction_id, generated_stb_numbers)

#     # Output results
#     logging.info(f"Final filtered STB numbers: {final_filtered_stb_numbers}")


@then("click Transfer STB and upload")
def steps_click_transfer_stb_and_uplod(context):
    context.bulkupload_page.bulkupload_transfer_stb(context, "Transfer STB")
    context.bulkupload_page.click_new_transfer_stb(context)
    transactionID_Text=context.bulkupload_page.bulk_upload_stb_transfer(context)
    file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/transfer_data.csv"
    context.transferSTB_page.afterUpload_TransactionID_Search(context,transactionID_Text)
    context.transferSTB_page.after_TransactionID_and_SerialNumberverify(context,file_path)
    context.transferSTB_page.verify_serial_number_and_lco_from_csv(context,file_path)


@then("Upload bulk Create Subscriber")
def steps_upload_bulk_create_subscriber(context):
    context.subscriberBulkCreate_page.click_subscriber_Menu(
        context, "subscriber")
    context.subscriberBulkCreate_page.click_subscriber_bulkOperations(
        context, "Bulk Operations")
    context.subscriberBulkCreate_page.create_bulk_subscriber(
        context, "Create")
    context.subscriberBulkCreate_page.upload_CreateSubscriber_bulk_file(
        context)
    file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/subscriber_data.csv"
    # column_names = ["First Name*"]
    context.subscriberID_search_page.afterUpload_Search_SubName(context,file_path)


@then("Upload bulk data for STB Deactivation")
def steps_upload_bulk_data(context):
    context.bulkupload_page.upload_Deactive_data_file(
        context, "Deactivation")
    context.bulkupload_page.choose_reason_Deactivate(
        context, "Temporary Deactivation")
    context.bulkupload_page.bulk_upload_stb_Deactivation(context)


@then("Upload bulk data for STB Reactivation")
def steps_upload_bulk_data(context):
    context.bulkupload_page.upload_reactivate_data_file(
        context, "Reactivation")

    context.bulkupload_page.choose_reason_Reactivate(
        context, "Activation Pack Change")
    context.bulkupload_page.bulk_upload_stb_Reactivation(context)


@then("Upload bulk data for STB deactivation reasons deactivated by MSO")
def steps_upload_bulk_data(context):
    context.bulkupload_page.upload_Deactive_data_file(
        context, "Deactivation")
    context.bulkupload_page.choose_reason(context, "Deactivate by MSO")
    context.bulkupload_page.bulk_upload_stb_Deactivation(context)


@then("Upload bulk data for STB Activation reasons Trial pack")
def steps_upload_bulk_data(context):
    context.bulkupload_page.upload_activation_data_file(
        context, "Activation")
    context.bulkupload_page.choose_reason_Activate(context, "Trial pack")
    context.bulkupload_page.bulk_upload_stb_Activation(context)

@then ("Upload Bulk data for Product")
def steps_upload_bulk_data(context):
    context.bulkproductcreate_page.click_products_menu(context, "product")
    context.bulkproductcreate_page.click_add_product(context)
    context.bulkproductcreate_page.create_bulk_product(context,"Sumavision")
    context.bulkproductcreate_page.upload_Product_bulk_file(context)

@then("After upload verify Product")
def steps_after_upload_verify_product(context):
    file_path = "D:/Automation/tccl-sms/TestAutomation-SMS/TestAutomation-SMS/features/files/product_create_data.csv"
    # column_names = ["Product Name*"]
    context.ProductVerification_page.afterUpload_Search_ProductName(context,file_path)

@then("Upload Bulk Intro LCO Transfer")
def steps_upload_bulk_data(context):
    context.transferSTB_page.upload_intro_LCO_transfer_file(context, "Intro LCO Transfer")
    context.transferSTB_page.bulk_upload_intro_LCO_transfer(context)

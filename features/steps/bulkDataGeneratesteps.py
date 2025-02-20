import sys
import pandas as pd
from features.pages.bulkdatagenerate_page import BulkDataGenerator
import os
from behave import when, then
from features.utils.config_reader import ConfigReader
# from behave.runner import Context

# config_reader = ConfigReader()


@when("generate Bulkdata")
def generate_bulk_data(context):
    context.env = os.getenv("ENV")
    """
   Generates bulk data and stores it in the context.
   """

    context.num_rows = 2  # Example: Set number of rows to generate

    config_reader = ConfigReader("config.ini")  # Read configuration

    # Generate the STB data and store it in the context
    context.generated_data = BulkDataGenerator.generate_stb_data(
        context,
        context.num_rows,
        config_reader.get_tccl_sms_productname(context.env),
        config_reader.get_tccl_sms_lcoID(context.env),
        config_reader.get_tccl_sms_source_LCoID(context.env),
        config_reader.get_tccl_sms_destination_LCoID(context.env),
        config_reader)

    print("Generated Data:", context.generated_data)


@then("verify the data is generated correctly")
def verify_data_generated_correctly(context):
    (
        main_data, transfer_data, activate_data, reactivate_data,
        subscriber_data, intra_lco_data, product_create_data,
        cash_payment_data, bank_payment_data, online_payment_data, bulk_STB_Block_Unblock_data, bulk_STB_VC_Pair_Unpair_data, bulk_STB_Product_Clear_data
    ) = context.generated_data

    # Convert to DataFrames for saving or verification
    main_df = pd.DataFrame(main_data)
    transfer_df = pd.DataFrame(transfer_data)
    activate_df = pd.DataFrame(activate_data)
    reactivate_df = pd.DataFrame(reactivate_data)
    subscriber_df = pd.DataFrame(subscriber_data)
    intra_lco_df = pd.DataFrame(intra_lco_data)
    product_create_df = pd.DataFrame(product_create_data)
    cash_payment_df = pd.DataFrame(cash_payment_data)
    bank_payment_df = pd.DataFrame(bank_payment_data)
    online_payment_df = pd.DataFrame(online_payment_data)
    block_unblock_df = pd.DataFrame(bulk_STB_Block_Unblock_data)
    Pair_Unpair_data_df = pd.DataFrame(bulk_STB_VC_Pair_Unpair_data)
    Product_Clear_data_df = pd.DataFrame(bulk_STB_Product_Clear_data)

    # Define folder path where CSVs will be saved
    folder_path = 'D:\\Automation\\tccl-sms\\TestAutomation-SMS\\TestAutomation-SMS\\features\\files'

    # Create the folder if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Define the file names for each CSV
    main_csv_path = os.path.join(folder_path, 'main_data.csv')
    transfer_csv_path = os.path.join(folder_path, 'transfer_data.csv')
    activate_csv_path = os.path.join(folder_path, 'activate_data.csv')
    reactivate_csv_path = os.path.join(folder_path, 'reactivate_data.csv')
    subscriber_csv_path = os.path.join(folder_path, 'subscriber_data.csv')
    intra_lco_csv_path = os.path.join(folder_path, 'intra_lco_data.csv')
    product_create_csv_path = os.path.join(
        folder_path, 'product_create_data.csv')
    cash_payment_csv_path = os.path.join(folder_path, 'cash_payment_data.csv')
    bank_payment_csv_path = os.path.join(folder_path, 'bank_payment_data.csv')
    online_payment_csv_path = os.path.join(
        folder_path, 'online_payment_data.csv')
    block_unblock_csv_path = os.path.join(
        folder_path, 'block_unblock_data.csv')
    Pair_Unpair_data_csv_path = os.path.join(
        folder_path, 'Pair_Unpair_data.csv')
    Product_Clear_data_csv_path = os.path.join(
        folder_path, 'Product_Clear_data.csv')

    # Save the DataFrames to CSV in the specified folder
    main_df.to_csv(main_csv_path, index=False)
    transfer_df.to_csv(transfer_csv_path, index=False)
    activate_df.to_csv(activate_csv_path, index=False)
    reactivate_df.to_csv(reactivate_csv_path, index=False)
    subscriber_df.to_csv(subscriber_csv_path, index=False)
    intra_lco_df.to_csv(intra_lco_csv_path, index=False)
    product_create_df.to_csv(product_create_csv_path, index=False)
    cash_payment_df.to_csv(cash_payment_csv_path, index=False)
    bank_payment_df.to_csv(bank_payment_csv_path, index=False)
    online_payment_df.to_csv(online_payment_csv_path, index=False)
    block_unblock_df.to_csv(block_unblock_csv_path, index=False)
    Pair_Unpair_data_df.to_csv(Pair_Unpair_data_csv_path, index=False)
    Product_Clear_data_df.to_csv(Product_Clear_data_csv_path, index=False)

    # Print confirmation messages
    print(f"CSV files have been saved in the folder: {folder_path}")
    print(f"Files saved: {main_csv_path}, {transfer_csv_path}, {activate_csv_path}, {reactivate_csv_path}, {subscriber_csv_path}, {intra_lco_csv_path}, {product_create_csv_path}, {cash_payment_csv_path}, {bank_payment_csv_path}, {online_payment_csv_path},{block_unblock_csv_path},{Pair_Unpair_data_csv_path},{Product_Clear_data_csv_path}")

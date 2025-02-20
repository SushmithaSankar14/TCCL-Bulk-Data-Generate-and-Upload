import random
import string
from features.pages.base_page import BasePage
from features.utils.config_reader import ConfigReader


class DataGenerator:
    """Utility class for generating random data for bulk processing."""

    @staticmethod
    def generate_stb_number():
        """Generate a random STB number."""
        return f"{random.randint(330004010, 3400800010)}"

    @staticmethod
    def generate_bulk_stb_numbers(count):
        """Generate a list of random STB numbers."""
        return [DataGenerator.generate_stb_number() for _ in range(count)]

    @staticmethod
    def generate_name():
        """Generate a random 6-character name."""
        return ''.join(random.choices(string.ascii_uppercase, k=6))

    @staticmethod
    def generate_mobile_number():
        """Generate a random 10-digit mobile number."""
        return f"{random.randint(9867546789, 9868124789)}"

    @staticmethod
    def generate_pan_number():
        """Generate a random PAN number."""
        first_three = ''.join(random.choices(string.ascii_uppercase, k=3))
        fourth_char = 'P'
        fifth_char = random.choice(string.ascii_uppercase)
        four_digits = ''.join(random.choices(string.digits, k=4))
        last_char = random.choice(string.ascii_uppercase)
        return f"{first_three}{fourth_char}{fifth_char}{four_digits}{last_char}"

    @staticmethod
    def generate_unique_names(product_line,count):
        """Generate a list of unique product names."""
        unique_names = [
            f"{product_line}_{i:03d}" for i in range(1, count + 1)
        ]
        return unique_names

    @staticmethod
    def generate_unique_amount():
        return f"{random.randint(1, 1000000)}"


class BulkDataGenerator(BasePage):
    """Class to generate bulk STB data."""

    @staticmethod
    def generate_stb_data(context, num_rows, productName, lcoID, sourceLcoID, destinationLcoID, config_reader):
        # context.env = "preprod"
        """Generate bulk data for STB operations."""
        product_line, count ="AutoProduct", 10

        static_data = {
            "Server Type(Sumavision/ Verimatrix/ Gospell)*": "Sumavision",
            "Model(PANODIC_SD/ SKARDIN_SD/ YINHE_SD/ YINHE_HD/ YINHE_888HD/ YINHE_777HD/ YINHE_666HD/ YINHE_ZAPPER_HD/ OVT_SD/ OVT_HD)*": "YINHE_HD",
            "Company Make(PANODIC/ SKARDIN/ YINHE/ OVT)*": "YINHE",
            "PO Number*": "PO12345",
            "Invoice Number*": "INV67890",
            "STB Type(HD/ SD)*": "HD",
            "Warranty Type(Days/ Months /Years)*": "Years",
            "Warranty Period*": "3"
        }
        subscriber_static_data = {
            # "Products": config_reader.get_tccl_sms_productname(section, env),
            "Products": config_reader.get_tccl_sms_productname(context.env),
            "Gender(Male/Female/Others)*": "Male",
            "LCO Business Code*": config_reader.get_tccl_sms_lcoID(context.env),
            "Billing Type(Prepaid/Postpaid)*": "Prepaid",
            "Subscriber Type*(Residence/Commercial/Hotel/Hospital/Office/PublicPlace/Others)": "Residence",
            "Address Line 1*": "Salem",
            "Address Line 2*": "Salem",
            "Pincode*": "636119",
            "State*": "Tamil nadu",
            "District*": "Salem",
            "City*": "Salem",
            "Email ID*": "susisankarece@gmail.com",
            "ID Type*(AadhaarCard/DrivingLicense/ElectricityBill/PAN/Passport/RationCard/VoterID)": "PAN"
        }

        product_create_static_data = {
            "Validity Type* (Days/Months/Years)": "Months",
            "Validity*": "10",
            "Product Type(AlaCarte/BasePackage/BroadcasterPackage/DPOPackage)*": "BasePackage",
            "Broadcaster Name": "",
            "Bill Type*(Prepaid/Postpaid)": "Prepaid",
            "Recurring Period (Monthly/Yearly)": "",
            "Base Price*": "75.50",
            "Tax Template (None/GST/NEWGST)*": "GST",
            "LCO Share Type* (Amount/Percentage)": "Amount",
            "LCO Share*": "5",
            "Distributor Percentage (%)": "",
            "Sub Distributor Percentage (%)": "",
            "SumaVision VC Number*": "1244",
            "VeriMatrix VC Number*": "765",
            "Gospell VC Number*": "557",

        }

        rows = []
        transfer_stb_vc_rows = []
        activate_rows = []
        reactivate_rows = []
        subscriber_create_rows = []
        intra_lco_transfer_rows = []
        product_create_bulk_rows = []
        bulk_lco_deposit_cash_payment_rows = []
        bulk_lco_deposit_bank_payment_rows = []
        bulk_lco_deposit_online_payment_rows = []
        bulk_STB_Block_Unblock = []
        bulk_STB_VC_Pair_Unpair = []
        bulk_STB_Product_Clear = []

        for _ in range(num_rows):
            stb_number = DataGenerator.generate_stb_number()
            name = DataGenerator.generate_name()
            mobile = DataGenerator.generate_mobile_number()
            pan = DataGenerator.generate_pan_number()
            amount = DataGenerator.generate_unique_amount()

            # Main Data
            rows.append({
                "Server Type(Sumavision/ Verimatrix/ Gospell)*": static_data["Server Type(Sumavision/ Verimatrix/ Gospell)*"],
                "Serial Number*": stb_number,
                "VC Number*": stb_number,
                "Model(PANODIC_SD/ SKARDIN_SD/ YINHE_SD/ YINHE_HD/ YINHE_888HD/ YINHE_777HD/ YINHE_666HD/ YINHE_ZAPPER_HD/ OVT_SD/ OVT_HD)*": static_data["Model(PANODIC_SD/ SKARDIN_SD/ YINHE_SD/ YINHE_HD/ YINHE_888HD/ YINHE_777HD/ YINHE_666HD/ YINHE_ZAPPER_HD/ OVT_SD/ OVT_HD)*"],
                "Company Make(PANODIC/ SKARDIN/ YINHE/ OVT)*": static_data["Company Make(PANODIC/ SKARDIN/ YINHE/ OVT)*"],
                "PO Number*": static_data["PO Number*"],
                "Invoice Number*": static_data["Invoice Number*"],
                "STB Type(HD/ SD)*": static_data["STB Type(HD/ SD)*"],
                "Warranty Type(Days/ Months /Years)*": static_data["Warranty Type(Days/ Months /Years)*"],
                "Warranty Period*": static_data["Warranty Period*"]

            })

            # Transfer Data
            transfer_stb_vc_rows.append({
                "STB ID(Serial Number/VC Number)*": stb_number,
                "Source*": "HO",
                "Destination*": config_reader.get_tccl_sms_lcoID(context.env)
                # SDD1733228008689
            })

            # Activate Data
            activate_rows.append({
                "STB ID* (Serial Number/VC Number)": stb_number,
                "Product Name*": config_reader.get_tccl_sms_productname(context.env)
                # "PREMIUM 01"
            })

            # Reactivate Data
            reactivate_rows.append({
                "STB ID* (Serial Number/VC Number)": stb_number
            })

            # Subscriber Data
            subscriber_create_rows.append({
                "Serial Number": stb_number,
                "Products": subscriber_static_data["Products"],
                "Reason(TrialPack/ActivationPackChange/PaymentMade/CAFUpload/UndergoingIntraLcoTransfer/TemporaryActivation)": "TrialPack",
                "Remarks": "Test Remarks",
                "First Name*": name,
                "Last Name": "",
                "Gender(Male/Female/Others)*": subscriber_static_data["Gender(Male/Female/Others)*"],
                "LCO Business Code*": subscriber_static_data["LCO Business Code*"],
                "Billing Type(Prepaid/Postpaid)*": subscriber_static_data["Billing Type(Prepaid/Postpaid)*"],
                "Subscriber Type*(Residence/Commercial/Hotel/Hospital/Office/PublicPlace/Others)": subscriber_static_data["Subscriber Type*(Residence/Commercial/Hotel/Hospital/Office/PublicPlace/Others)"],
                "Business Name": "",
                "Address Line 1*": subscriber_static_data["Address Line 1*"],
                "Address Line 2*": subscriber_static_data["Address Line 2*"],
                "Address Line 3": "",
                "Pincode*": subscriber_static_data["Pincode*"],
                "State*": subscriber_static_data["State*"],
                "District*": subscriber_static_data["District*"],
                "Mandal/ Taluk": "",
                "City*": subscriber_static_data["City*"],
                "Telephone Number": "",
                "Mobile Number*": mobile,
                "Email ID*": subscriber_static_data["Email ID*"],
                "ID Type*(AadhaarCard/DrivingLicense/ElectricityBill/PAN/Passport/RationCard/VoterID)": subscriber_static_data["ID Type*(AadhaarCard/DrivingLicense/ElectricityBill/PAN/Passport/RationCard/VoterID)"],
                "ID Number*": pan
            })

            # Intra-LCO Transfer
            intra_lco_transfer_rows.append({
                "Id*": stb_number,
                "Source LCO*": config_reader.get_tccl_sms_source_LCoID(context.env),
                # "SDD1733228008689",
                "Destination LCO*": config_reader.get_tccl_sms_destination_LCoID(context.env)
                # "DSD1730288963375"
            })

            # Product Creation
            product_create_bulk_rows.append({
                "Product Name*": f"{product_line}_{random.randint(1, 999):03d}",
                "Validity Type* (Days/Months/Years)": product_create_static_data["Validity Type* (Days/Months/Years)"],
                "Validity*": product_create_static_data["Validity*"],
                "Product Type(AlaCarte/BasePackage/BroadcasterPackage/DPOPackage)*": product_create_static_data["Product Type(AlaCarte/BasePackage/BroadcasterPackage/DPOPackage)*"],
                "Broadcaster Name": "",
                "Bill Type*(Prepaid/Postpaid)": product_create_static_data["Bill Type*(Prepaid/Postpaid)"],
                "Recurring Period (Monthly/Yearly)": "",
                "Base Price*": product_create_static_data["Base Price*"],
                "Tax Template (None/GST/NEWGST)*": product_create_static_data["Tax Template (None/GST/NEWGST)*"],
                "LCO Share Type* (Amount/Percentage)": product_create_static_data["LCO Share Type* (Amount/Percentage)"],
                "LCO Share*": product_create_static_data["LCO Share*"],
                "Distributor Percentage (%)": "",
                "Sub Distributor Percentage (%)": "",
                "SumaVision VC Number*": product_create_static_data["SumaVision VC Number*"],
                "VeriMatrix VC Number*": product_create_static_data["VeriMatrix VC Number*"],
                "Gospell VC Number*": product_create_static_data["Gospell VC Number*"]

            })

            # Payments
            bulk_lco_deposit_cash_payment_rows.append({
                "LCO Code*": config_reader.get_tccl_sms_lcoID(context.env),
                # "SDD1733228008689",
                "Amount(Rs)*": amount,
                "Receipt No*": "12344",
                "Remarks*": "Test Cash Deposit"
            })

            bulk_lco_deposit_bank_payment_rows.append({
                "LCO Code*": config_reader.get_tccl_sms_lcoID(context.env),
                #  "SDD1733228008689",
                "Amount(Rs)*": amount,
                "Receipt No*": "12344",
                "Cheque/DD No": "",
                "Bank": "",
                "Branch": "",
                "Remarks*": "Test Cash Deposite"
            })

            bulk_lco_deposit_online_payment_rows.append({
                "LCO Code*": config_reader.get_tccl_sms_lcoID(context.env),
                # "SDD1733228008689",
                "Amount(Rs)*": amount,
                "Transaction ID*": "1234",
                "Remarks*": "Test Cash Online Deposit"
            })

            bulk_STB_Block_Unblock.append({
                "STB ID* (Serial Number/VC Number)": stb_number
            })

            bulk_STB_VC_Pair_Unpair.append({
                "STB ID* (Serial Number/VC Number)": stb_number
            })

            bulk_STB_Product_Clear.append({
                "STB ID* (Serial Number/VC Number)": stb_number,
                "Reason*": "Test Clear"
            })

        return (
            rows, transfer_stb_vc_rows, activate_rows, reactivate_rows,
            subscriber_create_rows, intra_lco_transfer_rows, product_create_bulk_rows,
            bulk_lco_deposit_cash_payment_rows, bulk_lco_deposit_bank_payment_rows, bulk_lco_deposit_online_payment_rows, bulk_STB_Block_Unblock, bulk_STB_VC_Pair_Unpair, bulk_STB_Product_Clear
        )

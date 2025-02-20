# config_reader.py
from configparser import ConfigParser


class ConfigReader:

    def __init__(self, config_file="config.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    # def get_value(self, section, key, env):
    #     """Fetch the value based on the section, key, and environment."""
    #     try:
    #         return self.config[section][env].strip()
    #     except KeyError as e:
    #         raise ValueError(f"Missing configuration for {
    #                          key} in {section} under {env}") from e

    def get_tccl_SMS_URL(self, key):
        return self.config.get("TCCL_SMS", key)

    def get_tccl_SMS_UserName(self, key):
        return self.config.get("UserName_SMS", key)

    def get_tccl_SMS_Password(self, key):
        return self.config.get("Password_SMS", key)

    def get_tccl_SMS_Users(self, key):
        return self.config.get("Users_SMS", key)

    # def get_tccl_sms_productname(self, section, env):
    #     return self.get_value(section, 'stage' if env == 'stage' else 'preprod', env)

    # def get_tccl_sms_lcoID(self, section, env):
    #     return self.get_value(section, 'stage' if env == 'stage' else 'preprod', env)

    # def get_tccl_sms_source_LCoID(self, section, env):
    #     return self.get_value(section, 'stage' if env == 'stage' else 'preprod', env)

    # def get_tccl_sms_destination_LCoID(self, section, env):
    #     return self.get_value(section, 'stage' if env == 'stage' else 'preprod', env)

    def get_tccl_sms_productname(self, key):
        return self.config.get("ProductName_sms", key)

    def get_tccl_sms_lcoID(self, key):
        return self.config.get("LCOID_sms", key)

    def get_tccl_sms_source_LCoID(self, key):
        return self.config.get("IntraLCOTransfer_SourceLCO_sms", key)

    def get_tccl_sms_destination_LCoID(self, key):
        return self.config.get("IntraLCOTransfer_DestinationLCO_sms", key)

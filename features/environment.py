from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


# before all
def before_all(context):
    print("Before all executed")


# before every scenario
# def before_scenario(scenario, context):
def before_scenario(context, scenario):
    print("Before scenario executed")


# after every feature
# def after_feature(feature, context):
def after_feature(context, feature):
    print("After feature executed")


# after all
def after_all(context):
    print("After all executed")

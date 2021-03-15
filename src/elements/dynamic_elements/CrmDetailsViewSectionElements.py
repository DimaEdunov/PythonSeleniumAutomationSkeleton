from enum import Enum
import time
from enum import Enum
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Section(Enum):
    # Details view section elements
    ADDRESS_INFORMATION = "Address Information"
    MARKETING_INFORMATION = "Marketing Information"
    CUSTOM_INFORMATION = "Custom Information"
    TRADING_ACCOUNTS = "Trading Accounts"
    FINANCIAL_TRANSACTIONS = "Financial Transactions"
    CLIENT_INFORMATION = "Client Information"
    HELP_DESK = "Help Desk"
    ACTIVITIES = "Activities"

    # Documents details view - section elements
    DOCUMENTS_BASIC_INFORMATION_SECTION = "Basic"


class SortButtonsValuesInSection(Enum):
    START_DATE = "Start Date"
    LOGIN = "Login"
    SERVER = "Server"

class SectionElements(object):

    # Open Section inside details view, ALL MODULES beside 'Documents'
    @staticmethod
    def open_section(driver, section_name):
        return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                        "//mat-expansion-panel-header[@aria-expanded='false']//mat-panel-title/div[contains(text(), '%s')]" % section_name)))


    # 'Open Section inside details view of 'Documents'
    @staticmethod
    def open_section_documents(driver, documents_section_name):
        return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                        "//mat-panel-title//div[contains(text(), '%s')]" % documents_section_name)))


    @staticmethod
    def sort_button(driver, column_name):

        return WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,
                                            "//*[contains(text(),' %s ')]//button" % column_name)))

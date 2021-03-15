import time
from enum import Enum

from selenium.webdriver.common.by import By


class SearchBar(Enum):
    # Affiliate Filter Enums
    PARTNER_ID = "Partner ID"
    PARTNER_NAME = "Partner Name"
    SECRET_KEY = "Secret Key"
    ASSIGNED_TO = "Assigned To"
    TRANSACTION_TYPE = "Transaction Type"
    CLIENT_NAME = "Client Name"
    TRANSACTION_NO = "Transaction No"
    CRM_ACCOUNT_NAME = "CRM Account Name"
    SERVER = "Server"
    TITLE = "Title"
    SUBJECT = "Subject"
    CRM_ID = "CRM Id"
    LEAD_NO = "Lead No"
    FIRST_NAME = "First Name"
    RELATED_TO = "Related To"
    DOCUMENT_NO = "Document No"
    FILE_NAME = "File Name"

    # Audit Logs Enums
    COLUMN_MODULE = "Module"
    COLUMN_ACTION = "Action"

    # Client Searchbar Enums
    EMAIL = "Email"

    # Tasks
    EVENT_TYPE = "Event type"
    ACCOUNT_NAME = "Account name"



    CLIENT_NAME_VALUE_ENVIRONMENT_PREPARATION = "dima edunov"

class SearchbarElements():

    # Once using this method, insert Enum variable from above
    @staticmethod
    def bar_choose_element(driver, filter_name):
        time.sleep(5)
        return driver.find_element(By.XPATH,
                                    "//span[contains(text(),'%s')]//following-sibling::div[@class='select-wrap']"
                                    % filter_name)

    # Once using this method, insert Enum variable from above
    @staticmethod
    def bar_insert_value_field_element(driver, filter_name):
            return driver.find_element(By.XPATH,
                                "//span[contains(text(),'%s')]//following-sibling::div[@class='select-wrap']//input[@placeholder='Search']"
                                % filter_name)
    @staticmethod
    def bar_choose_picklist_first_value(driver):
        SEARCHBAR_PICKLIST_ITEM_LIST = "//*[@class='input-wrap open']//ul//li"

        return driver.find_elements(By.XPATH, SEARCHBAR_PICKLIST_ITEM_LIST)[0]



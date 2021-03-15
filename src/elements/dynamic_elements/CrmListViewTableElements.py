import time
from enum import Enum
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Columns(Enum):
    COLUMN_FNAME = "First Name"
    COLUMN_LNAME = "Last Name"
    COLUMN_MOBILE = "Mobile"
    COLUMN_PHONE = "Phone"
    COLUMN_EMAIL = "Email"
    COLUMN_S_EMAIL = "Secondary email"
    COLUMN_TITLE = "Title"
    COLUMN_LANGUAGE = "Language"
    COLUMN_SOURCE_NAME = "Source Name"
    COLUMN_FAX = "Fax"
    COLUMN_REFERRAL = "Referral"
    COLUMN_ADDRESS = "Address"
    COLUMN_POSTAL_CODE = "Postal Code"
    COLUMN_CITY = "City"
    COLUMN_STATE = "State"
    COLUMN_PO_BOX = "PO Box"
    COLUMN_DESCRIPTION = "Description"
    COLUMN_LEAD_SOURCE = "Lead source"
    COLUMN_LEAD_STATUS = "Lead Status"
    COLUMN_ASSIGNED_TO = "Assigned To"
    COLUMN_COUNTRY = "Country"
    COLUMN_LEAD_NO = "Lead No"
    COLUMN_CREATED_TIME = "Created Time"
    CRM_ID = "CRM Id"
    LEADS_NO = "Lead No"
    DOCUMENTS_NO = "Document No"
    SUBJECT = "Subject"
    TRADING_ACCOUNT_LOGIN = "Trading Account Login"
    CLIENT_NAME = "Client Name"
    CLIENT_STATUS = "Client Status"
    COUNTRY = "Country"
    FIRST_NAME = "First Name"
    LAST_NAME = "Last Name"
    LEAD_STATUS = "Lead Status"
    TICKET_NO = "Ticket No"
    TITLE = "Title"
    STATUS = "Status"
    START_DATE = "Start date"



class SortTypes(Enum):
    ALPHABETICAL = "alphabetical"
    NUMERIC = "numeric"


class ColumnElements(object):

    @staticmethod
    def get_cell_element_by_column_name(driver, row, column_name):
        # Find all columns in the table
        table_columns = WebDriverWait(driver, 25).until(
            EC.presence_of_all_elements_located((By.XPATH, "//table/thead[@role='rowgroup']/tr/th")))

        # Locate the number of the defined column in the table
        column_number = (table_columns.index(driver.find_element(By.XPATH,
                                                                 "//table/thead[@role='rowgroup']/tr/th[contains(text(),'%s')]" % column_name)) + 1)

        if len(driver.find_elements(By.XPATH, "//table/tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))][%s]/td[%s]//span" % (row, column_number))) > 0:

            cell_element = driver.find_element(By.XPATH, "//table/tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))][%s]/td[%s]//span" % (row, column_number))

        else:

            cell_element = driver.find_element(By.XPATH,
                                               "//table/tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))][%s]/td[%s]" % (row, column_number))

        return cell_element

    @staticmethod
    def table_row_counter(driver):

        row_counter = len(driver.find_elements(By.XPATH,
                                                "//table/tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))]"))
        return row_counter

    @staticmethod
    def get_column_name_by_index(driver, index):

        column_name = WebDriverWait(driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, "//table/thead[@role='rowgroup']/tr/th[@role ='columnheader'][%s]" % index)))

        #  The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
        #  " CRM ID "  => "CRM ID"
        return driver.execute_script('return arguments[0].firstChild.textContent;', column_name).strip()

    @staticmethod
    def get_row_values_by_row_number(driver, row):
        column_list = []
        for counter in range(2, 20):
            text = ColumnElements.get_column_name_by_index(driver, counter)
            if text != ('More' and 'Actions'):
                column_list.append(text)
                # print(text)
            else:
                break

        row_values = {}
        for column in range(len(column_list)):
            text = ColumnElements.get_cell_element_by_column_name(driver, row, column_list[column]).text
            row_values[column_list[column]] = text
            # print(column_list[column], text)

        # Method return values as dictionary , for example,  dict = {key1 : value1, key2: value2}
        return row_values

    @staticmethod
    def convert_exported_values_to_lower_case(exported_values_dictionary):

        return {(''.join(c if c != '_' else ' ' for c in column_name)).lower().strip(): value.lower().strip() for column_name, value in exported_values_dictionary.items()}

    @staticmethod
    def select_record_via_checkbox_by_row_number(driver, row):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//tbody[@role='rowgroup']//tr[not(contains(@style,'hidden'))][%s]//label[@class='mat-checkbox-layout']" % row))).click()



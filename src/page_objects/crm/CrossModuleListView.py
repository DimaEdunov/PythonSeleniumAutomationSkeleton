import time
import random
import csv
from enum import Enum
import allure
import xlrd
import os
from allure_commons.types import AttachmentType

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.elements.dynamic_elements.CrmListViewTabsElements import TabElements
from src.elements.dynamic_elements.CrmListViewTableActionsMenuElements import ListViewActionsMenu
from src.infrastructure.dynamic_helpers.CssColorOfElement import CssColorOfElement
from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldNameConstants
from src.elements.dynamic_elements.CrmListViewTableElements import ColumnElements
from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmListViewFilterElements import Filters, FilterElements
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchbarElements, SearchBar
from src.page_objects.api.Api import ApiConstants
from src.infrastructure.dynamic_helpers.SwitchTo import SwitchTo


class CrossModuleInputs(Enum):
    LEADS = "leads"
    CLIENTS = "clients"


class ModuleNames(Enum):
    CLIENTS = "Clients"
    LEADS = "Leads"
    FINANCIAL_TRANSACTIONS = "MTTransactions"
    HELP_DESK = "HelpDesk"
    DOCUMENTS = "Documents"
    TASKS = "tasks"
    AFFILIATES = "affiliate"
    TRADING_ACCOUNTS = "Tradingaccounts"

class VerificationExportFields():
    CLIENTS = ['crm id', 'client name', 'email', 'client status', 'country', 'assigned to', 'created time', 'client source', 'ftd']
    LEADS = ['lead no', 'first name', 'last name', 'lead status', 'email', 'country', 'language', 'assigned to', 'created time', 'lead source', 'duplicate', 'last interaction date']
    FINANCIAL_TRANSACTIONS = ['transaction no', 'client', 'transaction type', 'currency', 'transaction approval', 'created time', 'original transaction owner',
                              'payment type', 'cleared by', 'payment processor', 'ftd', 'assigned to', 'country']
    HELP_DESK = ['ticket no', 'title', 'status', 'priority', 'created time', 'assigned to']
    DOCUMENTS = ['document no', 'attached to', 'document type', 'status', 'assigned to', 'file name', 'last status changed by', 'approved date']
    TASKS = ['event type', 'subject', 'status', 'account name', 'account status', 'country', 'assigned to', 'created by', 'department', 'brand',
             'local time', 'priority']
    AFFILIATES = ['partner name', 'enabled', 'allowed ip', 'blocked countries', 'allowed methods', 'brand']
    TRADING_ACCOUNTS = ['trading account login', 'crm account name', 'group', 'server', 'currency', 'assigned to']

class CrossModuleListView(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("CrossModuleListView.search_via_searchbar() | Use searchbar ")
    def search_via_searchbar(self, searchbar_name, searched_value):
        time.sleep(1.5)
        SearchbarElements.bar_choose_element(self.driver, searchbar_name.value).click()
        time.sleep(1.5)

        SearchbarElements.bar_insert_value_field_element(self.driver, searchbar_name.value).clear()

        time.sleep(2.5)
        SearchbarElements.bar_insert_value_field_element(self.driver, searchbar_name.value).send_keys(searched_value)
        time.sleep(1.5)

        if len(self.driver.find_elements(By.XPATH, CrmElements.FILTER_AGREE_BUTTON)) > 0:
            self.driver.find_element(By.XPATH, CrmElements.FILTER_AGREE_BUTTON).click()
        else:
            SearchbarElements.bar_choose_picklist_first_value(self.driver).click()
            self.driver.find_element(By.XPATH, CrmElements.FILTER_AGREE_BUTTON).click()

        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

    @allure.step("CrossModuleListView.go_to_via_saerchbar() | Go to list view (Clients / Leads) view by searchbar")
    def go_to_via_saerchbar(self, email_value, module_name):
        SearchbarElements.bar_choose_element(self.driver, SearchBar.EMAIL.value).click()

        SearchbarElements.bar_insert_value_field_element(self.driver, SearchBar.EMAIL.value).clear()

        SearchbarElements.bar_insert_value_field_element(self.driver, SearchBar.EMAIL.value).send_keys(email_value)

        time.sleep(1)
        self.driver.find_element(By.XPATH, CrmElements.FILTER_AGREE_BUTTON).click()

        WebDriverWait(self.driver, 50).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        if module_name == "leads":
            # Click on 'Lead number' from row 0
            crm_id = self.driver.find_elements(By.XPATH, CrmElements.LEAD_ID_LIST)[0]

            self.driver.execute_script("arguments[0].click();", crm_id)

            WebDriverWait(self.driver, 45).until(
                EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

            time.sleep(5)

        if module_name == "clients":
            # Click on 'Lead number' from row 0
            crm_id = self.driver.find_elements(By.XPATH, CrmElements.CRM_ID_LIST)[0]

            self.driver.execute_script("arguments[0].click();", crm_id)

            WebDriverWait(self.driver, 45).until(
                EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

            time.sleep(5)

    @allure.step("CrossModuleListView.search_via_searchbar_verification() | Verify results after using searchbar ")
    def search_via_searchbar_verification(self, refferenced_cell_value):
        time.sleep(3)
        match = False

        for cell_value in self.driver.find_elements(By.XPATH, CrmElements.LISTVIEW_FIRST_ROW_CELL_ITEMS_LIST):
            if refferenced_cell_value.lower() in cell_value.text.lower():
                print("verification passed")
                match = True
                time.sleep(0.5)
                break

        if not match:
            print("There was no match! ): ")
            assert False

    # Set test filter cross-module
    @allure.step("CrossModuleListView.set_test_filter() | Setting filter on ListView ")
    def set_test_filter(self, filter_value):
        time.sleep(5)
        client_filter = FilterElements.filter_choose_element(self.driver, filter_value)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", client_filter)

        WebDriverWait(self.driver, 45).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        time.sleep(10)

    # Search lead or client via global search
    @allure.step("CrossModuleListView.search_lead_or_client_via_search_bar() | Search lead or client via search bar")
    def search_lead_or_client_via_search_bar(self, searchbar_name, searched_value, who_is_searched):
        searched = {}
        # Find lead's id and email via search bar
        SearchbarElements.bar_choose_element(self.driver, searchbar_name.value).click()

        SearchbarElements.bar_insert_value_field_element(self.driver, searchbar_name.value).send_keys(
            searched_value)

        self.driver.find_element(By.XPATH, CrmElements.FILTER_AGREE_BUTTON).click()
        time.sleep(2)

        # Search for email and id in list view
        if who_is_searched == "Lead":
            searched['searched_id_in_search_bar_text'] = self.driver.find_elements(By.XPATH, CrmElements.LEAD_ID_LIST)[
                0].text
            searched['searched_email_in_search_bar'] = self.driver.find_elements(By.XPATH, CrmElements.LEAD_EMAIL_LIST)[
                0].text
        else:
            searched['searched_id_in_search_bar_text'] = self.driver.find_elements(By.XPATH, CrmElements.CRM_ID_LIST)[
                0].text
            searched['searched_email_in_search_bar'] = self.driver.find_elements(By.XPATH, CrmElements.CRM_EMAIL_LIST)[
                0].text

        return searched

    # Search lead or client via global search
    @allure.step(
        "CrossModuleListView.search_lead_or_client_via_global_search() | Search lead or client via global search")
    def search_lead_or_client_via_global_search(self, searched):

        # Find the lead via global search
        global_search = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_SEARCH)))

        global_search.click()
        global_search.send_keys(searched['searched_id_in_search_bar_text'])

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_MAGNIFYING_GLASS))).click()

        # Search for email in global search

        searched['searched_email_via_global_search'] = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.TEST_EMAIL_IN_GLOBAL_SEARCH))).text

        return searched

    # Search via global search verification
    @allure.step(
        "CrossModuleListView.search_lead_or_client_via_global_search_verification() | Verify the searched lead via global search is desirable lead")
    def search_lead_or_client_via_global_search_verification(self, searched):

        # If the email are not '***' and the are equal
        if searched['searched_email_in_search_bar'] != searched['searched_email_via_global_search'] \
                or searched['searched_email_in_search_bar'] == '****':

            first_screen_identifier = self.driver.window_handles[0]

            # Clicking on 'Client / Lead Link, new tab opens'

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.TEST_NAME_IN_GLOBAL_SEARCH))).click()

            time.sleep(7)

            # Get 'API's screen ID of screen 'SECOND SCREEN'
            second_screen_identifier = self.driver.window_handles[1]

            # Create object of SwitchTo
            switch_to_helper = SwitchTo(first_screen_identifier, second_screen_identifier, self.driver)

            # Switch to second screen ID -> 'API' screen
            switch_to_helper.switch_to("1")

            # Get second's screen URL -> 'API' screen
            second_screen_url = self.driver.current_url

            self.driver.close()

            # Switch back to 'FIRST SCREEN' - > CRM
            switch_to_helper.switch_to("0")

            # Open 'API' url in 'FIRST SCREEN'
            self.driver.get(second_screen_url)

            time.sleep(8)

            lead_no = self.driver.find_element(By.XPATH, CrmElements.LEAD_NO)

            if searched['searched_id_in_search_bar_text'] != lead_no.text:

                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_SEARCH))).clear()
                except:
                    pass

                allure.attach(self.driver.get_screenshot_as_png(),
                              name="search_lead_or_client_via_global_search_verification",
                              attachment_type=AttachmentType.PNG)
                assert False

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.CLOSE_GLOBAL_SEARCH_X_BUTTON))).click()
        except:
            pass

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_SEARCH))).clear()
        except:
            time.sleep(1.5)
            pass

    @allure.step("CrossModuleListView.switch_filter_tab() | Switching filter tab")
    def switch_filter_tab(self, filter_name):

        FilterElements.filter_tab_choose_element(self.driver, filter_name)

    def listview_phone_verification(self, expected_validation_type):
        if expected_validation_type == "valid":
            if len(self.driver.find_elements(By.XPATH, CrmElements.LISTVIEW_VALID_PHONE_ICON_FIRST)) > 0 and \
                    self.driver.find_element(By.XPATH,
                                             CrmElements.LISTVIEW_PHONE).text == ApiConstants.PHONE_VALID.value or '****':
                print("List verification was successful")

            else:
                assert False

        if expected_validation_type == "invalid":
            if len(self.driver.find_elements(By.XPATH, CrmElements.LISTVIEW_INVALID_PHONE_ICON_FIRST)) > 0 and \
                    self.driver.find_element(By.XPATH,

                                             CrmElements.LISTVIEW_PHONE).text == FieldNameConstants.INVALID_PHONE_A.value or '****':
                print("List verification was successful")

            else:
                assert False

    def get_number_of_cells_of_a_table(self):
        pass
        "//table/tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))][]/td[2]//span"

    @allure.step("CrossModuleListView.sort() | Help Desk sort")
    def sort(self, table_column_name):

        # Locate element, the reason 'column_name' is not passed here, is because the 'sort' button
        sort_up_button_element = ListViewActionsMenu.column_sort_button(self.driver, table_column_name.value)

        # Create an object for testing css colors before and after a click
        sort_button_color_change = CssColorOfElement(self.driver, sort_up_button_element)

        # Get the color of the element
        sort_button_color_change.extract_color_of_element()

        # Click on the element
        sort_up_button_element.click()

        time.sleep(2)

        # Re-check the color of the element
        sort_button_color_change.extract_color_of_element()

        # Get status whether the color of the element changed or not before / after the click
        # If the status is False, then the test will FAIL
        sort_button_color_change.check_color_change()

        tested_values = []

        row_counter = ColumnElements.table_row_counter(self.driver)
        for counter in range(1, row_counter + 1):
            try:

                text = ColumnElements.get_cell_element_by_column_name(self.driver, counter, table_column_name.value).text
                tested_values.append(text.lower())
            except:
                break

        sorted_tested_values = tested_values.copy()
        print(sorted_tested_values)

        sorted_tested_values.sort()

        # for counter in range(1,len(tested_values)):
        #     print("Counter : " + str(counter))
        #     print("Core list value  :" +str(tested_values[counter]))
        #     print("Sorted list value  :" +str(sorted_tested_values[counter]))
        #
        #     if tested_values[counter] != sorted_tested_values[counter]:
        #         print("Values are not equal - Successful PASSED")

        flag = 0
        i = 2
        while i < len(tested_values):
            if (sorted_tested_values[i] < sorted_tested_values[i - 1]):
                flag = 1
            i += 1

        # printing result
        if (not flag):
            print("Yes, List is sorted.")
        else:
            print("No, List is not sorted.")

    def choose_tab_with_verification(self, tab_name):

        record_sample_before_click = TabElements.get_number_of_records(self.driver)
        print("Number of records sample - BEFORE switching tab : " + str(record_sample_before_click))

        time.sleep(3)

        TabElements.choose_tab_element(self.driver, tab_name).click()

        time.sleep(4)

        record_sample_after_click = TabElements.get_number_of_records(self.driver)
        print("Number of records sample - AFTER switching tab : " + str(record_sample_after_click))

        if record_sample_before_click != record_sample_after_click:
            print("Verification passed")
        else:
            print("Verification failed")
            assert False

    def choose_tab_without_verification(self, tab_name):


        time.sleep(3)

        TabElements.choose_tab_element(self.driver, tab_name).click()

        time.sleep(4)

    def export_records(self, file_format, export_scope='export_selected_records'):

        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.REFRESH_BUTTON))).click()

        time.sleep(1)

        # Getting the number of rows in the CRM for export.
        number_selected_records = ColumnElements.table_row_counter(self.driver)
        print('number_selected_records: ' + str(number_selected_records))

        number_of_all_records = int(TabElements.get_number_of_records(self.driver))
        print('number_of_all_records: ' + str(number_of_all_records))

        # Getting the value of the random row for further export verification.
        if number_of_all_records == 1:
            crm_table_random_row_number = 1
        else:
            crm_table_random_row_number = random.randrange(1, number_selected_records)
            print("crm_table_random_row_number: " + str(crm_table_random_row_number))

        # Getting values from the list view for further verification(comparison), based on the random row, hence each time the values are different.
        crm_table_random_row_values = ColumnElements.get_row_values_by_row_number(self.driver, crm_table_random_row_number)
        print(crm_table_random_row_values.items())

        # Collecting the test data for transferring into verification method.
        if export_scope == 'export_selected_records':
            test_data = [number_selected_records, crm_table_random_row_number, crm_table_random_row_values]

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.SELECT_ALL_ITEMS_BUTTON))).click()
        elif export_scope == 'export_full_list':
            test_data = [number_of_all_records, crm_table_random_row_number, crm_table_random_row_values]

        else:
            print("wrong value inserted into export_scope")

        # Export file
        time.sleep(2)

        if file_format == 'affiliate':

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.AFFILIATES_EXPORT_BUTTON))).click()
            print("Affiliate export clicked")
        else:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.TOP_EXPORT_BUTTON))).click()

            if file_format == 'csv':
                time.sleep(1)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, CrmElements.CSV_CHECKBOX))).click()
                print("CSV clicked")
            else:
                time.sleep(0.5)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, CrmElements.EXCEL_CHECKBOX))).click()
                print("Excel clicked")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.EXPORT_CONFIRM_BUTTON))).click()

        time.sleep(25)

        return test_data

    def export_verification(self, file_name, file_format, test_data, fields_to_test):
        print("Verification")

        row_counter = test_data[0]
        crm_table_random_row_number = test_data[1]
        crm_table_random_row_values = ColumnElements.convert_exported_values_to_lower_case(test_data[2])

        if file_format == 'csv':
            # Reading CSV
            path = ("C:\web-automation-downloads\%s.csv" % file_name)
            with open(path, 'rt', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)

                #  Reading the whole file, row by row.
                exported_rows = []
                for raw in reader:
                    exported_rows.append(raw)

                # Getting the number of rows in export file.
                rows_in_export = len(exported_rows)

                # Getting values from a file based on the same random row as in CRM.
                export_values = ColumnElements.convert_exported_values_to_lower_case(exported_rows[crm_table_random_row_number - 1])
                print(export_values.items())

        else:
            # Reading Excel
            path = ("C:\web-automation-downloads\%s.xlsx" % file_name)
            excel_file = xlrd.open_workbook(path, on_demand=True)
            excel_file_sheet = excel_file.sheet_by_index(0)
            column_names = []
            for counter in range(excel_file_sheet.ncols):
                column_names.append(excel_file_sheet.cell_value(0, counter))

            row_values = excel_file_sheet.row_values(crm_table_random_row_number)

            # Getting values from a file based on the same random row as in CRM.
            export_values = {}
            for counter in range(len(column_names)):
                # print("Column - column_name: " + str(column_names[counter]))
                # print("Value: " + str(row_values[counter]))
                if type(row_values[counter]) == float:
                    export_values[column_names[counter]] = str(int(row_values[counter]))
                else:
                    export_values[column_names[counter]] = str(row_values[counter])

            export_values = ColumnElements.convert_exported_values_to_lower_case(export_values)
            print(export_values.items())
            # Getting the number of rows in export file.
            rows_in_export = excel_file_sheet.nrows - 1

            # Close excel file
            excel_file.release_resources()
            del excel_file

        #  Remove the file after reading
        os.remove(path)

        # The temporary downloads directory will be removed before session closed. Configured in the conftest.py => def pytest_unconfigure(config)->None

        # Export file verification.
        # Compare the value from CRM (crm_table_random_row_values) with the same data in the export file (export_values).
        for column_name in (crm_table_random_row_values.keys() & export_values.keys()):
            if column_name in fields_to_test:
                print("Column_name: " + str(column_name))
                if crm_table_random_row_values[column_name] == export_values[column_name]:
                    print("correct")
                    print(crm_table_random_row_values[column_name], export_values[column_name])
                else:
                    if column_name == 'email' and (crm_table_random_row_values[column_name] == '****' or export_values[column_name] == '****'):
                        print("correct for Email")
                        print(crm_table_random_row_values[column_name], export_values[column_name])
                        continue
                    else:
                        print("Verification failed")
                        print(crm_table_random_row_values[column_name], export_values[column_name])
                        assert False
            else:
                continue

        print('row_counter: ' + str(row_counter))
        print('rows_in_export: ' + str(rows_in_export))
        if row_counter == rows_in_export:
            print("Verification passed")
        else:
            print("Verification failed")
            assert False

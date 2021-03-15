import os
import subprocess
import time
import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.page_objects.crm.CrossModuleListView import CrossModuleListView, ModuleNames, VerificationExportFields
from src.page_objects.crm.FinancialTransactionsListView import FinancialTransactionsListView

from src.page_objects.crm.InitialSignin import InitialSignin
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_FinancialTransactionsListView(object):

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Financial Transaction')
    @allure.story('Searching by columns')
    @pytest.mark.run(order=1)
    def test_searching_by_columns(self, driver, brand):

        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()


            financial_transactions_list_view = FinancialTransactionsListView(driver)

            financial_transactions_list_view.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.set_test_filter(Filters.FILTER_TEST_FINANCIAL.value)

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.search_via_searchbar(SearchBar.TRANSACTION_NO, "MTT")

            list_view_cross_module.search_via_searchbar(SearchBar.TRANSACTION_TYPE, "Deposit")

            list_view_cross_module.search_via_searchbar_verification("MTT")

            list_view_cross_module.search_via_searchbar_verification("Deposit")

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_searching_by_columns",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Financial Transactions')
    @allure.story('Export selected records')
    @pytest.mark.run(order=2)
    def test_export_selected_records(self, driver, brand):
        try:
            driver.refresh()
            time.sleep(10)

            financial_transactions_list_view = FinancialTransactionsListView(driver)

            # Step 2: Go to Financial Transactions module
            financial_transactions_list_view.go_to()

            # Create object for 'ListView' cross-module logic
            list_view_cross_module = CrossModuleListView(driver)

            # Step 3: Export CSV file
            csv_test_data = list_view_cross_module.export_records('csv', 'export_selected_records')

            # Step 4: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.FINANCIAL_TRANSACTIONS.value, 'csv', csv_test_data, VerificationExportFields.FINANCIAL_TRANSACTIONS)

            # Step 5: Export CSV file
            excel_test_data = list_view_cross_module.export_records('excel', 'export_selected_records')

            # Step 6: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.FINANCIAL_TRANSACTIONS.value, 'excel', excel_test_data, VerificationExportFields.FINANCIAL_TRANSACTIONS)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_export_selected_records",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
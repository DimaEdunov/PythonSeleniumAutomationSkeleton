import os
import subprocess
import time
import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmListViewTableElements import Columns
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.page_objects.crm.CrossModuleListView import CrossModuleListView, ModuleNames, VerificationExportFields
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.TradingAccountsListView import TradingAccountsListView
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_TradingAccountsListView(object):

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Trading Accounts')
    @allure.story('Searching by columns')
    @pytest.mark.run(order=1)
    def test_searching_by_columns(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            trading_accounts_list_view = TradingAccountsListView(driver)

            # Step 2: navigate to trading accounts module
            trading_accounts_list_view.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 3: search via searchbar - CRM ACCOUNT NAME
            list_view_cross_module.search_via_searchbar(SearchBar.CRM_ACCOUNT_NAME, "qa qa")

            # Step 4:: search via searchbar - SERVER
            list_view_cross_module.search_via_searchbar(SearchBar.SERVER, "Demo")

            # Step 5: Verify CRM ACCOUNT NAME value
            list_view_cross_module.search_via_searchbar_verification("qa qa")

            # Step 6: Verify SERVER value
            list_view_cross_module.search_via_searchbar_verification("demo")

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
    @allure.feature('Trading Accounts')
    @allure.story('Export full list')
    @pytest.mark.run(order=2)
    def test_export_full_list(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            trading_accounts_list_view = TradingAccountsListView(driver)

            # Step 2: navigate to trading accounts module
            trading_accounts_list_view.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 3: search via searchbar - CRM ACCOUNT NAME
            list_view_cross_module.search_via_searchbar(SearchBar.CRM_ACCOUNT_NAME, "qa qa")

            # Step 4: Export CSV file
            csv_test_data = list_view_cross_module.export_records('csv', 'export_full_list')

            # Step 5: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.TRADING_ACCOUNTS.value, 'csv', csv_test_data, VerificationExportFields.TRADING_ACCOUNTS)

            # Step 6 Export Excel file
            excel_test_data = list_view_cross_module.export_records('excel', 'export_full_list')

            # Step 7: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.TRADING_ACCOUNTS.value, 'excel', excel_test_data, VerificationExportFields.TRADING_ACCOUNTS)



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
    @allure.feature('Trading Accounts List View')
    @allure.story('Sorting')
    @pytest.mark.run(order=3)
    def test_trading_accounts_sort(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            time.sleep(10)

            trading_accounts_module = TradingAccountsListView(driver)

            # step 2: go to Clients module
            trading_accounts_module.go_to()

            cross_module_list_view = CrossModuleListView(driver)

            cross_module_list_view.sort(Columns.TRADING_ACCOUNT_LOGIN)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_tasks_sort",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False
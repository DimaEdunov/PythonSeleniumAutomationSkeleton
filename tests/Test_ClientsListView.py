import time
import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.elements.dynamic_elements.CrmListViewTabsElements import TabNames
from src.elements.dynamic_elements.CrmListViewTableElements import SortTypes, Columns
from src.page_objects.crm.CrossModuleListView import CrossModuleListView, ModuleNames, VerificationExportFields
from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.ClientsListView import ClientsListView
from src.tests.conftest import get_brand_url

@pytest.mark.usefixtures("driver", "brand")
class Test_ClientsListView:

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Clients List View')
    @allure.story('Mass Edit')
    @pytest.mark.run(order=1)
    def test_mass_edit(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            time.sleep(10)

            clients_module = ClientsListView(driver)

            # step 2: go to Clients module
            clients_module.go_to()

            # Create object for 'ListView' cross-module logic
            list_view_cross_module = CrossModuleListView(driver)

            # Step 3: Set 'Test' filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 4: Perform mass edit
            client_status = clients_module.mass_edit()

            # Step 5: Perform mass edit verification
            clients_module.mass_edit_verification(client_status)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_mass_edit",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Clients List View')
    @allure.story('Export selected records')
    @pytest.mark.run(order=2)
    def test_export_selected_records(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            clients_module = ClientsListView(driver)

            # step 1: go to Clients module
            clients_module.go_to()

            # Create object for 'ListView' cross-module logic
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Set 'Test' filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 3: Export CSV file
            csv_test_data = list_view_cross_module.export_records('csv', 'export_selected_records')

            # Step 4: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.CLIENTS.value, 'csv', csv_test_data, VerificationExportFields.CLIENTS)

            # Step 5: Export Excel file
            excel_test_data = list_view_cross_module.export_records('excel', 'export_selected_records')

            # Step 6: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.CLIENTS.value, 'excel', excel_test_data, VerificationExportFields.CLIENTS)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_export_selected_records",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Clients List View')
    @allure.story('Export full list')
    @pytest.mark.run(order=3)
    def test_export_full_list(self, driver, brand):
        try:

            clients_module = ClientsListView(driver)

            # step 1: go to Clients module
            clients_module.go_to()

            # Create object for 'ListView' cross-module logic
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Set 'Test' filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 3: Export CSV file
            csv_test_data = list_view_cross_module.export_records('csv', 'export_full_list')

            # Step 4: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.CLIENTS.value, 'csv', csv_test_data, VerificationExportFields.CLIENTS)

            # Step 5: Export Excel file
            excel_test_data = list_view_cross_module.export_records('excel', 'export_full_list')

            # Step 6: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.CLIENTS.value, 'excel', excel_test_data, VerificationExportFields.CLIENTS)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_export_full_list",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Clients List View')
    @allure.story('Sorting')
    @pytest.mark.run(order=4)
    def test_clients_sort(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            time.sleep(10)

            clients_module = ClientsListView(driver)

            # step 2: go to Clients module
            clients_module.go_to()

            list_view_cross_module = CrossModuleListView(driver)
            list_view_cross_module.set_test_filter(Filters.FILTER_NEW.value)

            cross_module_list_view = CrossModuleListView(driver)

            cross_module_list_view.sort(Columns.CRM_ID)

            cross_module_list_view.sort(Columns.CLIENT_NAME)

            cross_module_list_view.sort(Columns.CLIENT_STATUS)

            cross_module_list_view.sort(Columns.COUNTRY)

            cross_module_list_view.sort(Columns.COLUMN_ASSIGNED_TO)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_clients_sorting",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Clients List View')
    @allure.story('Tabs')
    @pytest.mark.run(order=5)
    def test_clients_tabs(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            time.sleep(10)

            clients_module = ClientsListView(driver)

            # step 2: go to Clients module
            clients_module.go_to()

            cross_module_listview = CrossModuleListView(driver)

            cross_module_listview.choose_tab_without_verification(TabNames.ALL.value)

            cross_module_listview.choose_tab_with_verification(TabNames.NEW.value)



        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_clients_tabs",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Clients List View')
    @allure.story('Searching by columns')
    @pytest.mark.run(order=6)
    def test_searching_by_columns(self, driver, brand):

        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            clients_list_view = ClientsListView(driver)

            clients_list_view.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.search_via_searchbar(SearchBar.CRM_ID, "ACC")

            list_view_cross_module.search_via_searchbar_verification("ACC")

            list_view_cross_module.search_via_searchbar(SearchBar.CLIENT_NAME, "qa qa")

            list_view_cross_module.search_via_searchbar_verification("qa qa")

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_searching_by_columns",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False
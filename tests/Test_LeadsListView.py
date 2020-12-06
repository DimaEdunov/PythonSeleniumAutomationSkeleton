import os
import subprocess
import time
import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.elements.dynamic_elements.CrmListViewTabsElements import TabNames
from src.elements.dynamic_elements.CrmListViewTableElements import Columns
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView
from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.page_objects.crm.CrossModuleListView import CrossModuleListView, CrossModuleInputs, ModuleNames, VerificationExportFields
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.LeadsDetailsView import LeadsDetailsView
from src.page_objects.crm.LeadsListView import LeadsListView, CreateLeadConstants
from src.tests.conftest import get_brand_url



@pytest.mark.usefixtures("driver", "brand")
class Test_LeadsListView:


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Leads List View')
    @allure.story('Create Lead')
    @pytest.mark.run(order=1)
    def test_create_lead(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            time.sleep(10)

            leads_module = LeadsListView(driver)

            # step 2: go to leads module
            leads_module.go_to()

            #step 3: create lead
            leads_module.create_lead(CreateLeadConstants.FIRST_NAME_VALUE.value,
                                     CreateLeadConstants.LAST_NAME_VALUE.value,
                                     CreateLeadConstants.LEAD_EMAIL_VALUE.value)

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 4 : Select Test Clients[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 5: Navigate to created lead - details view page
            list_view_cross_module.go_to_via_saerchbar(CreateLeadConstants.LEAD_EMAIL_VALUE.value, CrossModuleInputs.LEADS.value)

            # Create LeadsDetailsView object
            leads_details_view = LeadsDetailsView(driver)

            # step 6: create lead verification
            leads_details_view.create_lead_verification(CreateLeadConstants.LEAD_EMAIL_VALUE.value,
                                                        CreateLeadConstants.FIRST_NAME_VALUE.value,
                                                        CreateLeadConstants.LAST_NAME_VALUE.value)

        except :
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_lead",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Leads List View')
    @allure.story('Mass Edit')
    @pytest.mark.run(order=3)
    def test_mass_edit(self, driver, brand):
        try:
            leads_module = LeadsListView(driver)

            #Step 1: Go to Leads module list view
            leads_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            #Step 2: Set 'Test' filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 3 : Perform mass edit
            leads_module.mass_edit()

            # Step 4 : Perform mass edit verification
            leads_module.mass_edit_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_mass_edit",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Leads List View')
    @allure.story('Mass Assign Leads')
    @pytest.mark.run(order=4)
    def test_mass_assign(self, driver, brand):
        try:
            leads_module = LeadsListView(driver)

            # Step 1: Go to Leads module list view
            leads_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Set 'Test' filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 3 : Perform mass assign
            leads_module.mass_assign()
            leads_module.mass_assign_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_mass_assign",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Clients List View')
    @allure.story('Export selected records')
    @pytest.mark.run(order=5)
    def test_export_selected_records(self, driver, brand):
        try:
            leads_module = LeadsListView(driver)

            # Step 1: Go to Leads module list view
            leads_module.go_to()

            # Create object for 'ListView' cross-module logic
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Set 'Test' filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 3: Export CSV file
            csv_test_data = list_view_cross_module.export_records('csv', 'export_selected_records')

            # Step 4: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.LEADS.value, 'csv', csv_test_data, VerificationExportFields.LEADS)

            # Step 5: Export Excel file
            excel_test_data = list_view_cross_module.export_records('excel', 'export_selected_records')

            # Step 6: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.LEADS.value, 'excel', excel_test_data, VerificationExportFields.LEADS)


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
    @pytest.mark.run(order=6)
    def test_export_full_list(self, driver, brand):
        try:
            leads_module = LeadsListView(driver)

            # Step 1: Go to Leads module list view
            leads_module.go_to()

            # Create object for 'ListView' cross-module logic
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Set 'Test' filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 3: Export CSV file
            csv_test_data = list_view_cross_module.export_records('csv', 'export_full_list')

            # Step 4: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.LEADS.value, 'csv', csv_test_data, VerificationExportFields.LEADS)

            # Step 5: Export Excel file
            excel_test_data = list_view_cross_module.export_records('excel', 'export_full_list')

            # Step 6: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.LEADS.value, 'excel', excel_test_data, VerificationExportFields.LEADS)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_export_full_list",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Leads List View')
    @allure.story('Sorting')
    @pytest.mark.run(order=7)
    def test_leads_sort(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            time.sleep(10)

            leads_module = LeadsListView(driver)

            # step 2: go to Clients module
            leads_module.go_to()

            list_view_cross_module = CrossModuleListView(driver)
            list_view_cross_module.set_test_filter(Filters.FILTER_ALL.value)

            cross_module_list_view = CrossModuleListView(driver)

            cross_module_list_view.sort(Columns.LEADS_NO)

            cross_module_list_view.sort(Columns.FIRST_NAME)

            cross_module_list_view.sort(Columns.LAST_NAME)

            cross_module_list_view.sort(Columns.LEAD_STATUS)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_leads_sorting",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Leads List View')
    @allure.story('Searching by columns')
    @pytest.mark.run(order=8)
    def test_searching_by_columns(self, driver, brand):

        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            leads_list_view = LeadsListView(driver)

            leads_list_view.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.search_via_searchbar(SearchBar.LEAD_NO, "LEA")

            list_view_cross_module.search_via_searchbar_verification("LEA")

            list_view_cross_module.search_via_searchbar(SearchBar.FIRST_NAME, "qa")

            list_view_cross_module.search_via_searchbar_verification("qa")

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_searching_by_columns",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False
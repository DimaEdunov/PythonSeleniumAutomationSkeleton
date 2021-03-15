import time
from pathlib import Path

import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.elements.dynamic_elements.CrmListViewTabsElements import TabNames
from src.elements.dynamic_elements.CrmListViewTableElements import Columns
from src.page_objects.crm.CrossModuleListView import CrossModuleListView, ModuleNames, VerificationExportFields
from src.page_objects.crm.DocumentsDetailsView import DocumentsDetailsView
from src.page_objects.crm.DocumentsListView import DocumentsListView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.tests.conftest import get_brand_url

@pytest.mark.usefixtures("driver", "brand")
class Test_DocumentsListView(object):



    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Documents List View')
    @allure.story('Tabs')
    @pytest.mark.run(order=1)
    def test_documents_tabs(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            time.sleep(10)

            documents_module = DocumentsListView(driver)

            # step 2: go to Clients module
            documents_module.go_to()

            cross_module_listview = CrossModuleListView(driver)

            cross_module_listview.choose_tab_without_verification(TabNames.APPROVED.value)

            cross_module_listview.choose_tab_with_verification(TabNames.ALL.value)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_documents_tabs",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.regression
    @allure.feature('Documents List View')
    @allure.story('Create Document')
    @pytest.mark.run(order=2)
    def test_create_document(self,driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Go to CRM Main screen
            crm_main_screen.go_to()

            # Sign in verification
            crm_main_screen.sign_in_verification()

            documents_list_view = DocumentsListView(driver)

            #go to my leads module
            documents_list_view.go_to()

            path_to_document_attachment = Path(__file__).parent

            documents_list_view.create_new_document(path_to_document_attachment)

            cross_module_listview = CrossModuleListView(driver)


            cross_module_listview.choose_tab_without_verification(TabNames.ALL.value)

            documents_list_view.new_document_verification()

        except:

            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_document",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False


    @pytest.mark.regression
    @allure.feature('Documents List View')
    @allure.story('Documents - Edit Button')
    @pytest.mark.run(order=3)
    def test_edit_document_via_edit_button(self,driver, brand):
        try:

            documents_details_view = DocumentsDetailsView(driver)

            documents_details_view.edit_document_via_edit_button()

            documents_details_view.edit_document_via_edit_button_verification("Approved")

        except:

            allure.attach(driver.get_screenshot_as_png(),
                          name="test_check_crm_password",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @allure.feature('Documents List View')
    @allure.story('Documents - Download File')
    @pytest.mark.run(order=4)
    def test_download_file(self, driver, brand):
        try:

            documents_details_view = DocumentsDetailsView(driver)

            documents_details_view.download()

            documents_details_view.download_verification()

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
    @allure.feature('Documents List View')
    @allure.story('Export selected records')
    @pytest.mark.run(order=5)
    def test_export_selected_records(self, driver, brand):
        try:
            documents_module = DocumentsListView(driver)

            # Step 1: Go to Documents module
            documents_module.go_to()

            # Create object for 'ListView' cross-module logic
            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.choose_tab_without_verification(TabNames.APPROVED.value)

            # Step 3: Export CSV file
            csv_test_data = list_view_cross_module.export_records('csv', 'export_selected_records')

            # Step 4: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.DOCUMENTS.value, 'csv', csv_test_data, VerificationExportFields.DOCUMENTS)

            # Step 5: Export CSV file
            excel_test_data = list_view_cross_module.export_records('excel', 'export_selected_records')

            # Step 6: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.DOCUMENTS.value, 'excel', excel_test_data, VerificationExportFields.DOCUMENTS)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_export_selected_records",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Document List View')
    @allure.story('Sorting')
    @pytest.mark.run(order=6)
    def test_documents_sort(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            time.sleep(10)

            documents_module = DocumentsListView(driver)

            # step 2: go to Clients module
            documents_module.go_to()

            cross_module_list_view = CrossModuleListView(driver)

            cross_module_list_view.sort(Columns.DOCUMENTS_NO)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_leads_sorting",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Documents')
    @allure.story('Search columns')
    @pytest.mark.run(order=7)
    def test_searching_by_columns(self, driver, brand):

        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            documents_list_view = DocumentsListView(driver)

            documents_list_view.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.set_test_filter(Filters.FILTER_ALL.value)

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.search_via_searchbar(SearchBar.DOCUMENT_NO, "DOC")

            list_view_cross_module.search_via_searchbar(SearchBar.FILE_NAME, "documentAttachment")

            list_view_cross_module.search_via_searchbar_verification("DOC")

            list_view_cross_module.search_via_searchbar_verification("documentAttachment")


        except:

            allure.attach(driver.get_screenshot_as_png(),

                          name="test_searching_by_columns",

                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False
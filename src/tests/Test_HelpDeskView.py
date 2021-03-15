import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldNameConstants
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView

from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.elements.dynamic_elements.CrmListViewTableElements import Columns
from src.elements.dynamic_elements.CrmListViewTabsElements import TabNames
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderConstants, RightSliderElements
from src.page_objects.crm.ClientsDetailsView import ClientDetailsView
from src.page_objects.crm.CrossModuleListView import CrossModuleListView, ModuleNames, VerificationExportFields
from src.page_objects.crm.HelpDeskDetailsView import HelpDeskDetailsView
from src.page_objects.crm.HelpDeskListView import HelpDeskListView

from src.page_objects.crm.InitialSignin import InitialSignin
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_HelpDeskView:


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Help desk view')
    @allure.story('Create new ticket')
    @pytest.mark.run(order=1)
    def test_create_ticket(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            # Instance of an object 'HelpDeskListView'
            help_desk_list_view = HelpDeskListView(driver)

            # Step 2 : navigate to help desk listview
            help_desk_list_view.go_to()

            # Step 3: Create a new ticket
            help_desk_list_view.create_new_ticket()

            # Instance of an object 'HelpDeskDetailsView'
            help_desk_details_view = HelpDeskDetailsView(driver)

            # Step 4: navigate to help desk details view
            help_desk_details_view.go_to()

            # Step 5: Verify creation of ticket
            help_desk_details_view.create_edit_ticket_verification("title", "General Question", "Open")

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_ticket",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Help desk')
    @allure.story('Tabs')
    @pytest.mark.run(order=2)
    def test_help_desk_tabs(self, driver, brand):
        try:
            # Instance of an object 'HelpDeskDetailsView'
            help_desk_details_view = HelpDeskListView(driver)

            # Step 1 : Edit details via pencil
            help_desk_details_view.go_to()

            cross_module_listview = CrossModuleListView(driver)

            cross_module_listview.choose_tab_with_verification(TabNames.IN_PROGRESS.value)

            cross_module_listview.choose_tab_with_verification(TabNames.ALL.value)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="HelpDeskModule.test_help_desk_tabs",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('HelpDesk View')
    @allure.story('Searching by columns')
    @pytest.mark.run(order=3)
    def test_searching_by_columns(self, driver, brand):

        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            help_list_view = HelpDeskListView(driver)

            help_list_view.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.set_test_filter(Filters.FILTER_ALL.value)

            list_view_cross_module.search_via_searchbar(SearchBar.TITLE, "title")

            list_view_cross_module.search_via_searchbar_verification("title")

            list_view_cross_module.search_via_searchbar(SearchBar.RELATED_TO, "dima edunov")

            list_view_cross_module.search_via_searchbar_verification("dima edunov")

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
    @allure.feature('HelpDesk View')
    @allure.story('Export selected records')
    @pytest.mark.run(order=4)
    def test_export_selected_records(self, driver, brand):

        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            help_list_view = HelpDeskListView(driver)

            # step 2: go to Help Desk module
            help_list_view.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            # Step 3: Export CSV file
            csv_test_data = list_view_cross_module.export_records('csv', 'export_selected_records')

            # Step 4: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.HELP_DESK.value, 'csv', csv_test_data,
                                                       VerificationExportFields.HELP_DESK)

            # Step 5: Export CSV file
            excel_test_data = list_view_cross_module.export_records('excel', 'export_selected_records')

            # Step 6: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.HELP_DESK.value, 'excel', excel_test_data,
                                                       VerificationExportFields.HELP_DESK)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_export_selected_records",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('HelpDesk View')
    @allure.story('Add new event ')
    @pytest.mark.run(order=5)
    @allure.step("HelpDeskModule.add_event() | Create new event")
    def test_add_event(self, driver, brand):

        try:
            driver.refresh()
            time.sleep(10)

            help_desk_list_view = HelpDeskListView(driver)
            help_desk_list_view.go_to()
            time.sleep(3)

            help_desk_list_view.navigate_to_the_help_desk_details_view(FieldNameConstants.TITLE_VALUE.value)
            time.sleep(3)

            cross_module_listview = CrossModuleDetailsView(driver)
            cross_module_listview.add_event(CrossModuleDetailsView.subject_input1)
            time.sleep(3)

            client_details_view = ClientDetailsView(driver)
            client_details_view.client_details_view_add_interaction_verification(CrossModuleDetailsView.subject_input1)
            time.sleep(3)

            help_desk_list_view = HelpDeskListView(driver)
            help_desk_list_view.go_to()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_navigate_to_the_clients_from_the_help_desk",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('HelpDesk View')
    @allure.story('Sorting')
    @pytest.mark.run(order=6)
    def test_help_desk_sort(self, driver, brand):
        try:
            help_desk_list_view = HelpDeskListView(driver)
            help_desk_list_view.go_to()
            time.sleep(6)

            cross_module_list_view = CrossModuleListView(driver)

            cross_module_list_view.sort(Columns.TICKET_NO)

            cross_module_list_view.sort(Columns.TITLE)

            cross_module_list_view.sort(Columns.STATUS)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_help_desk_sort",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False



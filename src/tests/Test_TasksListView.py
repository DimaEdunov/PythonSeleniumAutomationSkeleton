import os
import subprocess
import time

import allure
import pytest
from allure_commons.types import AttachmentType


from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView
from src.elements.dynamic_elements.CrmListViewTabsElements import TabNames
from src.elements.dynamic_elements.CrmListViewTableElements import Columns
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.page_objects.crm.CrossModuleListView import CrossModuleListView, ModuleNames, VerificationExportFields
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.TasksListView import TasksListView
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_TaskListView():

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Tasks List View')
    @allure.story('Create task')
    @pytest.mark.run(order=1)
    def test_create_task(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            tasks_list_view = TasksListView(driver)

            # Step 2: Go to tasks module
            tasks_list_view.go_to()

            cross_module_details_view = CrossModuleDetailsView(driver)

            subject_field_input = cross_module_details_view.add_event(CrossModuleDetailsView.subject_input1)

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.search_via_searchbar(SearchBar.SUBJECT, subject_field_input)

            # Step 4: Verify task creation
            list_view_cross_module.search_via_searchbar_verification(subject_field_input)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_task",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Tasks List View')
    @allure.story('Edit event')
    @pytest.mark.run(order=2)
    def test_tasks_edit_event(self, driver, brand):
        try:
            # Instance of an object 'CrossModuleListView'
            tasks_list_view = TasksListView(driver)
            tasks_list_view.go_to()

            # Step 1: Perform edit event
            tasks_list_view.edit_event()

            # Instance of an object 'CrossModuleListView'
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Search for "subject qa" in the subject.
            list_view_cross_module.search_via_searchbar(SearchBar.SUBJECT, "QA_TEST edit event")

            # Step 3: Perform edit event verification
            tasks_list_view.edit_event_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_tasks_edit_event",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Tasks List View')
    @allure.story('Tasks Mass Edit')
    @pytest.mark.run(order=3)
    def test_tasks_mass_edit(self, driver, brand):
        try:
            # Instance of an object 'TasksListView'
            tasks_list_view = TasksListView(driver)
            tasks_list_view.go_to()

            # Step 1: Create a new task
            cross_module_details_view = CrossModuleDetailsView(driver)

            cross_module_details_view.add_event(CrossModuleDetailsView.subject_input1)

            cross_module_details_view.add_event(CrossModuleDetailsView.subject_input3)

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.choose_tab_without_verification(TabNames.SHOW_MINE.value)

            # Step 2: Search for "subject qa" in the subject.
            list_view_cross_module.search_via_searchbar(SearchBar.SUBJECT, CrossModuleDetailsView.subject_input)

            # Step 3: Perform mass edit
            tasks_list_view.mass_edit()

            # Step 4: Perform mass edit verification
            tasks_list_view.mass_edit_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_task_mass_edit",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Tasks List View')
    @allure.story('Export selected records')
    @pytest.mark.run(order=4)
    def test_export_selected_records(self, driver, brand):
        try:
            # Instance of an object 'TasksListView'
            tasks_list_view = TasksListView(driver)
            tasks_list_view.go_to()

            cross_module_list_view = CrossModuleListView(driver)

            # Step 3: Export CSV file
            csv_test_data = cross_module_list_view.export_records('csv', 'export_selected_records')

            # Step 4: Verify data is correct
            cross_module_list_view.export_verification(ModuleNames.TASKS.value, 'csv', csv_test_data, VerificationExportFields.TASKS)

            # Step 5: Export Excel file
            excel_test_data = cross_module_list_view.export_records('excel', 'export_selected_records')

            # Step 6: Verify data is correct
            cross_module_list_view.export_verification(ModuleNames.TASKS.value, 'excel', excel_test_data, VerificationExportFields.TASKS)


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
    @allure.feature('Tasks List View')
    @allure.story('Export selected records iCal')
    @pytest.mark.run(order=5)
    def test_export_selected_record_iCal(self, driver, brand):
        try:
            # Instance of an object 'TasksListView'
            tasks_list_view = TasksListView(driver)
            tasks_list_view.go_to()

            ical_test_data = tasks_list_view.export_selected_record_iCal()
            tasks_list_view.export_iCal_verification(ical_test_data)
            
        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_export_selected_records_ical",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Tasks List View')
    @allure.story('Sorting')
    @pytest.mark.run(order=6)
    def test_tasks_sort(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            time.sleep(10)

            tasks_module = TasksListView(driver)

            # step 2: go to Clients module
            tasks_module.go_to()

            cross_module_list_view = CrossModuleListView(driver)

            cross_module_list_view.sort(Columns.SUBJECT)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_tasks_sort",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Tasks List View')
    @allure.story('Tasks Delete Event')
    @pytest.mark.run(order=7)
    def test_tasks_delete_event(self, driver, brand):
        try:
            # Instance of an object 'TasksListView'
            tasks_list_view = TasksListView(driver)
            tasks_list_view.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 1: Search for "subject qa edit one event" in the subject.
            list_view_cross_module.search_via_searchbar(SearchBar.SUBJECT, CrossModuleDetailsView.subject_input3)

            # Step 2: Delete event.
            tasks_list_view.delete_event()

            # Step 3: Search for "subject qa edit one event" in the subject.
            list_view_cross_module.search_via_searchbar(SearchBar.SUBJECT, CrossModuleDetailsView.subject_input3)

            # Step 4: Perform delete event verification
            tasks_list_view.delete_event_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_task_delete_event",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Tasks List View')
    @allure.story('Searching by columns')
    @pytest.mark.run(order=8)
    def test_searching_by_columns(self,driver, brand):

        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            tasks_list_view = TasksListView(driver)

            tasks_list_view.go_to()

            cross_module_listview = CrossModuleListView(driver)

            cross_module_listview.choose_tab_without_verification(TabNames.SHOW_ALL.value)

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.search_via_searchbar(SearchBar.EVENT_TYPE, "Call")

            list_view_cross_module.search_via_searchbar_verification("Call")

            driver.refresh()
            time.sleep(8)
            cross_module_listview.choose_tab_without_verification(TabNames.SHOW_ALL.value)

            list_view_cross_module.search_via_searchbar(SearchBar.ACCOUNT_NAME, "dima")

            list_view_cross_module.search_via_searchbar_verification("dima")

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
    @allure.feature('Tasks List View')
    @allure.story('Tasks Mass Delete')
    @pytest.mark.run(order=9)
    def test_tasks_mass_delete(self, driver, brand):
        try:
            # Instance of an object 'TasksListView'
            tasks_list_view = TasksListView(driver)
            tasks_list_view.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.choose_tab_without_verification(TabNames.SHOW_MINE.value)

            # tasks_list_view.create_task("Meeting")


            cross_module_details_view = CrossModuleDetailsView(driver)

            cross_module_details_view.add_event(CrossModuleDetailsView.subject_input1)

            # Instance of an object 'CrossModuleListView'
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Search for "subject qa" in the subject.
            list_view_cross_module.search_via_searchbar(SearchBar.SUBJECT, CrossModuleDetailsView.subject_input)

            # Step 3: Delete events.
            tasks_list_view.mass_delete()

            # Step 4: Perform mass delete verification.
            list_view_cross_module.search_via_searchbar(SearchBar.SUBJECT, CrossModuleDetailsView.subject_input)

            tasks_list_view.delete_event_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_task_mass_delete",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

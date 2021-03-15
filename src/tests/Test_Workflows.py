import os
import subprocess
from time import sleep
from allure_commons.types import AttachmentType
import allure
import pytest
from src.tests.conftest import get_brand_url
from src.page_objects.crm.ClientsListView import ClientsListView
from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.page_objects.crm.ClientsDetailsView import ClientDetailsView
from src.page_objects.crm.CrossModuleListView import CrossModuleListView
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView, EditFieldValues
from src.page_objects.crm.WorkflowsAddConditions import WorkflowAddConditionsConstants, WorkflowAddConditionsTempVars, \
    WorkflowsAddConditions
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.WorkflowsModuleListView import WorkflowsModuleListView
from src.page_objects.crm.WorkflowsSchedule import WorkflowsSchedule, ScheduleWorkflowConstants
from src.page_objects.crm.WorkflowsAddConditions import WorkflowsAddConditions, WorkflowAddConditionsConstants
from src.page_objects.crm.WorkflowsAddTasks import WorkflowAddTasksConstants, WorkflowsAddTasks


@pytest.mark.usefixtures("driver", "brand")
# Test name structure is taken from the QA checklist : 'Test_FeatureName_TestedBehaviorName'
class Test_Workflow():


    @pytest.mark.regression
    @allure.feature('Workflows List View')
    @allure.story('Create Workflow')
    @pytest.mark.run(order=1)
    def test_create_workflow(self, driver, brand):
        try:
            sleep(5)
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to crm main screen
            crm_main_screen.go_to()

            # Step 2: go to workflow module
            workflow_module = WorkflowsModuleListView(driver)
            workflow_module.go_to()

            # Step 3: click new workflow button
            workflow_module.click_new_workflow_button()

            # Step 4: Schedule Workflow
            schedule_workflow_screen = WorkflowsSchedule(driver)
            schedule_workflow_screen.filling_mandatory_fields_and_submitting(
                ScheduleWorkflowConstants.NAME_WORKFLOW_VALUE.value)

            # Step 5: Add Conditions
            workflow_add_conditions = WorkflowsAddConditions(driver)
            workflow_add_conditions.select_module(WorkflowAddConditionsConstants.CLIENTS_MODULE.value)

            # workflow_module.click_add_condition_group_button()
            workflow_add_conditions.choose_condition_group()
            workflow_add_conditions.select_filter_condition()
            workflow_add_conditions.select_client_status_value()
            workflow_add_conditions.select_country_condition()
            workflow_add_conditions.select_email_condition()
            workflow_add_conditions.select_second_mid_condition()

            # Step 7: Add Tasks
            workflow_add_tasks = WorkflowsAddTasks(driver)
            workflow_add_tasks.add_task()
            workflow_add_tasks.verify_workflow_in_list_view()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_workflow",
                          attachment_type=AttachmentType.PNG)
            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False


    @pytest.mark.regression
    @allure.feature('Workflows List View')
    @allure.story('Testing Workflow 1')
    @pytest.mark.run(order=2)
    def test_check_workflow_1(self, driver, brand):
        try:
            # Step 1: go to clients module
            driver.switch_to_default_content()
            clients_module = ClientsListView(driver)
            clients_module.go_to()

            # Step 2: open test filter
            list_view_cross_module = CrossModuleListView(driver)
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST_CLIENTS.value)

            # Step 3: open client's details
            details_view_cross_module = CrossModuleDetailsView(driver)
            details_view_cross_module.go_to_via_searchbar_using_email("pandaqa+2", "clients")

            # Step 4: edit client status
            client_details = CrossModuleDetailsView(driver)
            client_details.pencil_edit_list(EditFieldValues.CLIENT_STATUS_FIELD.value,
                                            WorkflowAddConditionsTempVars.CLIENT_STATUS)

            # Step 5: verify client's data was updated
            client_details = ClientDetailsView(driver)
            client_details.workflow_client_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_check_workflow_1",
                          attachment_type=AttachmentType.PNG)
            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()


    @pytest.mark.regression
    @allure.feature('Workflows List View')
    @allure.story('Testing Workflow 2')
    @pytest.mark.run(order=2)
    def test_check_workflow_2(self, driver, brand):
        try:
            # Step 1: go to clients module
            clients_module = ClientsListView(driver)
            clients_module.go_to()

            # Step 2: open test filter
            list_view_cross_module = CrossModuleListView(driver)
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST_CLIENTS.value)

            # Step 3: open client's details
            details_view_cross_module = CrossModuleDetailsView(driver)
            details_view_cross_module.go_to_via_searchbar_using_email("pandaqa+3", "clients")

            # Step 4: click edit client button
            cross_module_details_view = CrossModuleDetailsView(driver)
            cross_module_details_view.click_edit_button()

            # Step 5: edit client
            client_details_view = ClientDetailsView(driver)
            client_details_view.pencil_edit_for_workflow()

            # Step 5: verify client's data was updated
            client_details = ClientDetailsView(driver)
            client_details.workflow_client_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_check_workflow_2",
                          attachment_type=AttachmentType.PNG)
            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()


    @pytest.mark.regression
    @allure.feature('Workflows List View')
    @allure.story('Delete Workflow')
    @pytest.mark.run(order=3)
    def test_delete_workflow(self, driver, brand):
        try:
            # Step 1: go to workflow module
            workflow_module = WorkflowsModuleListView(driver)
            workflow_module.go_to()

            # Step 2: searching of workflow by name
            workflow_module.search_workflow_by_name(ScheduleWorkflowConstants.NAME_WORKFLOW_VALUE.value)

            # Step 3: delete workflow
            workflow_module.delete_workflow()

            # Step 4: searching of workflow by name
            workflow_module.search_workflow_by_name(ScheduleWorkflowConstants.NAME_WORKFLOW_VALUE.value)

            # Step 5: verify workflow was deleted
            workflow_module.check_workflow_not_found()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_delete_workflow",
                          attachment_type=AttachmentType.PNG)
            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

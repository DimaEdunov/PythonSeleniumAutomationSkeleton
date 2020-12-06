from enum import Enum
from time import sleep
from src.page_objects.crm.WorkflowsSchedule import ScheduleWorkflowConstants
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from src.elements.CrmElements import CrmElements


class WorkflowAddTasksConstants(Enum):
    TASK_TITLE_VALUE = "Test_title"
    ADDRESS_PICK_LIST_VALUE = "Address"
    TEST_ADDRESS_VALUE = "Test_address"
    COUNTRY_ALBANIA_VALUE = "Albania"
    COUNTRY_PICK_LIST_VALUE = "Country"


class WorkflowsAddTasks(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("WorkflowsAddTasks.add_task() | Add Task")
    def add_task(self):
        sleep(0.2)
        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.ADD_TASK_LIST))).click()
        sleep(0.2)
        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.UPDATE_FIELD_ITEM))).click()
        sleep(2)
        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.TASK_TITLE_FIELD))) \
            .send_keys(WorkflowAddTasksConstants.TASK_TITLE_VALUE.value)

        sleep(2)
        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.ADD_FIELD_BUTTON))).click()

        """" Set Address  """
        sleep(0.2)
        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.SELECT_FIELD_LIST))).click()
        sleep(0.2)
        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.TASK_SEARCH_FIELD))) \
            .send_keys(WorkflowAddTasksConstants.ADDRESS_PICK_LIST_VALUE.value)

        sleep(0.3)

        address_pick_list_value = self.driver.find_element(By.XPATH, CrmElements.ADDRESS_ITEM)
        self.driver.execute_script("arguments[0].click();", address_pick_list_value)

        sleep(2)

        self.driver.find_element(By.XPATH, CrmElements.ADDRESS_TEXT_FIELD).click()

        sleep(2)

        self.driver.find_element(By.XPATH, CrmElements.ADDRESS_TEXT_AREA) \
            .send_keys(WorkflowAddTasksConstants.TEST_ADDRESS_VALUE.value)
        sleep(0.2)

        self.driver.find_element(By.XPATH, CrmElements.SAVE_VALUE_BUTTON).click()
        """" <><><>  """

        sleep(2)
        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.ADD_FIELD_BUTTON))).click()

        """" Set Country  """
        sleep(0.2)
        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.SELECT_FIELD_LIST))).click()

        sleep(0.2)

        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.TASK_SEARCH_FIELD2))) \
            .send_keys(WorkflowAddTasksConstants.COUNTRY_PICK_LIST_VALUE.value)

        sleep(0.3)

        country_pick_list_value = self.driver.find_element(By.XPATH, CrmElements.COUNTRY_PICK_LIST_VALUE)
        self.driver.execute_script("arguments[0].click();", country_pick_list_value)

        sleep(0.2)

        country_list = Select(self.driver.find_element(By.XPATH, CrmElements.TASKS_COUNTRY_PICK_LIST))
        country_list.select_by_visible_text(WorkflowAddTasksConstants.COUNTRY_ALBANIA_VALUE.value)
        """" <><><>  """

        sleep(2)
        self.driver.find_element(By.XPATH, CrmElements.SAVE_WORKFLOWS_TASK_BUTTON).click()

        sleep(2)
        self.driver.find_element(By.XPATH, CrmElements.SAVE_WORKFLOW_BUTTON).click()

    @allure.step("WorkflowsAddTasks.verify_workflow_in_list_view() | Verify new Workflow exist in list view")
    def verify_workflow_in_list_view(self):
        sleep(3)
        name_workflow = self.driver.find_element(By.XPATH, "//span[text()='%s']"
                                                 % ScheduleWorkflowConstants.NAME_WORKFLOW_VALUE.value).text
        assert name_workflow == ScheduleWorkflowConstants.NAME_WORKFLOW_VALUE.value

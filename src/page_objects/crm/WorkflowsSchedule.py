from enum import Enum
from time import *
import allure
import random
from allure_commons.types import AttachmentType
from src.elements.CrmElements import CrmElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScheduleWorkflowConstants(Enum):
    random_number = random.randrange(1, 9999)
    NAME_WORKFLOW_VALUE = "Test_workflow " + str(random_number)


class WorkflowsSchedule(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("WorkflowsSchedule.set_workflow_name() | Set Workflow name")
    @allure.severity(allure.severity_level.NORMAL)
    def filling_mandatory_fields_and_submitting(self, workflow_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, CrmElements.WORKFLOW_NAME_FIELD))).send_keys(workflow_name)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, CrmElements.WORKFLOW_EXECUTE_RADIOBUTTON))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.NEXT_BUTTON))).click()
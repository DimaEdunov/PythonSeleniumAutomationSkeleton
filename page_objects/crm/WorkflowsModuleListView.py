from enum import Enum
from time import sleep

import allure
import random
import string
from datetime import *
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldElements, FieldName
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchbarElements, SearchBar
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, RightSliderConstants
from src.elements.dynamic_elements.CrmSideMenuElements import CrmSideMenu, Modules


class WorkflowsModuleListView(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("WorkflowsModuleListView.go_to() | Navigating to Workflows Module")
    def go_to(self):

        sleep(7)
        # Navigating to workflows module screen
        crm_config_module = CrmSideMenu.side_menu_items(self.driver, Modules.CRM_CONFIGURATION_MODULE.value)
        self.driver.execute_script("arguments[0].click();", crm_config_module)

        sleep(5)

        self.driver.switch_to_frame(self.driver.find_element(By.XPATH, CrmElements.MODULE_IFRAME))

        WebDriverWait(self.driver, timeout=25).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.WORKFLOWS_MODULE))).click()
        sleep(7)

        self.driver.find_element(By.XPATH, CrmElements.WORKFLOWS_HEADER)

    @allure.step("WorkflowsModuleListView.click_new_workflow_button() | Click 'New Workflow' button")
    def click_new_workflow_button(self):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.NEW_WORKFLOW_BUTTON))).click()


    @allure.step("WorkflowsModuleListView.search_workflow_by_name() | Searching by workflow name")
    def search_workflow_by_name(self, name):
        sleep(2)
        name_field = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.WORKFLOW_LIST_VIEW_NAME_SEARCH_FIELD)))
        name_field.clear()
        name_field.send_keys(name)

    @allure.step("WorkflowsModuleListView.delete_workflow() | Click delete workflow")
    def delete_workflow(self):
        sleep(2)
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.WORKFLOW_LIST_VIEW_MORE_BUTTON))).click()
        self.driver.find_element(By.XPATH, CrmElements.WORKFLOW_LIST_VIEW_DELETE_BUTTON).click()
        sleep(2)
        self.driver.find_element(By.XPATH, CrmElements.WORKFLOW_LIST_VIEW_CONFIRM_DELETE_BUTTON).click()

    @allure.step("WorkflowsModuleListView.check_workflow_not_found() | Check 'No results' message is displayed")
    def check_workflow_not_found(self):
        sleep(2)
        WebDriverWait(self.driver, timeout=25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.WORKFLOW_LIST_VIEW_NO_RESULTS_MESSAGE)))

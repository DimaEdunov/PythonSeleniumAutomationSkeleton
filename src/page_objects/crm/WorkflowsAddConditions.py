from enum import Enum
from time import sleep

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from src.elements.CrmElements import CrmElements


class WorkflowAddConditionsConstants(Enum):
    CONDITION_OR = "OR"
    COUNTRY_GUAM = "Guam"
    PRIORITY_WORKFLOW_VALUE = ""
    CLIENTS_MODULE = "Clients"
    CONDITION_AND = "AND"


class WorkflowAddConditionsTempVars(object):
    CLIENT_STATUS = ""


class WorkflowsAddConditions(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("WorkflowsAddConditions.select_module() | Select module")
    def select_module(self, module_name_value):
        sleep(0.2)
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.PICKLIST_MODULE_ITEM))).click()
        sleep(0.2)

        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.MODULE_SEARCH_FIELD))) \
            .send_keys(module_name_value)

        sleep(0.2)
        module_item = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.WORKFLOW_PICKLIST_CHOOSE_MODULE)))
        self.driver.execute_script("arguments[0].click();", module_item)

    @allure.step("WorkflowsAddConditions.select_client_status_condition() | Choose Client Status condition")
    def choose_condition_group(self):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ADD_CONDITION_GROUP_BUTTON))).click()

        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.FILTER_CONDITION_LIST))).click()

        sleep(0.2)
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.CONDITION_LIST_SEARCH_FIELD))) \
            .send_keys("Client Status")

        sleep(0.2)
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.CLIENT_STATUS_PICK_LIST_VALUE))).click()

    @allure.step("WorkflowsAddConditions.select_filter_condition() | Choose 'is' condition")
    def select_filter_condition(self):
        sleep(0.2)
        condition_list = Select(self.driver.find_element(By.XPATH, CrmElements.CONDITION_LIST))
        condition_list.select_by_visible_text("is")

    @allure.step("WorkflowsAddConditions.select_client_status_value() | Choose Client Status value")
    def select_client_status_value(self):
        sleep(0.2)
        client_status_list = Select(self.driver.find_element(By.XPATH, CrmElements.CLIENT_STATUS_LIST))
        WorkflowAddConditionsTempVars.CLIENT_STATUS = self.driver.find_element \
            (By.XPATH, CrmElements.CLIENT_STATUS_SECOND_VALUE).text
        client_status_list.select_by_visible_text(WorkflowAddConditionsTempVars.CLIENT_STATUS)

    @allure.step("WorkflowsAddConditions.select_country_condition() | Choose Country filter condition")
    def select_country_condition(self):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ADD_CONDITION_GROUP_BUTTON))).click()

        sleep(0.2)
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.FILTER_CONDITION_LIST))).click()

        sleep(0.2)
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.SEARCH_FIELD))) \
            .send_keys("Country")

        sleep(0.3)
        country_pick_list_value = self.driver.find_element(By.XPATH, CrmElements.COUNTRY_PICK_LIST_VALUE)
        self.driver.execute_script("arguments[0].click();", country_pick_list_value)

        sleep(0.2)
        country_list = Select(self.driver.find_element(By.XPATH, CrmElements.COUNTRY_LIST))
        country_list.select_by_visible_text(WorkflowAddConditionsConstants.COUNTRY_GUAM.value)

    @allure.step("WorkflowsAddConditions.select_second_filter_condition() | Choose 'is' condition")
    def select_second_filter_condition(self):
        sleep(0.2)
        condition_list = Select(self.driver.find_element(By.XPATH, CrmElements.CONDITION_LIST)[2])
        condition_list.select_by_visible_text("is")

    @allure.step("WorkflowsAddConditions.select_email_condition() | Choose Email filter condition")
    def select_email_condition(self):
        sleep(0.2)
        mid_condition_list = Select(self.driver.find_element(By.XPATH, CrmElements.MID_CONDITION_LIST))
        mid_condition_list.select_by_visible_text(WorkflowAddConditionsConstants.CONDITION_OR.value)

        sleep(0.2)

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ADD_CONDITION_GROUP_BUTTON))).click()

        sleep(0.2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.FILTER_CONDITION_LIST))).click()

        sleep(0.2)
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.SEARCH_FIELD))) \
            .send_keys("Email")

        sleep(0.3)
        email_pick_list_value = self.driver.find_element(By.XPATH, CrmElements.EMAIL_PICK_LIST_VALUE)
        self.driver.execute_script("arguments[0].click();", email_pick_list_value)

        sleep(0.2)
        condition_list = Select(self.driver.find_element(By.XPATH, CrmElements.THIRD_CONDITION_LIST))
        condition_list.select_by_visible_text("contains")

        sleep(0.2)
        self.driver.find_element(By.XPATH, CrmElements.ENTER_EMAIL_BUTTON).click()

        sleep(0.2)
        self.driver.find_element(By.XPATH, CrmElements.EMAIL_FIELD).send_keys("pandaqa+")

        sleep(0.2)
        self.driver.find_element(By.XPATH, CrmElements.SAVE_ADD_CONDITION_BUTTON).click()

    @allure.step("WorkflowsAddConditions.select_second_mid_condition() | Select second mid condition")
    def select_second_mid_condition(self):
        sleep(2)
        mid_condition_list = Select(self.driver.find_element(By.XPATH, CrmElements.MID_CONDITION_LIST_2))
        mid_condition_list.select_by_visible_text(WorkflowAddConditionsConstants.CONDITION_AND.value)

        sleep(1)
        self.driver.find_element(By.XPATH, CrmElements.NEXT_BUTTON).click()

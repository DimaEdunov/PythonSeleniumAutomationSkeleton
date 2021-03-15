import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.elements.ApiElements import ApiElements
from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmSideMenuElements import CrmSideMenu, Modules


class AutoAssign():

    def __init__(self, driver):
        self.driver = driver

    @allure.step("AutoAssign.go_to() | Navigate to Auto assign")
    def go_to(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_WAIT_VERIFICATION_ELEMENT)))

        # Navigating to clients module screen
        CrmSideMenu.side_menu_items(self.driver, Modules.AUTO_ASSIGN_MODULE.value).click()

        time.sleep(3)

        WebDriverWait(self.driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH,CrmElements.MODULE_IFRAME)))


    @allure.step("AutoAssign.create_rule() | Create AutoAssign")
    def create_rule(self, name_of_auto_assign, type_of_auto_assign_rule):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CREATE_RULE_BUTTON))).click()

        time.sleep(3)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, CrmElements.RULE_POPUP_RULE_NAME_FIELD))).send_keys(name_of_auto_assign)

        if (type_of_auto_assign_rule == "leads"):
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_LEAD_INPUT_CHECKBOX))).click()

        else:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_CLIENT_INPUT_CHECKBOX))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_RULE_TYPE_PICKLIST_BOX))).click()

        rule_picklist_items = Select(self.driver.find_element(By.XPATH, CrmElements.RULE_POPUP_RULE_TYPE_PICKLIST_BOX))
        rule_picklist_items.select_by_visible_text("Country")

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_RULE_BRAND_PICKLIST_BOX))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_RULE_BRAND_PICKLIST_FIRST_ITEM))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_RULE_ASSIGN_TO_USER_CHECKBOX))).click()

        assign_to_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, CrmElements.RULE_POPUP_RULE_ASSIGN_TO_PICKLIST_FIELD)))

        assign_to_field.clear()

        assign_to_field.send_keys("Panda Auto")

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_RULE_COUNTRY_PICKLIST_BOX))).click()

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, CrmElements.RULE_POPUP_COUNTRY_SEARCH_FIELD))).send_keys("liechtenstein")

        print("CLICKED COUNTRY CHOOSE BOX")
        time.sleep(5)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_COUNTRY_PICKLIST_CHECKBOX))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_RULE_ASSIGN_TO_ITEM))).click()

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, CrmElements.RULE_POPUP_RULE_SUBMIT_BUTTON))

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_RULE_SUBMIT_BUTTON))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.AUTO_ASSIGN_OK_BUTTON))).click()

        time.sleep(2)

    @allure.step("AutoAssign.rule_verification() | Rule item verification")
    def rule_verification(self, name_of_auto_assign):
        time.sleep(5)

        name_of_auto_assign_rule = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, CrmElements.AUTO_ASSIGN_FIRST_RULE_NAME_CELL))).text

        print("Name of autoAssign = " +name_of_auto_assign_rule)
        if name_of_auto_assign_rule == name_of_auto_assign:
            pass

        else:
            assert False

    @allure.step("AutoAssign.sort_last_item_first_in_list() | Sort AutoAssign so last created item would be first")
    def sort_last_item_first_in_list(self):
        time.sleep(3)


        print("Count of 'SORT BY PRIORITY' elements : " +(str(len(self.driver.find_elements(By.XPATH,CrmElements.AUTO_ASSIGN_SORT_BY_PRIORITY_BUTTON )))))
        # Put the last created 'auto-assign' rule, to be first in list
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.AUTO_ASSIGN_SORT_BY_PRIORITY_BUTTON))).click()
        time.sleep(7)

    @allure.step("AutoAssign.edit_rule() | Edit autoAssign rule")
    def edit_rule(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.AUTO_ASSIGN_FIRST_RULE_PENCIL_CELL))).click()

        time.sleep(5)

        # Check if correct rule is beeing edited
        if len((self.driver.find_elements(By.XPATH, CrmElements.AUTO_ASSIGN_POPUP_RULE_NAME_INPUT_VALUE )))>0:

            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, CrmElements.RULE_POPUP_RULE_NAME_FIELD))).clear()

            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, CrmElements.RULE_POPUP_RULE_NAME_FIELD))).send_keys("EDITED automation_leads_test")

        else:
            print("Clicked on the WRONG rule")
            assert False

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RULE_POPUP_RULE_SUBMIT_BUTTON))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.AUTO_ASSIGN_OK_BUTTON))).click()

    @allure.step("AutoAssign.delete_rule() | Delete autoAssign rule")
    def delete_rule(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.AUTO_ASSIGN_DELETE_FIRST_RULE_BUTTON))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.AUTO_ASSIGN_OK_BUTTON))).click()

        time.sleep(4)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.AUTO_ASSIGN_OK_BUTTON))).click()
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

from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldElements, FieldName
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchbarElements, SearchBar
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, \
    RightSliderConstants
from src.elements.dynamic_elements.CrmSideMenuElements import CrmSideMenu, Modules


class CreateLeadConstants(Enum):
    # Create lead right slider
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    PASSWORD = "Aa111111"
    COUNTRY_VALUE = "de"
    FIRST_NAME_VALUE = "Jack" + random_character
    LAST_NAME_VALUE = "Jackson" + random_character
    random_number = datetime.now().strftime('%H%M%S%f')
    LEAD_EMAIL_VALUE = "pandaqa+" + random_number + "@pandats.com"

    # Mass assign right slider
    USER_ASSIGN_TO = "Anastasiia V"


class LeadsListView(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("LeadsModule.go_to() | Navigating to Leads Module")
    @allure.severity(allure.severity_level.NORMAL)
    def go_to(self):
            # Navigating to clients module screen
            CrmSideMenu.side_menu_items(self.driver, Modules.LEADS_MODULE.value).click()

            WebDriverWait(self.driver, 25).until(
                EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

            sleep(4)


    @allure.step("LeadsModule.create_lead() | Create Lead")
    @allure.severity(allure.severity_level.NORMAL)
    def create_lead(self, first_name_value, last_name_value, email_value):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CREATE_LEAD_BUTTON))).click()

        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.FIRST_NAME_FIELD.value).send_keys(
            first_name_value)

        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.LAST_NAME_FIELD.value).send_keys(
            last_name_value)

        sleep(3)

        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.EMAIL_FIELD.value).send_keys(
            email_value)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RIGHT_SLIDER_CREATE_LEAD_BUTTON))).click()

        sleep(5)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        return email_value

    @allure.step("LeadsModule.mass_edit() | Performing mass edit")
    @allure.severity(allure.severity_level.NORMAL)
    def mass_edit(self):
        import time
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SELECT_ALL_ITEMS_BUTTON))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.MASS_EDIT_BUTTON))).click()

        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ASSIGNED_TO_CHECKBOX))).click()

        assign_to_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                RightSliderConstants.ASSIGNED_TO_NAME_OF_PICKLIST.value,
                                                                                                RightSliderConstants.ASSIGNED_TO_PICKLIST_VALUE.value)
        time.sleep(2)

        self.driver.execute_script("arguments[0].click();", assign_to_pick_list)

        time.sleep(1)

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="LeadsModule.mass_edit",
                      attachment_type=AttachmentType.PNG)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SAVE_CHANGES_BUTTON))).click()

        time.sleep(45)

        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.LOADING_SPINNER)))

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        time.sleep(3)

    @allure.step("LeadsModule.mass_edit() | Performing mass edit verification")
    @allure.severity(allure.severity_level.NORMAL)
    def mass_edit_verification(self):
        import time
        time.sleep(5)
        crm_id = self.driver.find_elements(By.XPATH, CrmElements.LEAD_ID_LIST)[3]

        self.driver.execute_script("arguments[0].click();", crm_id)

        time.sleep(7)

        if FieldElements.get_field_value(self.driver,
                                         FieldName.ASSIGNED_TO_FIELD.value).text == RightSliderConstants.ASSIGNED_TO_PICKLIST_VALUE.value:
            print("DEBUG - Passed")
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="LeadsModule.mass_edit",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("LeadsModule.mass_assing() | Performing mass assign verification")
    @allure.severity(allure.severity_level.NORMAL)
    def mass_assign(self):
        sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SELECT_ALL_ITEMS_BUTTON))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.MASS_ASSIGN_BUTTON))).click()
        sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.USER_NAME_ASSIGN_TO
                                        % CreateLeadConstants.USER_ASSIGN_TO.value))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ASSIGN_BUTTON))).click()

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    @allure.step("LeadsModule.mass_assign_verification() | Performing mass assign verification")
    @allure.severity(allure.severity_level.NORMAL)
    def mass_assign_verification(self):
        sleep(5)
        crm_id = self.driver.find_elements(By.XPATH, CrmElements.LEAD_ID_LIST)[0]

        sleep(3)

        self.driver.execute_script("arguments[0].click();", crm_id)

        sleep(7)

        if FieldElements.get_field_value(self.driver,
                                         FieldName.ASSIGNED_TO_FIELD.value).text == CreateLeadConstants.USER_ASSIGN_TO.value:
            print("DEBUG - Passed")
        else:
            assert False

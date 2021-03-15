from datetime import *

import time
import allure


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
from src.elements.dynamic_elements.CrmDetailsViewSectionElements import SectionElements, Section
from src.elements.CrmElements import CrmElements

class ClientsListView(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("ClientsModule.go_to() | Navigating to Clients Module")
    @allure.severity(allure.severity_level.NORMAL)
    def go_to(self):
        try:
            # Navigating to clients module screen
            CrmSideMenu.side_menu_items(self.driver, Modules.CLIENTS_MODULE.value).click()

            WebDriverWait(self.driver, 25).until(
                EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        except:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="ClientsModule.go_to",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("ClientsModule.mass_edit() | Performing mass edit")
    def mass_edit(self):
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SELECT_ALL_ITEMS_BUTTON))).click()

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="test_mass_edit",
                      attachment_type=AttachmentType.PNG)

        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.MASS_EDIT_BUTTON))).click()

        time.sleep(1)

        # Select 'Assign to' checkbox / Select 'Assign to' value

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ASSIGNED_TO_CHECKBOX))).click()

        time.sleep(2)

        assign_to_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                RightSliderConstants.ASSIGNED_TO_NAME_OF_PICKLIST.value,
                                                                                                RightSliderConstants.ASSIGNED_TO_PICKLIST_VALUE.value)
        self.driver.execute_script("arguments[0].click();", assign_to_pick_list)


        # Select 'Client Status' checkbox / Select 'Client Status' value
        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.STATUS_CHECKBOX))).click()



        time.sleep(1)

        client_status_pick_list = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                                    RightSliderConstants.STATUS_NAME_OF_PICKLIST.value)


        self.driver.execute_script("arguments[0].click();", client_status_pick_list[7])

        client_status_value = str(client_status_pick_list[7].get_attribute('textContent'))

        time.sleep(7)

        print("BEFORE spinner : " + str(datetime.now().strftime('%H%M%S')))
        WebDriverWait(self.driver, 50).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.LOADING_SPINNER)))
        print("AFTER spinner : " + str(datetime.now().strftime('%H%M%S')))

        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SAVE_CHANGES_BUTTON))).click()

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="before clicking 'save' screenshot",
                      attachment_type=AttachmentType.PNG)

        time.sleep(45)

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="After clicking 'save' screenshot",
                      attachment_type=AttachmentType.PNG)

        return client_status_value

    @allure.step("ClientsModule.mass_edit_verification() | Performing mass edit verification")
    @allure.severity(allure.severity_level.NORMAL)
    def mass_edit_verification(self, client_status_value):
        time.sleep(2)

        crm_id = self.driver.find_elements(By.XPATH, CrmElements.CRM_ID_LIST)[7]

        self.driver.execute_script("arguments[0].click();", crm_id)

        time.sleep(8)

        if FieldElements.get_field_value(self.driver, FieldName.ASSIGNED_TO_FIELD.value).text == RightSliderConstants.ASSIGNED_TO_PICKLIST_VALUE.value \
                and FieldElements.get_field_value(self.driver, FieldName.CLIENT_STATUS_FIELD.value).text == client_status_value:
            print("DEBUG - Verification passed")

        else:
            assert False
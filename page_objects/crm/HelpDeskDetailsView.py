from time import sleep
from datetime import *
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.elements.CrmElements import CrmElements
from selenium.webdriver.support import expected_conditions as EC
from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldElements, FieldName, FieldNameConstants
from src.elements.dynamic_elements.CrmHelpdeskRightSliderFieldElements import HelpdeskRightSliderElements, \
    HelpdeskRightSliderFieldConstants
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, RightSliderConstants


class HelpDeskDetailsView():

    def __init__(self, driver):
        self.driver = driver

    @allure.step("HelpDeskDetailsView.go_to() | Navigate to Help Desk")
    def go_to(self):

        sleep(10)
        self.driver.refresh()
        sleep(7)

        help_desk_id = self.driver.find_elements(By.XPATH, CrmElements.HELP_DESK_ID)[0]
        help_desk_id.click()

        sleep(4)

    @allure.step("HelpDeskDetailsView.create_edit_ticket_verification() | Create a new ticket verification")
    def create_edit_ticket_verification(self, title_value, category_value, status_value):
        sleep(4)

        if FieldElements.get_field_value(self.driver, FieldName.STATUS_VALUE.value).text == status_value or "****" and \
                FieldElements.get_field_value(self.driver,
                                              FieldName.CATEGORY_VALUE.value).text == category_value and \
                FieldElements.get_field_value(self.driver, FieldName.TITLE_VALUE.value).text == title_value:
            print("DEBUG - Verification passed")
        else:
            print("DEBUG - Verification failed")
            assert False

    def edit_ticket_via_pencil_verification(self):
        pass

    @allure.step("HelpDeskDetailsView.edit_ticket_via_pencil() | Edit ticket via pencil")
    def edit_ticket_via_edit_button(self):

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.DETAILS_VIEW_MAIN_EDIT_BUTTON))).click()

        sleep(2)
        # Insert value into 'Title' field
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.TITLE_FIELD.value).clear()

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.TITLE_FIELD.value).send_keys(
            "title edited via edit")

        # Submitting 'STATUS' picklist
        status_pick_list = HelpdeskRightSliderElements.insert_value_to_picklist(self.driver,
                                                                                HelpdeskRightSliderFieldConstants.STATUS_NAME_OF_PICKLIST.value,
                                                                                HelpdeskRightSliderFieldConstants.STATUS_IN_PROGRESS_PICKLIST_VALUE.value)
        sleep(2)
        self.driver.execute_script("arguments[0].click();", status_pick_list)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.EDIT_TICKET_TICKET_SUBMIT_BUTTON))).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    def edit_ticket_via_edit_verification(self):
        pass
    @allure.step("HelpDeskModule.edit_ticket_via_pencil() | Performing edit via pencil")
    @allure.severity(allure.severity_level.NORMAL)
    def edit_ticket_via_pencil(self):

        FieldElements.change_text_field_value_via_pencil(self.driver, FieldName.TITLE_VALUE.value,
                                                             FieldNameConstants.TITLE_VALUE.value)

        FieldElements.change_picklist_field_value_via_pencil(self.driver, FieldName.TICKET_SOURCE_FIELD.value,
                                                                 FieldNameConstants.TICKET_SOURCE_VALUE.value)

    @allure.step("HelpDeskModule.edit_ticket_via_pencil() | Performing edit via pencil verification")
    @allure.severity(allure.severity_level.NORMAL)
    def edit_ticket_via_pencil_verification(self):
        sleep(1.5)
        if FieldElements.get_field_value(self.driver, FieldName.TITLE_VALUE.value).text == FieldNameConstants.TITLE_VALUE.value \
                and FieldElements.get_field_value(self.driver, FieldName.TICKET_SOURCE_FIELD.value).text == FieldNameConstants.TICKET_SOURCE_VALUE.value:
            print("DEBUG - Verification passed")

        else:
            print("DEBUG - Verification failed")
            assert False

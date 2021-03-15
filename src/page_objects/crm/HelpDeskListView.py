import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements import CrmHelpdeskRightSliderFieldElements
from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldNameConstants, FieldName
from src.elements.dynamic_elements.CrmHelpdeskRightSliderFieldElements import HelpdeskRightSliderFieldConstants, \
    HelpdeskRightSliderElements
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar, SearchbarElements
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, RightSliderConstants
from src.elements.dynamic_elements.CrmSideMenuElements import Modules, CrmSideMenu


class HelpDeskListView():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("HelpDeskListView.go_to() | Navigating to Help Desk")
    def go_to(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_WAIT_VERIFICATION_ELEMENT)))

        # Navigating to clients module screen
        CrmSideMenu.side_menu_items(self.driver, Modules.HELP_DESK_MODULE.value).click()

        time.sleep(3)

    @allure.step("HelpDeskListView.create_new_ticket() | Create a new ticket ")
    def create_new_ticket(self):
        time.sleep(2)
        # Clicking on 'New ticket' button
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CREATE_NEW_TICKET_BUTTON))).click()
        time.sleep(2.5)

        # Insert value into 'Title' field
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.TITLE_FIELD.value).send_keys("title")

        # Insert value into 'Description Information' field
        RightSliderElements.insert_value_into_description_field(self.driver, RightSliderConstants.DESCRIPTION_INFORMATION_FIELD.value).send_keys("description")

        # Submitting 'ASSIGNED TO' picklist
        assign_to_pick_list = HelpdeskRightSliderElements.insert_value_to_picklist(self.driver,
                                                                           HelpdeskRightSliderFieldConstants.ASSIGNED_TO_NAME_OF_PICKLIST.value,
                                                                           HelpdeskRightSliderFieldConstants.ASSIGNED_TO_PICKLIST_VALUE.value)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", assign_to_pick_list)

        # Inserting value into 'RELATES TO' field
        relates_to_picklist_choose_item = HelpdeskRightSliderElements.choose_item_from_relates_to_picklist(self.driver,
                                                                                                           HelpdeskRightSliderFieldConstants.RELATES_TO_PICKLIST_VALUE.value)
        relates_to_picklist_choose_item.click()
        time.sleep(2)

        # Submitting 'STATUS' picklist
        status_pick_list = HelpdeskRightSliderElements.insert_value_to_picklist(self.driver,
                                                                           HelpdeskRightSliderFieldConstants.STATUS_NAME_OF_PICKLIST.value,
                                                                           HelpdeskRightSliderFieldConstants.STATUS_OPEN_PICKLIST_VALUE.value)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", status_pick_list)

        # Submitting 'CATEGORY' picklist
        category_pick_list = HelpdeskRightSliderElements.insert_value_to_picklist(self.driver,
                                                                           HelpdeskRightSliderFieldConstants.CATEGORY_NAME_OF_PICKLIST.value,
                                                                           HelpdeskRightSliderFieldConstants.CATEGORY_PICKLIST_VALUE.value)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", category_pick_list)

        time.sleep(4)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CREATE_NEW_TICKET_SUBMIT_BUTTON))).click()

        time.sleep(1)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        time.sleep(4)

    @allure.step("HelpDeskListView.create_new_event() | Create a new event ")
    def navigate_to_the_help_desk_details_view(self, title_value):
        time.sleep(3)

        SearchbarElements.bar_choose_element(self.driver, SearchBar.TITLE.value).click()
        time.sleep(3)

        SearchbarElements.bar_insert_value_field_element(self.driver, SearchBar.TITLE.value).send_keys(title_value)

        self.driver.find_element(By.XPATH, CrmElements.FILTER_AGREE_BUTTON).click()
        time.sleep(3)

        help_desk_id = self.driver.find_elements(By.XPATH, CrmElements.HELP_DESK_ID)[0]
        help_desk_id.click()
        time.sleep(3)

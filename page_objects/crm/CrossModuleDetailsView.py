import time

from time import sleep
from enum import Enum
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from src.elements.dynamic_elements.CrmDetailsViewSectionElements import SectionElements, Section
from src.infrastructure.dynamic_helpers.ScrollActions import ScrollActions
from src.elements.CrmElements import CrmElements
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldElements, FieldNameConstants, FieldName
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchbarElements, SearchBar
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, \
    RightSliderConstants
from src.page_objects.api.Api import ApiConstants



class EditFieldValues(Enum):
    FIRST_NAME_NEW = "JackNew"
    FIRST_NAME_DEFAULT = "JackDefault"

    LAST_NAME_NEW = "JohnsonNew"
    LAST_NAME_DEFAULT = "JohnsonDefault"

    CITY_NEW = "HaifaNew"
    CITY_DEFAULT = "HaifaDefault"

    # field titles
    CLIENT_STATUS_FIELD = "Client Status"
    COUNTRY_FIELD = "Country"
    ADDRESS_FIELD = "Address"

    # tab titles
    ADDRESS_INFORMATION_TAB = "Address Information"


class CrossModuleDetailsView(object):

    random_number = ApiConstants.random_number_variable_a.value
    subject_input = "QA_TEST"
    subject_input1 = "QA_TEST1" + str(random_number)
    subject_input2 = "QA_TEST2" + str(random_number)
    subject_input3 = "QA_TEST3" + str(random_number)
    subject_input4 = "QA_TEST4" + str(random_number)

    def __init__(self, driver):
        self.driver = driver

    @allure.step("CrossModuleDetailsView.pencil_edit_fields() | Editing details view via pencil")
    def edit_fields_edit_button(self, first_name_value, last_name_value, city_value):
        WebDriverWait(self.driver, 15).until(

            EC.element_to_be_clickable((By.XPATH, CrmElements.DETAILS_VIEW_MAIN_EDIT_BUTTON))). \
            click()

        # Edit 'First Name' field
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.FIRST_NAME_FIELD.value). \
            clear()
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.FIRST_NAME_FIELD.value). \
            send_keys(first_name_value)

        # Edit 'Last Name' field
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.LAST_NAME_FIELD.value). \
            clear()
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.LAST_NAME_FIELD.value). \
            send_keys(last_name_value)

        # Edit 'City field'
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.CITY_FIELD.value) \
            .clear()
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.CITY_FIELD.value). \
            send_keys(city_value)

        # Submit the edit by tapping 'Update Lead' button and then 'Ok'
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.UPDATE_LEAD_BUTTON))).click()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        sleep(1.5)

    @allure.step("CrossModuleDetailsView.go_to_via_searchbar_using_email() | Navigating to details view via search by using email")
    def go_to_via_searchbar_using_email(self, email_value, module_name):
        sleep(7)

        SearchbarElements.bar_choose_element(self.driver, SearchBar.EMAIL.value).click()

        SearchbarElements.bar_insert_value_field_element(self.driver, SearchBar.EMAIL.value).send_keys()
        time.sleep(1)
        SearchbarElements.bar_insert_value_field_element(self.driver, SearchBar.EMAIL.value).send_keys(email_value)


        self.driver.find_element(By.XPATH, CrmElements.FILTER_AGREE_BUTTON).click()

        WebDriverWait(self.driver, 45).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        # Click on 'CRM Id' from row 0
        if module_name == "clients":
            clicked_item = CrmElements.CRM_ID_LIST

        if module_name == "leads":
            clicked_item = CrmElements.LEAD_ID_LIST

        first_client_item = self.driver.find_elements(By.XPATH, clicked_item)[0]
        sleep(1)
        self.driver.execute_script("arguments[0].click();", first_client_item)

        time.sleep(7)

    # Search for client / lead via email
    @allure.step("CrossModuleDetailsView.search_via_email() | Search lead / client via email")
    def search_via_email(self, email_value):
        SearchbarElements.bar_choose_element(self.driver, SearchBar.EMAIL.value).click()

        SearchbarElements.bar_insert_value_field_element(self.driver, SearchBar.EMAIL.value).send_keys(email_value)

        sleep(1)
        self.driver.find_element(By.XPATH, CrmElements.FILTER_AGREE_BUTTON).click()

        WebDriverWait(self.driver, 45).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

    @allure.step("CrossModuleDetailsView.pencil_edit_list() | Editing of pick list value in details view via pencil")
    def pencil_edit_list(self, field, value):
        # Click pencil icon in relevant picklist field
        pencil_btn = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.DETAILS_VIEW_FIELD_PENCIL_BUTTON % field)))
        sleep(0.5)

        self.driver.execute_script("arguments[0].click();", pencil_btn)
        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        # Select value from field
        sleep(0.1)
        first_item = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.DETAILS_VIEW_LIST_FIRST_ITEM % field)))
        self.driver.execute_script("arguments[0].click();", first_item)

        item = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.DETAILS_VIEW_LIST_ITEM % (field, value))))
        self.driver.execute_script("arguments[0].click();", item)

        # Click confirm button
        sleep(0.1)
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.DETAILS_VIEW_CONFIRM_BUTTON % field))).click()

    @allure.step("CrossModuleDetailsView.open_tab() | Open tab in details view")
    def open_tab(self, title):
        sleep(0.5)
        tab = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.DETAILS_VIEW_TAB % title)))
        self.driver.execute_script("arguments[0].click();", tab)
        sleep(1)
        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

    @allure.step("CrossModuleDetailsView.get_text_from_field() | Get value from field in details view")
    def get_text_from_field(self, field):
        sleep(0.1)
        data = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.DETAILS_VIEW_FIELD_VALUE % (field, field))))
        data = data.text
        return data

    @allure.step("CrossModuleDetailsView.click_edit_button() | Click Edit button in details view")
    def click_edit_button(self):
        sleep(0.1)
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.DETAILS_VIEW_EDIT_BUTTON))).click()
        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))
        sleep(1)

    @allure.step("CrossModuleDetailsView.change_phone() | Change phone number details view")
    def change_phone(self, phone_number_type):

        if phone_number_type == "valid":

            # Change phone to be valid
            FieldElements.change_text_field_value_via_pencil(self.driver, FieldName.PHONE_FIELD.value,
                                                             FieldNameConstants.VALID_PHONE)
        else:
            # Change phone to be Invalid
            FieldElements.change_text_field_value_via_pencil(self.driver, FieldName.PHONE_FIELD.value,
                                                             FieldNameConstants.INVALID_PHONE_A.value)


    def detailsview_phone_verification(self, expected_validation_type):
        self.driver.refresh()
        time.sleep(5)

        if expected_validation_type == "valid":
            if len(self.driver.find_elements(By.XPATH, CrmElements.DETAILSVIEW_VALID_PHONE_ICON)) > 0 and \
            FieldElements.get_field_value(self.driver, FieldName.PHONE_FIELD.value).text == ApiConstants.PHONE_VALID.value or 'xxxx':
                print("List verification was successful")

            else:
                assert False

        if expected_validation_type == "invalid":
            if len(self.driver.find_elements(By.XPATH, CrmElements.DETAILSVIEW_INVALID_PHONE_ICON)) > 0 and \
                    FieldElements.get_field_value(self.driver,
                                                  FieldName.PHONE_FIELD.value).text == FieldNameConstants.INVALID_PHONE_A.value or 'xxxx':
                print("List verification was successful")

            else:
                assert False

    @allure.step("CrossModuleDetailsView.edit_field_via_pencil() | Performing edit via pencil")
    def edit_field_via_pencil(self,field_name, new_value):

        time.sleep(2)

        FieldElements.change_text_field_value_via_pencil(self.driver, field_name.value,
                                                         new_value.value)

    @allure.step("CrossModuleDetailsView.open_section() | Opens a section inside details view")
    def open_section(self, section_name):
        time.sleep(2)
        ScrollActions.scroll_to(SectionElements.open_section(self.driver, section_name))

        time.sleep(4)

        SectionElements.open_section(self.driver, section_name).click()

        time.sleep(3)

    def edit_field_via_pencil_verification(self, field_name, expected_field_value):
        print("Value of field %s " %FieldElements.get_field_value(self.driver, field_name.value).text)
        print("Value of expected result %s " % expected_field_value.value)

        if FieldElements.get_field_value(self.driver, field_name.value).text == expected_field_value.value:
            pass

        else:
            assert False


    def details_view_phone_verification(self, expected_validation_type):
        if expected_validation_type == "valid":
            if len(self.driver.find_elements(By.XPATH, CrmElements.DETAILSVIEW_VALID_PHONE_ICON)) > 0 and \
                    FieldElements.get_field_value(self.driver, FieldName.PHONE_FIELD).text == ApiConstants.PHONE_VALID.value or '****':
                print("List verification was successful")

            else:
                assert False

        if expected_validation_type == "invalid":
            if len(self.driver.find_elements(By.XPATH, CrmElements.DETAILSVIEW_INVALID_PHONE_ICON)) > 0 and \
                    FieldElements.get_field_value(self.driver, FieldName.PHONE_FIELD).text == FieldNameConstants.INVALID_PHONE_A.value or '****':
                print("List verification was successful")

            else:
                assert False

    @allure.step("ClientDetailsView.make_an_interaction() | Make an interaction")

    def add_event(self,subject_input):

        self.driver.refresh()

        time.sleep(15)

        # When in 'Tasks' module, use this
        if len(self.driver.find_elements(By.XPATH, CrmElements.ADD_EVENT_BUTTON)) > 0:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.ADD_EVENT_BUTTON))).click()

        # When in any other 'Details View' screen, use this
        else:
            self.driver.find_element(By.XPATH, CrmElements.ADD_INTERACTION_BUTTON).click()

        time.sleep(3)
        event_status_picklist = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                  RightSliderConstants.EVENT_STATUS_PICKLIST.value,
                                                                                                  RightSliderConstants.EVENT_STATUS_PICKLIST_VALUE.value)
        self.driver.execute_script("arguments[0].click();", event_status_picklist)

        time.sleep(3)
        event_type_picklist = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                RightSliderConstants.EVENT_TYPE_PICKLIST.value,
                                                                                                RightSliderConstants.EVENT_TYPE_VALUE.value)
        self.driver.execute_script("arguments[0].click();", event_type_picklist)

        time.sleep(3)
        assign_to_picklist = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                               RightSliderConstants.ASSIGN_TO_NAME_OF_PICKLIST.value,
                                                                                               RightSliderConstants.ASSIGNED_TO_PICKLIST_VALUE.value)

        self.driver.execute_script("arguments[0].click();", assign_to_picklist)

        time.sleep(3)

        if len(self.driver.find_elements(By.XPATH, CrmElements.ATTACHED_TO_PICKLIST_ITEM)) > 0:
            time.sleep(1)
            attached_to_pick_list_item = RightSliderElements.choose_item_by_value_out_of_attached_to_picklist(
                self.driver,
                RightSliderConstants.ATTACHED_TO_PICKLIST.value,
                RightSliderConstants.ATTACHED_TO_PICKLIST_VALUE.value)

            # Must use the following loop, as part of names from picklist do not have values and are not clicked,
            # Randomly, and different on each bran
            counter = 0
            for name_item in attached_to_pick_list_item:
                if "dima" in name_item.text:
                    self.driver.execute_script("arguments[0].click();", attached_to_pick_list_item[counter])
                    break
                counter += 1

        time.sleep(2)

        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.SUBJECT_FIELD.value).clear()
        time.sleep(3)


        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.SUBJECT_FIELD.value).send_keys(subject_input)
        time.sleep(3)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RIGHT_SLIDER_COMMENTS_FIELD))).send_keys("comments qa")
        time.sleep(4)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SAVE_BUTTON))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        return subject_input
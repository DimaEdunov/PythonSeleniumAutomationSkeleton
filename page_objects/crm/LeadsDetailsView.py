import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldElements, FieldName
from src.elements.dynamic_elements.CrmDetailsViewSectionElements import SectionElements, Section
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, RightSliderConstants


class LeadsDetailsView(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("LeadsModule.create_lead_verification() | Create lead verification")
    def create_lead_verification(self, email_value, first_name_value, last_name_value):
        time.sleep(5)
        if FieldElements.get_field_value(self.driver, FieldName.EMAIL_FIELD.value).text == email_value or "****" and \
                FieldElements.get_field_value(self.driver,
                                              FieldName.FIRST_NAME_FIELD.value).text == first_name_value and \
                FieldElements.get_field_value(self.driver,
                                              FieldName.LAST_NAME_FIELD.value).text == last_name_value:
            print("DEBUG - Verification passed")
        else:
            print("DEBUG - Verification failed")
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="LeadsDetailsView.create_lead_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("LeadsModule.create_lead_verification() | Create lead autoAssign verification")
    def create_lead_auto_assign_verification(self, assign_to):
        time.sleep(5)
        if FieldElements.get_field_value(self.driver, FieldName.ASSIGNED_TO_FIELD.value).text == assign_to:
            print("DEBUG - Verification passed")
        else:
            print("DEBUG - Verification failed")
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="LeadsDetailsView.create_lead_auto_assign_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("LeadsModule.lead_pencil_edit_verification() | Lead pencil edit verification")
    @allure.severity(allure.severity_level.NORMAL)
    def lead_edit_button_change_field_verification(self, first_name_value, last_name_value, city_value):

        if FieldElements.get_field_value(self.driver,
                                         FieldName.FIRST_NAME_FIELD.value).text == first_name_value and \
                FieldElements.get_field_value(self.driver,
                                              FieldName.LAST_NAME_FIELD.value).text == last_name_value and \
                FieldElements.get_field_value(self.driver,
                                              FieldName.CITY_FIELD.value).text == city_value:
            print("DEBUG - Verification passed")
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="LeadsModule.lead_pencil_edit_verification",
                          attachment_type=AttachmentType.PNG)
            assert False


    @allure.step("LeadsModule.convert_lead() | Convert lead")
    def convert_lead(self, first_name_value, last_name_value, city_value, phone_value, address_value, postal_code_value,
                     country_value, day_date_of_birth_value, month_date_of_birth_value, year_date_of_birth_value):

        self.driver.find_elements(By.XPATH, CrmElements.LEAD_ID_LIST)[0].click()



        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CONVERT_LEAD_BUTTON_ORANGE))).click()

        # Edit 'First Name' field
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.FIRST_NAME_FIELD.value).clear()

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.FIRST_NAME_FIELD.value). \
            send_keys(first_name_value)

        # Edit 'Last Name' field
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.LAST_NAME_FIELD.value).clear()

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.LAST_NAME_FIELD.value). \
            send_keys(last_name_value)

        # Edit 'City field'
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.CITY_FIELD.value).clear()

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.CITY_FIELD.value). \
            send_keys(city_value)

        # Edit 'Phone field'
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.PHONE_FIELD.value) \
            .clear()

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.PHONE_FIELD.value). \
            send_keys(phone_value)

        # Edit 'Citizenship field'
        category_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                  RightSliderConstants.CITIZENSHIP_PICKLIST.value,
                                                                                  RightSliderConstants.CITIZENSHIP_VALUE.value)

        self.driver.execute_script("arguments[0].click();", category_pick_list)


        # If 'UI Langauge' picklist appears
        time.sleep(2)
        if (len(self.driver.find_elements(By.XPATH,CrmElements.LEADS_RIGHT_SLIDER_UI_LANGUAGE_PLACEHOLDER))>0):
            # Edit 'Currency field'
            ui_langauge_picklist = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                           RightSliderConstants.UI_LANGUAGE.value)

            self.driver.execute_script("arguments[0].click();", ui_langauge_picklist[0])


        # Edit 'Postal code field'
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.POSTAL_CODE_FIELD.value) \
            .clear()

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.POSTAL_CODE_FIELD.value). \
            send_keys(postal_code_value)

        # Edit 'Postal code field'
        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.ADDRESS_FIELD.value) \
            .clear()

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.ADDRESS_FIELD.value). \
            send_keys(address_value)

        # Edit 'Country field'
        category_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                               RightSliderConstants.COUNTRY_PICKLIST.value,
                                                                                               country_value)
        self.driver.execute_script("arguments[0].click();", category_pick_list)

        # Edit 'Currency field'
        currencies = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                        RightSliderConstants.CURRENCY_PICKLIST.value)

        self.driver.execute_script("arguments[0].click();", currencies[0])


        # Edit date of birth
        RightSliderElements.choose_date_of_birth(self.driver, year_date_of_birth_value, month_date_of_birth_value, day_date_of_birth_value)

        self.driver.find_element(By.XPATH, CrmElements.CONVERT_LEAD_BUTTON).click()

        time.sleep(13)

        # If ok button present on the page after creation of a lead
        try:
            if len(WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, CrmElements.OK_BUTTON)))) > 0:

                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, CrmElements.OK_BUTTON))).click()
        finally:
            time.sleep(3)
            return
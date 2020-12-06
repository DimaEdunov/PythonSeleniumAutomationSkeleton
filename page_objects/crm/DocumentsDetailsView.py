import os
import time
from datetime import datetime

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldName, FieldElements


class DocumentsDetailsView(object):

    """Notice! Elements of 'Documents RightSlider', are NOT dynamic due to DOM's structure on that page beeing
    different of other 'RightSlider' pages.

    Look in CrmRightSliderElements.py for elaboration
    """

    def __init__(self, driver):
        self.driver = driver

    @allure.step("DocumentsModule.edit_document_via_edit_button() | Edit Document via edit button")
    def edit_document_via_edit_button(self):
            time.sleep(3)
            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.DETAILS_VIEW_MAIN_EDIT_BUTTON))).click()

            time.sleep(5)
            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.DOCUMENTS_RIGHT_SLIDER_STATUS_PICKLIST_OPEN_BUTTON))).click()

            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.DOCUMENTS_RIGHT_SLIDER_STATUS_PICKLIST_ITEM_APPROVED))).click()

            time.sleep(3)

            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.DOCUMENTS_RIGHT_SLIDER_STATUS_SAVE_BUTTON))).click()

            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

            self.driver.refresh()


    @allure.step("DocumentsModule.edit_document_via_edit_button_verification() | Edit Document via edit button Verification")
    def edit_document_via_edit_button_verification(self,status_of_document):
            time.sleep(2)
            if FieldElements.get_field_value(self.driver, FieldName.STATUS.value).text == status_of_document:
                pass

            else:
                assert False

    def download(self):
        time.sleep(2)
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.DOCUMENTS_DOWNLOAD_BUTTON))).click()

        time.sleep(2)
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.DOCUMENTS_DOWNLOAD_OK_BUTTON))).click()

        time.sleep(10)

    def download_verification(self):
        downloaded_documents_folder = os.listdir("c:\\web-automation-downloads")

        # Calculates raw timestamp of html report creation
        raw_value_of_report_creation_timestamp = os.path.getmtime("c:\\web-automation-downloads\\%s" % downloaded_documents_folder[-1])
        download_timestamp = datetime.fromtimestamp(raw_value_of_report_creation_timestamp)
        delta_time = datetime.now() - download_timestamp

        print("DELTA TIME : " +str(delta_time))

        if delta_time.seconds>55:
            assert False
        else:
            pass
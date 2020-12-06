
from pathlib import Path
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

class DocumentsListView(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("DocumentsListView.go_to() | Navigating to Documents Module")
    @allure.severity(allure.severity_level.NORMAL)
    def go_to(self):
        try:
            # Navigating to clients module screen
            CrmSideMenu.side_menu_items(self.driver, Modules.DOCUMENTS_MODULE.value).click()

            WebDriverWait(self.driver, 25).until(
                EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        except:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="DocumentsModule.go_to",
                          attachment_type=AttachmentType.PNG)
            assert False


    @allure.step("DocumentsListView.create_new_document() | Create new document")
    @allure.severity(allure.severity_level.NORMAL)
    def create_new_document(self, base_path):
        try:

            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.CREATE_NEW_DOCUMENT_BUTTON))).click()

            # base_path = Path(__file__).parent
            file_path = (base_path / "files/documentAttachment.png").resolve()
            print(file_path)

            time.sleep(2)

            upload_image_field = self.driver.find_element(By.XPATH, CrmElements.UPLOAD_DOCUMENT_FIELD)

            self.driver.execute_script("arguments[0].click();", upload_image_field)

            upload_image_field.send_keys(str(file_path))

            time.sleep(2)

            attached_to_pick_list_item = RightSliderElements.choose_item_by_value_out_of_attached_to_picklist(
                self.driver,
                RightSliderConstants.ATTACHED_TO_PICKLIST.value,
                RightSliderConstants.ATTACHED_TO_PICKLIST_VALUE_QAQA.value)

            # Must use the following loop, as part of names from picklist do not have values and are not clicked,
            # Randomly, and different on each bran
            counter = 0
            for name_item in attached_to_pick_list_item:
                if "qa qa" in name_item.text:
                    self.driver.execute_script("arguments[0].click();", attached_to_pick_list_item[counter])
                    break
                counter += 1

            time.sleep(2)

            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.ADD_DOCUMENT_BUTTON))).click()

        except:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="create_new_document",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("DocumentsListView.new_document_verification() | New Document Verification")
    def new_document_verification(self):
            time.sleep(12)
            self.driver.refresh()
            time.sleep(8)

            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.DOCUMENT_1ST_ITEM_LIST_VIEW))).click()

            time.sleep(10)

            if (len(self.driver.find_elements(By.XPATH, CrmElements.DOCUMENT_DETAILS_VIEW_VERIFICATION)) == 0):
                assert False

            else:
                pass


import time

import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchbarElements, SearchBar
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, RightSliderConstants
from src.infrastructure.dynamic_helpers.ScrollActions import ScrollActions
from src.elements.CrmElements import CrmElements


class AffiliatesListView(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Affiliates.go_to() | Navigating to Affiliates")
    def go_to(self):
        try:
            time.sleep(4)
            # Scrolling to element 'Affiliates' module
            ScrollActions.scroll_to(self.driver.find_element(By.XPATH, CrmElements.SIDE_MENU_AFFILIATES))

            # Clicking on 'Affiliates'
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_AFFILIATES))).click()

            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(By.XPATH, CrmElements.SIDE_MENU_AFFILIATES))

            time.sleep(15)

            WebDriverWait(self.driver, 50).until(
                EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        except:
            self.driver.refresh()

            time.sleep(15)

    # Secret-key is copied using 'copy' button
    # partnerId is copied using 'partner_id_code' variable and returned at the end
    @allure.step("Affiliates.get_secret_key() | Getting 'secret-key' for Api module")
    def get_secret_key(self):
        # Getting secret key
        time.sleep(2)
        partner_id_code_element = self.driver.find_element(By.XPATH, CrmElements.AFFILIATES_PARTNER_ID_TEXT).text

        time.sleep(5)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.FILTER_COPY_CONTENT_BUTTON))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.FILTER_COPY_CONTENT_BUTTON))).click()
        time.sleep(2)
        return partner_id_code_element

    @allure.step("Affiliates.create_affiliate() | Create new affiliate")
    def create_affiliate(self, new_affiliate_name):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        CrmElements.CREATE_NEW_AFFILIATE_BUTTON))).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ALLOWED_IP_FIELD))).send_keys("1.1.1.1")

        time.sleep(1)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ADD_BUTTON))).click()

        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.PARTNER_NAME_FIELD.value).send_keys(
            new_affiliate_name)

        time.sleep(1)
        allowed_methods_picklist_item = RightSliderElements.choose_item_by_value_out_of_affiliates_picklist(self.driver,
                                                                                                            RightSliderConstants.CREATE_LEAD_VALUE.value)
        self.driver.execute_script("arguments[0].click();", allowed_methods_picklist_item)

        time.sleep(1)

        blocked_countries_picklist_item = RightSliderElements.choose_item_by_value_out_of_affiliates_picklist(
            self.driver,
            RightSliderConstants.AFGHANISTAN_VALUE.value)
        self.driver.execute_script("arguments[0].click();", blocked_countries_picklist_item)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SAVE_BUTTON))).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    @allure.step("Affiliates.remove_created_affiliate() | Delete newly created affiliate")
    def remove_created_affiliate(self):
        counter = 0

        while (counter < 10) and (len(self.driver.find_elements(By.XPATH, CrmElements.MORE_BUTTON))) >0:
            print("DEBUG")
            print(counter)

            counter += 1
            time.sleep(3)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            CrmElements.MORE_BUTTON))).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            CrmElements.BIN_BUTTON))).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            CrmElements.DELETE_BUTTON))).click()

            time.sleep(1.5)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            CrmElements.OK_BUTTON))).click()

    @allure.step("Affiliates.remove_created_affiliate_verification() | Delete newly created affiliate")
    def remove_created_affiliate_verification(self):

        # Once search-bar value inserted, if there are not 'More' buttons, then verification passed
        if (len(self.driver.find_elements(By.XPATH, CrmElements.MORE_BUTTON))) >0:
            assert False

        else:
            pass

import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, RightSliderConstants
from src.elements.dynamic_elements.CrmSideMenuElements import CrmSideMenu, Modules


class FinancialTransactionsListView():

    def __init__(self, driver):
        self.driver = driver

    @allure.step("FinancialTransactionsListView.go_to() | Navigating to financial transactions")
    def go_to(self):
        try:
            # Navigating to clients module screen
            CrmSideMenu.side_menu_items(self.driver, Modules.FINANCIAL_TRANSACTIONS_MODULE.value).click()

        except:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="ClientsModule.go_to",
                          attachment_type=AttachmentType.PNG)
            assert False


    @allure.step("FinancialTransactionsListView.create_filter() | Create new filter")
    def create_new_filter(self):
        time.sleep(2)
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CREATE_NEW_FILTER_BUTTON))).click()

        view_name_field = RightSliderElements.insert_value_to_field(self.driver,RightSliderConstants.VIEW_NAME.value)

        view_name_field.send_keys("Test Financial Auto []")

        self.driver.find_element(By.XPATH,CrmElements.CREATE_NEW_FILTER_ADD_COLUMN_FIELD).click()

        time.sleep(1)


        transaction_no = RightSliderElements.create_new_filter_screen_add_column(self.driver,RightSliderConstants.TRANSACTION_NO_FILTER_COLUMN_VALUE.value)
        transaction_no.click()

        client_name = RightSliderElements.create_new_filter_screen_add_column(self.driver,RightSliderConstants.CLIENT_NAME_FILTER_COLUMN_VALUE.value)
        client_name.click()

        assigned_to = RightSliderElements.create_new_filter_screen_add_column(self.driver,RightSliderConstants.ASSIGNED_TO_FILTER_COLUMN_VALUE.value)
        assigned_to.click()

        transaction_approval = RightSliderElements.create_new_filter_screen_add_column(self.driver,RightSliderConstants.TRANSACTION_APPROVAL_FILTER_COLUMN_VALUE.value)
        transaction_approval.click()

        transaction_type = RightSliderElements.create_new_filter_screen_add_column(self.driver,RightSliderConstants.TRANSACTION_TYPE_FILTER_COLUMN_VALUE.value)
        transaction_type.click()

        view_name_field.click()

        time.sleep(1)

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CREATE_NEW_FILTER_BUTTON_SAVE_CHANGES))).click()


        time.sleep(15)













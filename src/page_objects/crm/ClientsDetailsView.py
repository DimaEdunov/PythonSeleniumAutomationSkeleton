import time
from time import sleep

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmClientDetailsViewMtMenu import CrmClientDetailsViewMtActions, \
    CrmClientDetailsViewMtMenuConstants
from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldElements, FieldName
from src.elements.dynamic_elements.CrmDetailsViewSectionElements import SectionElements, Section, \
    SortButtonsValuesInSection
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchbarElements, SearchBar
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, RightSliderConstants
from src.infrastructure.dynamic_helpers.ScrollActions import ScrollActions
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView, EditFieldValues
from src.page_objects.crm.WorkflowsAddTasks import WorkflowAddTasksConstants

class ClientDetailsView(object):
    from datetime import datetime
    random_number_variable = datetime.now().strftime('%H%M')

    global newly_set_password
    newly_set_password = "Aa1111%s" % random_number_variable

    def __init__(self, driver):
        self.driver = driver

    @allure.step(
        "CrossModuleDetailsView.go_to_via_searchbar_using_email() | Navigating to details view via search by using email")
    def go_to_via_searchbar_using_client_name(self, client_name):
        SearchbarElements.bar_choose_element(self.driver, SearchBar.CLIENT_NAME.value).click()
        SearchbarElements.bar_insert_value_field_element(self.driver, SearchBar.CLIENT_NAME.value).send_keys(
            client_name)

        sleep(1)
        self.driver.find_element(By.XPATH, CrmElements.FILTER_AGREE_BUTTON).click()

        WebDriverWait(self.driver, 45).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        clicked_item = CrmElements.CRM_ID_LIST

        first_client_item = self.driver.find_elements(By.XPATH, clicked_item)[0]
        sleep(1)
        self.driver.execute_script("arguments[0].click();", first_client_item)

    @allure.step("ClinetsDetailsView.assigned_to")
    def client_assigned_to(self, crm_user):

        time.sleep(5)
        FieldElements.change_assigned_to_value(self.driver, FieldName.ASSIGNED_TO_FIELD.value, crm_user)

    @allure.step("ClientDetailsView_create_client_verification() | Verifying creation of a Client / Customer")
    def create_client_verification(self, email_value, first_name_value, last_name_value):
        sleep(3)
        if FieldElements.get_field_value(self.driver, FieldName.EMAIL_FIELD.value).text == email_value or "****" and \
                FieldElements.get_field_value(self.driver,
                                              FieldName.FIRST_NAME_FIELD.value).text == first_name_value and \
                FieldElements.get_field_value(self.driver,
                                              FieldName.LAST_NAME_FIELD.value).text == last_name_value:
            print("DEBUG - Verification passed")

        else:
            print("DEBUG - Verification failed")
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="ClientDetailsView.api_create_client_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("ClientDetailsView.api_update_client_verification() | Verifying update of API Customer")
    def api_update_client_verification(self, first_name_value, postal_code_value, phone_value):
        sleep(3)
        address_section = SectionElements.open_section(self.driver, Section.ADDRESS_INFORMATION.value)
        self.driver.execute_script("arguments[0].click();", address_section)
        if FieldElements.get_field_value(self.driver, FieldName.PHONE_FIELD.value).text == phone_value or "****" and \
                FieldElements.get_field_value(self.driver,
                                              FieldName.FIRST_NAME_FIELD.value).text == first_name_value and \
                FieldElements.get_field_value(self.driver,
                                              FieldName.CODE_FIELD.value).text == postal_code_value:
            print("DEBUG - Verification passed")

        else:
            print("DEBUG - Verification failed")
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="ClientDetailsView.api_update_client_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("CrossModuleDetailsView.comparator_string() | Compare 2 string values")
    def workflow_client_verification(self):
        self.driver.refresh()
        client_details = CrossModuleDetailsView(self.driver)
        client_details.open_tab(EditFieldValues.ADDRESS_INFORMATION_TAB.value)
        country = client_details.get_text_from_field(EditFieldValues.COUNTRY_FIELD.value)
        address = client_details.get_text_from_field(EditFieldValues.ADDRESS_FIELD.value)

        counter = 0
        while country != WorkflowAddTasksConstants.COUNTRY_ALBANIA_VALUE.value and \
                address != WorkflowAddTasksConstants.TEST_ADDRESS_VALUE.value:

            self.driver.refresh()

            client_details.open_tab(EditFieldValues.ADDRESS_INFORMATION_TAB.value)
            country = client_details.get_text_from_field(EditFieldValues.COUNTRY_FIELD.value)
            address = client_details.get_text_from_field(EditFieldValues.ADDRESS_FIELD.value)
            counter += 1
            if counter == 5:
                break

    @allure.step("CrossModuleDetailsView.pencil_edit_for_workflow() | Edit Client for workflow test")
    def pencil_edit_for_workflow(self):
        # set birthday
        sleep(0.1)

        date_field = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.RIGHT_SLIDER_DATE_FIELD)))
        self.driver.execute_script("arguments[0].click();", date_field)

        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.RIGHT_SLIDER_CURRENT_DATE_BUTTON))).click()

        prev_button = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.RIGHT_SLIDER_PREVIOUS_BUTTON)))

        prev_button.click()
        sleep(0.5)

        prev_button.click()

        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.RIGHT_SLIDER_YEAR_VALUE))).click()

        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.RIGHT_SLIDER_MONTH_VALUE))).click()

        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.RIGHT_SLIDER_DAY_VALUE))).click()

        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.RIGHT_SLIDER_SET_BUTTON))).click()

        # set citizenship
        citizenship_value = RightSliderElements \
            .choose_item_by_value_out_of_specific_picklist(self.driver,
                                                           RightSliderConstants.CITIZENSHIP_PICKLIST.value,
                                                           RightSliderConstants.CITIZENSHIP_PICKLIST_VALUE.value)

        self.driver.execute_script("arguments[0].click();", citizenship_value)

        # set city
        city_field = RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.CITY_FIELD.value)
        city_field.clear()
        city_field.send_keys("City")

        # set postal code
        code_field = RightSliderElements.insert_value_to_field(self.driver,
                                                               RightSliderConstants.POSTAL_CODE_FIELD.value)
        code_field.clear()
        code_field.send_keys("123123")

        # set address
        address_field = RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.ADDRESS_FIELD.value)
        address_field.clear()
        address_field.send_keys("Address")

        # set country
        country_value = RightSliderElements \
            .choose_item_by_value_out_of_specific_picklist(self.driver,
                                                           RightSliderConstants.COUNTRY_PICKLIST.value,
                                                           RightSliderConstants.COUNTRY_PICKLIST_VALUE.value)

        self.driver.execute_script("arguments[0].click();", country_value)

        # click save button
        save_button = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.EDIT_CLIENT_SAVE_BUTTON)))
        self.driver.execute_script("arguments[0].click();", save_button)

        sleep(1)
        WebDriverWait(self.driver, 45).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

    @allure.step("ClientDetailsView.open_trading_account_menu()")
    def open_trading_account_menu(self):
        time.sleep(15)
        self.driver.refresh()

        time.sleep(8)

        print("DEBUG 1")
        # Open menu, brands have 2 types of menus, Type_1, Type_2
        try:
            CrmClientDetailsViewMtActions.open_close_mt_menu(self.driver,
                                                             CrmClientDetailsViewMtMenuConstants.MT_ACTIONS_MENU_TYPE_1.value).click()
        except:
            CrmClientDetailsViewMtActions.open_close_mt_menu(self.driver,
                                                             CrmClientDetailsViewMtMenuConstants.MT_ACTIONS_MENU_TYPE_2.value).click()
        time.sleep(2)

    @allure.step("ClientDetailsView.create_trading_account() | Create a trading account. Live or Demo")
    def create_trading_account(self, trading_account_type):

        # Click on 'Create Trading Account' button on MT menu/ brands have 2 types of 'create' buttons, Type_1, Type_2
        try:
            CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver,
                                                             CrmClientDetailsViewMtMenuConstants.CREATE_TRADING_ACCOUNT_TYPE_1.value).click()
        except:
            CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver,
                                                             CrmClientDetailsViewMtMenuConstants.CREATE_TRADING_ACCOUNT_TYPE_2.value).click()

        time.sleep(4)

        if trading_account_type == "demo":
            server_picklist_demo_server = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                            RightSliderConstants.SERVER_PICKLIST.value,
                                                                                                            RightSliderConstants.DEMO_VALUE.value)
            self.driver.execute_script("arguments[0].click();", server_picklist_demo_server)
        print("DEBUG 2")

        if trading_account_type == "live":
            server_picklist_live_server = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                            RightSliderConstants.SERVER_PICKLIST.value,
                                                                                                            RightSliderConstants.LIVE_VALUE.value)
            self.driver.execute_script("arguments[0].click();", server_picklist_live_server)

        time.sleep(2)
        currency_items = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                           RightSliderConstants.CURRENCY_PICKLIST.value)

        self.driver.execute_script("arguments[0].click();", currency_items[0])

        print("DEBUG 3")
        time.sleep(3)

        group_items = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                        RightSliderConstants.GROUP_PICKLIST.value)
        self.driver.execute_script("arguments[0].click();", group_items[0])

        leverage_picklist_item = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                   RightSliderConstants.LEVERAGE_PICKLIST.value,
                                                                                                   RightSliderConstants.LEVERAGE_VALUE.value)
        self.driver.execute_script("arguments[0].click();", leverage_picklist_item)
        print("DEBUG 4")
        time.sleep(2)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RIGHT_SLIDER_CREATE_BUTTON))).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    @allure.step("ClientDetailsView.create_trading_account_verification() | Verifying creation of trading account")
    def create_trading_account_verification(self, trading_account_type):

        print("DEBUG Verification")

        ScrollActions.scroll_to(SectionElements.open_section(self.driver, Section.TRADING_ACCOUNTS.value))

        time.sleep(5)

        SectionElements.open_section(self.driver, Section.TRADING_ACCOUNTS.value).click()

        time.sleep(4)

        if trading_account_type == "demo":

            if len(self.driver.find_elements(By.XPATH, CrmElements.TRADING_ACCOUNTS_DEMO_ACCOUNT_VERIFICATION)) > 0:
                print("Verification passed")

            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="create_trading_account_verification",
                              attachment_type=AttachmentType.PNG)
                assert False

        if trading_account_type == "live":

            if len(self.driver.find_elements(By.XPATH, CrmElements.TRADING_ACCOUNTS_LIVE_ACCOUNT_VERIFICATION)) > 0:
                print("Verification passed")

            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="create_trading_account_verification",
                              attachment_type=AttachmentType.PNG)
                assert False

        self.driver.refresh()
        time.sleep(8)

    @allure.step("ClientDetailsView.make_a_deposit() | Make a deposit")
    def make_a_deposit(self, deposit_amount):

        CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver,
                                                         CrmClientDetailsViewMtMenuConstants.DEPOSIT.value).click()

        payment_method_picklist = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                    RightSliderConstants.PAYMENT_METHOD_PICKLIST.value,
                                                                                                    RightSliderConstants.ADJUSTMENT_VALUE.value)

        self.driver.execute_script("arguments[0].click();", payment_method_picklist)

        status_picklist = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                            RightSliderConstants.STATUS_NAME_OF_PICKLIST.value,
                                                                                            RightSliderConstants.APPROVED_VALUE.value)

        self.driver.execute_script("arguments[0].click();", status_picklist)

        # Choose trading account, by index (Pick first)
        trading_account_items = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                                  RightSliderConstants.TRADING_ACCOUNTS_PICKLIST.value)
        self.driver.execute_script("arguments[0].click();", trading_account_items[0])

        time.sleep(2)

        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.AMOUNT_IN_ACCOUNT_CURRENCY_FIELD.value).send_keys(
            deposit_amount)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.DEPOSIT_BUTTON))).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        time.sleep(4)

    @allure.step("ClientDetailsView.make_a_deposit_verification() | Verify a deposit")
    def make_a_deposit_verification(self):
        self.driver.refresh()
        time.sleep(8)

        ScrollActions.scroll_to(SectionElements.open_section(self.driver, Section.FINANCIAL_TRANSACTIONS.value))

        time.sleep(8)

        SectionElements.open_section(self.driver, Section.FINANCIAL_TRANSACTIONS.value).click()

        time.sleep(3)

        if len(self.driver.find_elements(By.XPATH, CrmElements.FINANCIAL_TRANSACTIONS_DEPOSIT_VERIFICATION)) > 0:
            print("Verification passed")

        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="make_a_deposit_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("ClientDetailsView.make_a_withdraw() | Make a withdraw")
    def make_a_withdraw(self, withdraw_amount):

        self.driver.refresh()

        time.sleep(5)

        # Open menu, brands have 2 types of menus, Type_1, Type_2
        try:
            CrmClientDetailsViewMtActions.open_close_mt_menu(self.driver,
                                                             CrmClientDetailsViewMtMenuConstants.MT_ACTIONS_MENU_TYPE_1.value).click()
        except:
            CrmClientDetailsViewMtActions.open_close_mt_menu(self.driver,
                                                             CrmClientDetailsViewMtMenuConstants.MT_ACTIONS_MENU_TYPE_2.value).click()

        CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver,
                                                         CrmClientDetailsViewMtMenuConstants.WITHDRAW.value).click()

        status_picklist = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                            RightSliderConstants.STATUS_NAME_OF_PICKLIST.value,
                                                                                            RightSliderConstants.APPROVED_VALUE.value)
        self.driver.execute_script("arguments[0].click();", status_picklist)

        # Choose payment method, if crypto choose 'Other' else choose the first by index
        try:
            payment_method_picklist = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                        RightSliderConstants.PAYMENT_METHOD_PICKLIST.value,
                                                                                                        RightSliderConstants.OTHER_VALUE.value)
            self.driver.execute_script("arguments[0].click();", payment_method_picklist)

        except:

            payment_method_picklist = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                                        RightSliderConstants.PAYMENT_METHOD_PICKLIST.value)
            self.driver.execute_script("arguments[0].click();", payment_method_picklist[0])

        # Choose trading account, by index (Pick first item)
        trading_account_items = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                                  RightSliderConstants.TRADING_ACCOUNTS_PICKLIST.value)
        self.driver.execute_script("arguments[0].click();", trading_account_items[0])

        # Choose amount to withdraw
        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.AMOUNT_IN_ACCOUNT_CURRENCY_FIELD.value).send_keys(
            withdraw_amount)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.WITHDRAW_BUTTON))).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        time.sleep(4)

    @allure.step("ClientDetailsView.make_a_withdraw_verification() | Verify a withdraw")
    def make_a_withdraw_verification(self):
        self.driver.refresh()

        time.sleep(5)

        ScrollActions.scroll_to(SectionElements.open_section(self.driver, Section.FINANCIAL_TRANSACTIONS.value))

        SectionElements.open_section(self.driver, Section.FINANCIAL_TRANSACTIONS.value).click()

        time.sleep(3)

        if len(self.driver.find_elements(By.XPATH, CrmElements.FINANCIAL_TRANSACTIONS_WITHDRAW_VERIFICATION)) > 0:
            print("Verification passed")

        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="make_a_deposit_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("ClientDetailsView.transfer_between_ta() | Transfer funds between live accounts")
    def transfer_between_ta(self, transfer_between_ta_amount):
        self.driver.refresh()

        time.sleep(5)

        # Open menu, brands have 2 types of menus, Type_1, Type_2
        try:
            CrmClientDetailsViewMtActions.open_close_mt_menu(self.driver,
                                                             CrmClientDetailsViewMtMenuConstants.MT_ACTIONS_MENU_TYPE_1.value).click()
        except:
            CrmClientDetailsViewMtActions.open_close_mt_menu(self.driver,
                                                             CrmClientDetailsViewMtMenuConstants.MT_ACTIONS_MENU_TYPE_2.value).click()

        CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver,
                                                         CrmClientDetailsViewMtMenuConstants.TRANSFER_BETWEEN_TA.value).click()

        time.sleep(1)
        source_picklist_items = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                                  RightSliderConstants.SOURCE_PICKLIST.value)

        self.driver.execute_script("arguments[0].click();", source_picklist_items[0])

        time.sleep(1)
        destination_picklist_items = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                                       RightSliderConstants.DESTINATION_PICKLIST.value)

        self.driver.execute_script("arguments[0].click();", destination_picklist_items[0])

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.AMOUNT.value). \
            send_keys(transfer_between_ta_amount)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.TRANSFER_BUTTON))).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        time.sleep(10)

    @allure.step("ClientDetailsView.transfer_between_ta_verification() | Verify transfer funds between live accounts")
    def transfer_between_ta_verification(self):
        self.driver.refresh()

        time.sleep(5)

        ScrollActions.scroll_to(SectionElements.open_section(self.driver, Section.FINANCIAL_TRANSACTIONS.value))

        SectionElements.open_section(self.driver, Section.FINANCIAL_TRANSACTIONS.value).click()

        time.sleep(3)

        if len(self.driver.find_elements(By.XPATH,
                                         CrmElements.FINANCIAL_TRANSACTIONS_TRANSFER_BETWEEN_TA_VERIFICATION)) > 1:
            print("Verification passed")

        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="make_a_deposit_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("ClientDetailsView.change_crm_password() | Check the password using mt bar")
    def change_crm_password(self):
        self.driver.refresh()
        time.sleep(6)

        CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver,
                                                         CrmClientDetailsViewMtMenuConstants.MANAGE_TA_PASSWORD.value).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CHANGE_PASSWORD_FIELD))).clear()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CHANGE_PASSWORD_FIELD))).send_keys(
            newly_set_password)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CHANGE_PASSWORD_BUTTON))).click()

        time.sleep(2)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        time.sleep(3)

    @allure.step("ClientDetailsView.check_crm_password() | Check crm password")
    def check_crm_password(self):
        self.driver.refresh()
        time.sleep(6)

        CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver,
                                                         CrmClientDetailsViewMtMenuConstants.MANAGE_TA_PASSWORD.value).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CHECK_PASSWORD_FIELD))).clear()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CHECK_PASSWORD_FIELD))).send_keys(newly_set_password)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CHECK_PASSWORD_BUTTON))).click()

        time.sleep(2)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

        time.sleep(3)

    @allure.step("ClientDetailsView.make_a_credit_in() | Credit in")
    def make_a_credit_in(self, credit_in_amount):

        CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver,
                                                         CrmClientDetailsViewMtMenuConstants.CREDIT_IN.value).click()

        # Choose trading account, by index (Pick first)
        trading_account_items = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                                  RightSliderConstants.TRADING_ACCOUNTS_PICKLIST.value)
        self.driver.execute_script("arguments[0].click();", trading_account_items[0])

        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.AMOUNT_IN_ACCOUNT_CURRENCY_FIELD.value).send_keys(
            credit_in_amount)

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.COMMENT_FIELD.value).send_keys(
            "test qa")

        # Save changes

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CREDIT_IN_BUTTON))).click()

        time.sleep(6)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    @allure.step("ClientDetailsView.make_a_credit_in_verification() | Credit in verification")
    def make_a_credit_in_verification(self):
        self.driver.refresh()

        ScrollActions.scroll_to(SectionElements.open_section(self.driver, Section.HELP_DESK.value))

        SectionElements.open_section(self.driver, Section.FINANCIAL_TRANSACTIONS.value).click()

        time.sleep(3)

        if len(self.driver.find_elements(By.XPATH, CrmElements.FINANCIAL_TRANSACTIONS_CREDIT_IN_VERIFICATION)) > 0:
            print("Verification passed")

        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="make_a_credit_in_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("ClientDetailsView.make_a_credit_out() | Credit out")
    def make_a_credit_out(self, credit_out_amount):

        CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver,
                                                         CrmClientDetailsViewMtMenuConstants.CREDIT_OUT.value).click()

        #  Choose trading account, by index (Pick first)
        trading_account_items = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                                  RightSliderConstants.TRADING_ACCOUNTS_PICKLIST.value)
        self.driver.execute_script("arguments[0].click();", trading_account_items[0])

        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.AMOUNT_IN_ACCOUNT_CURRENCY_FIELD.value).send_keys(
            credit_out_amount)

        RightSliderElements.insert_value_to_field(self.driver,
                                                  RightSliderConstants.COMMENT_FIELD.value).send_keys("test qa")

        # Save changes
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CREDIT_OUT_BUTTON))).click()

        time.sleep(6)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    @allure.step("ClientDetailsView.make_a_credit_out_verification() | Credit out verification")
    def make_a_credit_out_verification(self):
        self.driver.refresh()

        ScrollActions.scroll_to(SectionElements.open_section(self.driver, Section.HELP_DESK.value))

        SectionElements.open_section(self.driver, Section.FINANCIAL_TRANSACTIONS.value).click()

        time.sleep(3)

        if len(self.driver.find_elements(By.XPATH, CrmElements.FINANCIAL_TRANSACTIONS_CREDIT_OUT_VERIFICATION)) > 0:
            print("Verification passed")

        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="make_a_credit_out_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("ClientDetailsView.make_an_interaction_verification() | Verify a interaction")
    def client_details_view_add_interaction_verification(self, subject_input):
        self.driver.refresh()
        time.sleep(10)

        ScrollActions.scroll_to(SectionElements.open_section(self.driver, Section.ACTIVITIES.value))

        time.sleep(3)

        SectionElements.open_section(self.driver, Section.ACTIVITIES.value).click()

        time.sleep(8)

        SectionElements.sort_button(self.driver, SortButtonsValuesInSection.START_DATE.value).click()

        time.sleep(3)

        if self.driver.find_element(By.XPATH, CrmElements.CLIENT_DETAILS_VIEW_SUBJECT_FIELD).text == subject_input:
            print("Verification passed")
        else:
            # 2nd try (Refresh) procedure
            try:
                SectionElements.open_section(self.driver, Section.ACTIVITIES.value).click()

                time.sleep(8)

                SectionElements.sort_button(self.driver, SortButtonsValuesInSection.START_DATE.value).click()

                time.sleep(3)

                if self.driver.find_element(By.XPATH,
                                            CrmElements.CLIENT_DETAILS_VIEW_SUBJECT_FIELD).text == subject_input:
                    print("Verification passed")
            except:
                assert False

            assert False

    @allure.step("ClientDetailsView.update_mt4_user() | Update MT4 User")
    def update_mt4_user(self):

        time.sleep(5)

        CrmClientDetailsViewMtActions.mt_sidemenu_button(self.driver, CrmClientDetailsViewMtMenuConstants.UPDATE_TRADING_ACCOUNT.value).click()

        trading_account = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                        RightSliderConstants.CHANGE_MT4_TRADING_ACCOUNTS_PICKLIST.value,
                                                                                                        RightSliderConstants.DEMO_TA_VALUE.value)

        self.driver.execute_script("arguments[0].click();", trading_account)

        leverage_picklist = RightSliderElements.choose_item_by_index_out_of_specific_picklist(self.driver,
                                                                                                  RightSliderConstants.LEVERAGE_PICKLIST.value)
        self.driver.execute_script("arguments[0].click();", leverage_picklist[2])


        right_slider_leverage_value = RightSliderElements.field_value(self.driver, RightSliderConstants.LEVERAGE_PICKLIST.value).text

        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.UPDATE_MT_ACCOUNT_READ_ONLY_CHECKBOX))).click()

        time.sleep(2)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.UPDATE_MT_ACCOUNT_BUTTON))).click()

        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()
        time.sleep(4)

        return right_slider_leverage_value

    @allure.step("ClientDetailsView.update_mt4_user_verification() | Update Mt4 User Verification")
    def update_mt4_user_verification(self, right_slider_leverage_value):
        self.driver.refresh()
        time.sleep(10)

        ScrollActions.scroll_to(SectionElements.open_section(self.driver, Section.TRADING_ACCOUNTS.value))
        time.sleep(3)

        SectionElements.open_section(self.driver, Section.TRADING_ACCOUNTS.value).click()
        time.sleep(8)

        SectionElements.sort_button(self.driver, SortButtonsValuesInSection.SERVER.value).click()
        time.sleep(3)

        if self.driver.find_element(By.XPATH, CrmElements.CLIENT_DETAILS_VIEW_LEVERAGE_FIELD).text in right_slider_leverage_value\
                and self.driver.find_element(By.XPATH, CrmElements.CLIENT_DETAILS_VIEW_READ_ONLY_FIELD).text == "yes":
            print("Verification passed")
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="update_mt4_user_verification",
                          attachment_type=AttachmentType.PNG)
            assert False
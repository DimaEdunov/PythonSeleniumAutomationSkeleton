from datetime import *
import time
from enum import Enum
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

""" Works in all modules beside:
 1) Help-Desk : Which you can find it's elements in CrmHelpDeskRightSliderFieldElements
 2) Documents : Is structured in a way where the 'label' of the picklists and 'picklist' itself are not connected at all
 So - There is not point to use 'dynamic element', find document's elements in 'CrmElements'
 
 """

class RightSliderConstants(Enum):

    # In right slider screen, 'Description' field is exceptional regarding elements attributes
    HELP_DESK_DESCRIPTION_FIELD = "Description information"

    # Field names
    FIRST_NAME_FIELD = "First"
    LAST_NAME_FIELD = "Last"
    EMAIL_FIELD = "Email"
    CITY_FIELD = "City"
    LANGUAGE_FIELD = "Language"
    TITLE_FIELD = "Title"
    DESCRIPTION_INFORMATION_FIELD = "Description information"
    PARTNER_NAME_FIELD = "Partner name"
    SUBJECT_FIELD = "Subject"
    COMMENTS_FIELD = "Comments"
    COMMENT_FIELD = "Comment"
    VIEW_NAME = "View name"

    POSTAL_CODE_FIELD = "Postal code"
    ADDRESS_FIELD = "Address"
    PHONE_FIELD = "Phone"
    BIRTHDAY_FIELD = "Date Of Birth"
    AMOUNT_IN_ACCOUNT_CURRENCY_FIELD = "Amount in account currency"
    AMOUNT = "Amount"

    # Name of picklist
    ASSIGNED_TO_NAME_OF_PICKLIST = "Assigned To"
    ASSIGN_TO_NAME_OF_PICKLIST = "Assign To"  # Tasks module
    LEAD_STATUS_NAME_OF_PICKLIST = "Lead Status"
    STATUS_NAME_OF_PICKLIST = "Status"
    CATEGORY_NAME_OF_PICKLIST = "Category"
    ATTACHED_TO = "Attached To"
    CITIZENSHIP_PICKLIST = "Citizenship"
    COUNTRY_PICKLIST = "Country"
    ATTACHED_TO_PICKLIST = "Attached To"
    SERVER_PICKLIST = "Server"
    LEVERAGE_PICKLIST = "Leverage"
    CURRENCY_PICKLIST = "Currency"
    GROUP_PICKLIST = "Group"
    PAYMENT_METHOD_PICKLIST = "Payment method"
    TRADING_ACCOUNTS_PICKLIST = "Trading account"
    CHANGE_MT4_TRADING_ACCOUNTS_PICKLIST = "Trading Account"
    SOURCE_PICKLIST = "Source"
    DESTINATION_PICKLIST = "Destination"
    UI_LANGUAGE = "UI Language"
    EVENT_TYPE_PICKLIST = "Event Type"
    EVENT_DURATION_PICKLIST = "Duration"
    EVENT_STATUS_PICKLIST = "Event Status"

    # Value in picklist
    ASSIGNED_TO_PICKLIST_VALUE = "Panda Auto"
    ATTACHED_TO_PICKLIST_VALUE = "dima edunov"
    ATTACHED_TO_PICKLIST_VALUE_QAQA = "qa qa"
    ASSIGN_TO_PICKLIST_VALUE = "Anastasiia V"
    STATUS_FTD_PICKLIST_VALUE = "FTD"
    STATUS_OPEN_PICKLIST_VALUE = "Open"
    CATEGORY_PICKLIST_VALUE = "General Question"
    CREATE_LEAD = "Create lead"
    AFGHANISTAN = "Afghanistan"
    CITIZENSHIP_PICKLIST_VALUE = "Albanian"
    COUNTRY_PICKLIST_VALUE = "Guam"
    CREATE_LEAD_VALUE = "Create lead"
    AFGHANISTAN_VALUE = "Afghanistan"
    LIVE_VALUE = "Live"
    DEMO_VALUE = "Demo"
    DEMO_TA_VALUE = "demo"
    LEVERAGE_VALUE = "1"
    LEVERAGE_UPDATE_INDEX_VALUE = "4"
    ADJUSTMENT_VALUE = "Adjustment"
    APPROVED_VALUE = "Approved"
    CITIZENSHIP_VALUE = "Afghan"
    OTHER_VALUE = "Other"
    CALL_VALUE = "Call"
    MEETING_VALUE = "Meeting"
    EVENT_TYPE_VALUE = "Call"
    TASK_STATUS_VALUE = "Planned"
    TASK_DURATION_VALUE = "30M"
    UI_LANGUAGE_ENGLISH_VALUE = "Language"
    EVENT_STATUS_PICKLIST_VALUE = "In Progress"

    # New values in adding columns in 'filters'
    TRANSACTION_NO_FILTER_COLUMN_VALUE = "Transaction No"
    CLIENT_NAME_FILTER_COLUMN_VALUE = "Client name"
    TRANSACTION_TYPE_FILTER_COLUMN_VALUE = "Transaction Type"
    TRANSACTION_APPROVAL_FILTER_COLUMN_VALUE = "Transaction Approval"
    ASSIGNED_TO_FILTER_COLUMN_VALUE = "Assigned To"


class RightSliderElements():

    @staticmethod
    def insert_value_into_description_field(driver, description_field_attribute):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(label,'%s')]//following-sibling::mat-form-field//div//div//div//textarea" % description_field_attribute)))

        return driver.find_element(By.XPATH,
                                   "//div[contains(label,'%s')]//following-sibling::mat-form-field//div//div//div//textarea" % description_field_attribute)

    @staticmethod
    def insert_value_to_field(driver, field_name):
        time.sleep(3)

        return driver.find_element(By.XPATH,
                                        "//div[contains(label,'%s')]//following-sibling::mat-form-field//input" % field_name)

    @staticmethod
    def choose_item_by_value_out_of_specific_picklist(driver, pick_list_name, value_name):
        time.sleep(2)
        click_on_picklist = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                            "//mat-sidenav//span[contains(text(),'%s ')]//following-sibling::div/span" % pick_list_name)))

        driver.execute_script("arguments[0].click();", click_on_picklist)

        time.sleep(4)

        pick_list = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                    "//mat-sidenav//span[contains(text(),'%s ')]//following-sibling::ul//a[contains(@title,'%s')]" % (pick_list_name, value_name))))

        return pick_list

    @staticmethod
    def choose_item_by_index_out_of_specific_picklist(driver, pick_list_name):
        time.sleep(2.5)

        click_on_picklist = driver.find_element(By.XPATH, "//span[contains(text(),'%s')]//following-sibling::ul//span" % pick_list_name)

        driver.execute_script("arguments[0].click();", click_on_picklist)

        time.sleep(1.5)

        pick_list_items = driver.find_elements(By.XPATH,
                                        "//span[contains(text(),'%s')]//following-sibling::ul//span" % (pick_list_name))

        time.sleep(1.5)
        return pick_list_items

    @staticmethod
    def choose_item_by_value_out_of_affiliates_picklist(driver, value_name):
        time.sleep(2)
        pick_list_item = driver.find_element(By.XPATH, "(//span[contains(text(),'%s')])[1]" % (value_name))

        time.sleep(2)
        return pick_list_item

    # The above method 'choose_value_out_of_specific_picklist' does not apply to 'Tasks' RightSlider screen, attached to picklist

    @staticmethod
    def choose_item_by_value_out_of_attached_to_picklist(driver, pick_list_name, value_name):

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//span[text()=' %s  ']//following-sibling::div/span" % pick_list_name))).click()

        pick_list_input_field = driver.find_element(By.XPATH,
                                                    "//span[text()=' %s  ']//following-sibling::div//input"
                                                    % pick_list_name)
        pick_list_input_field.click()

        pick_list_input_field.send_keys(value_name)

        time.sleep(2)

        pick_list_select_item = driver.find_elements(By.XPATH, "(//li/a/span[contains(text(),'%s')])" % value_name)

        time.sleep(2)

        return pick_list_select_item

    @staticmethod
    def create_new_filter_screen_add_column(driver, search_for_value):
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//section[@class='select-list']//input[@autocomplete='off']"))).click()
        driver.find_element(By.XPATH, "//section[@class='select-list']//input[@autocomplete='off']").clear()
        driver.find_element(By.XPATH, "//section[@class='select-list']//input[@autocomplete='off']").send_keys(search_for_value)

        return driver.find_element(By.XPATH, "//div[@class='input-wrap open']//ul//a")

    @staticmethod
    def choose_date_of_birth(driver, year, month, day):
        # Open calendar
        date_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//input[@placeholder='Choose date of birth']")))

        driver.execute_script("arguments[0].click();", date_field)

        # Click on current date
        current_date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "(//span[@class='mat-button-wrapper' and contains(text(),'2020')])[1]")))

        current_date.click()

        previous_year_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "(//button[@class='mat-calendar-previous-button mat-icon-button mat-button-base'])[1]")))

        previous_year_button.click()
        time.sleep(0.5)
        previous_year_button.click()

        select_year = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(text(),'%s')]" % year)))

        select_year.click()

        select_month = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(text(),'%s')]" % month)))

        select_month.click()

        select_day = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(text(),'%s')]" % day)))

        select_day.click()

        set_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[text()='Set'])[1]")))

        set_btn.click()

    @staticmethod
    def field_value(driver, field_name):
        field_value = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                     "//mat-sidenav//span[contains(text(),'%s')]//following-sibling::div//span[contains(@class,'ng-star-inserted')]" % field_name)))

        return field_value
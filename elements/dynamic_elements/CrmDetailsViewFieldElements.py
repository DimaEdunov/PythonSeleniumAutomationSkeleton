import time
from time import sleep
from enum import Enum
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class FieldName(Enum):
    # Leads details view - "Client Exist" field is exceptional, appears in CrmElements.py
    FIRST_NAME_FIELD = "First Name"
    LAST_NAME_FIELD = "Last Name"
    EMAIL_FIELD = "Email"
    PHONE_FIELD = "Phone"
    CITIZENSHIP_FIELD = "Citizenship"
    UI_LANGUAGE_FIELD = "UI Language"
    ADDRESS_FIELD = "Address"
    CODE_FIELD = "Code"
    CITY_FIELD = "City"
    COUNTRY_FIELD = "Country"
    ASSIGNED_TO_FIELD = "Assigned To"
    LANGUAGE_FIELD = "Language"
    TITLE_VALUE = "Title"
    STATUS_VALUE = "Status"
    CATEGORY_VALUE = "Category"
    CLIENT_ID = "CRM Id"
    CREATED_TIME = "Created Time"
    MOBILE = "Mobile"

    # Documents List View
    STATUS = "Status"

    # Help Desk details view
    TICKET_SOURCE_FIELD = "Ticket Source"

    # Clients details view
    CLIENT_SOURCE_FIELD = "Client Source"
    CLIENT_STATUS_FIELD = "Client Status"

class FieldNameConstants(Enum):
    # Inserted values
    TITLE_VALUE = "Test title"
    TICKET_SOURCE_VALUE = "Telephone Call"
    VALID_PHONE = "19053919620"
    INVALID_PHONE_A = "123123"
    INVALID_PHONE_B = "61298765432312"

    ASSIGNED_TO_CRM_USER = "Anastasiia v"
    FIRST_NAME_VALUE = "QAQA"
    ADDRESS_FIELD_VALUE = "HADAR CITY"


class FieldElements:

    @staticmethod
    def get_field_value(driver, field_name):
        sleep(3)

        if len(driver.find_elements(By.XPATH, "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-txt-wrapper')]" % field_name))>0:
            return driver.find_element(By.XPATH, "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-txt-wrapper')]" % field_name)

        elif len(driver.find_elements(By.XPATH, "//div[label='%s']//following-sibling::div//div[@class and text()]" % field_name)) > 0:
            return driver.find_element(By.XPATH, "//div[label='%s']//following-sibling::div//div[@class and text()]" % field_name)

        else:
            return driver.find_element(By.XPATH, "(//div[label='%s']//following-sibling::button//span)[1]" % field_name)

    @staticmethod
    def change_text_field_value_via_pencil(driver, field_name, value_name):
        # Click on the pencil icon
        time.sleep(2)

        print(len(driver.find_elements(By.XPATH, "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-pencil')]" % field_name)))
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-pencil')]" % field_name))).click()

        # Edit the text field
        text_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'label-wrap') and label='%s']//following-sibling::mat-form-field//input" % field_name)))

        text_field.click()
        text_field.clear()
        text_field.send_keys(value_name)

        time.sleep(2)
        # Click on the confirm button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[label='%s']//following-sibling::div//div[contains(@class,'button-confirm')]" % field_name))).click()


    @staticmethod
    def change_assigned_to_value(driver, field_name, value_name):
        # Click on the pencil icon
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-pencil')]" % field_name))).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                        "//input[@placeholder='Name']"))).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                        "//input[@placeholder='Name']"))).send_keys(value_name)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                              "//span[@title='%s']" % value_name))).click()

    @staticmethod
    def change_picklist_field_value_via_pencil(driver, field_name, value_name):
        # Click on the pencil icon
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-pencil')]" % field_name))).click()

        # Select value out of picklist
        picklist_value = driver.find_element(By.XPATH, "//div[label='%s']//following-sibling::div//span[contains("
                                                        "text(),'%s')]" % (field_name, value_name))

        driver.execute_script("arguments[0].click();", picklist_value)

        # Click on the confirm button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[label='%s']//following-sibling::div//div[contains(@class,'button-confirm')]" % field_name))).click()

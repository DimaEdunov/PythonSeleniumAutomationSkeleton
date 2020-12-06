from datetime import *
import time
from enum import Enum
from random import randint

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.elements.ApiElements import ApiElements
from src.elements.dynamic_elements import ApiResponseCode
from src.elements.dynamic_elements.ApiResponseCode import ApiAction, ApiResponse
from src.elements.dynamic_elements.ApiSideMenuElements import ApiSideMenuElements, ApiSideMenuItems
from src.infrastructure.dynamic_helpers.ScrollActions import ScrollActions
from src.infrastructure.dynamic_helpers.SwitchTo import SwitchTo
from src.elements.CrmElements import CrmElements


class ApiConstants(Enum):

    # [C] Customer & [C] Lead sections
    random_number_variable_a = datetime.now().strftime('%Y%m%d%H%M%S%f')
    random_number_variable_b = str(randint(0, 10000))
    PASSWORD = "Aa111111"

    COUNTRY_DE = "de"
    COUNTRY_LI = "li"

    COUNTRY_VALUE = "de"
    FIRST_NAME_VALUE_1 = "qa"
    LAST_NAME_VALUE_1 = "qa"

    FIRST_NAME_VALUE_2 = "dima"
    LAST_NAME_VALUE_2 = "edunov"

    FIRST_NAME_UPDATE_VALUE = "qaupdate"
    POSTAL_CODE_VALUE = "code879"
    PHONE_INVALID = "12345678"
    PHONE_VALID = "49619053919620"

    PHONE_DUPLICATE_VALUE = "8765432109"
    PHONE_UPDATE_VALUE = random_number_variable_b

    # [C] Customer section
    CUSTOMER_EMAIL_VALUE_OPTION_A = "pandaqa+" + random_number_variable_a + "0customer@pandats.com"
    CUSTOMER_EMAIL_VALUE_OPTION_B = "pandaqa+" + random_number_variable_b + "14customer@pandats.com"
    CUSTOMER_EMAIL_VALUE_OPTION_C = "pandaqa+" + random_number_variable_b + "12customer@pandats.com"
    CUSTOMER_EMAIL_VALUE_OPTION_D = "pandaqa+" + random_number_variable_b + "35customer@pandats.com"
    CUSTOMER_EMAIL_VALUE_OPTION_E = "pandaqa+" + random_number_variable_a + "41customer@pandats.com"
    CUSTOMER_EMAIL_VALUE_OPTION_F = "pandaqa+" + random_number_variable_b + "54customer@pandats.com"


    ENVIRONMENT_PREP_CUSTOMER_1 = "pandaqa+" + random_number_variable_a + "+qateam@test.com"
    ENVIRONMENT_PREP_CUSTOMER_2 = "pandaqa+" + random_number_variable_b + "+environmentPrep2@pandats.com"
    ENVIRONMENT_PREP_CUSTOMER_3 = "pandaqa+" + random_number_variable_b + "+environmentPrep3@pandats.com"

    # [C] Lead section
    LEAD_EMAIL_VALUE_1 = "pandaqa+" + random_number_variable_a + "1lead@pandats.com"
    LEAD_EMAIL_VALUE_2 = "pandaqa+" + random_number_variable_a + "2lead@pandats.com"
    LEAD_EMAIL_VALUE_3 = "pandaqa+" + random_number_variable_a + "2lead@pandats.com"
    LEAD_EMAIL_VALUE_4 = "pandaqa+" + random_number_variable_a + "2lead@pandats.com"

    ENVIRONMENT_PREP_LEAD_1 = "donottouch+automationLeadPencil@pandats.com"
    ENVIRONMENT_PREP_LEAD_2 = "automation+donttouch.qa@test.com"


class Api(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Api.go_to() | Navigating to Api module")
    def go_to(self):
        # Get 'CRM' screen ID of screen 'FIRST SCREEN'
        first_screen_identifier = self.driver.window_handles[0]

        # Clicking on 'API Link'
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.AFFILIATES_API_LINK)))

        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,CrmElements.AFFILIATES_API_LINK))

        # Get 'API's screen ID of screen 'SECOND SCREEN'
        second_screen_identifier = self.driver.window_handles[1]

        # Create object of SwitchTo
        switch_to_helper = SwitchTo(first_screen_identifier, second_screen_identifier, self.driver)

        # Switch to second screen ID -> 'API' screen
        switch_to_helper.switch_to("1")

        # Get second's screen URL -> 'API' screen
        second_screen_url = self.driver.current_url

        self.driver.close()

        # Switch back to 'FIRST SCREEN' - > CRM
        switch_to_helper.switch_to("0")

        # Open 'API' url in 'FIRST SCREEN'
        self.driver.get(second_screen_url)

    @allure.step("Api.authentication_process() | Going through authentication process")
    def authorization_process(self, partner_id_code):
        # Inserting 'secret-key' into relevant field

        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.API_SIDE_MENU_PARTNER_SECRET_KEY_FIELD))).click()

        time.sleep(3.5)
        self.driver.find_element(By.XPATH, ApiElements.API_SIDE_MENU_PARTNER_SECRET_KEY_FIELD).send_keys(
            Keys.CONTROL + 'v')


        ApiSideMenuElements.navigate_to(self.driver, ApiSideMenuItems.AUTHORIZATION_SECTION.value).click()

        # Scrolling to 'accessKey' field
        ScrollActions.scroll_to(self.driver.find_element(By.XPATH, ApiElements.API_AUTHORIZATION_PARTNER_ID_FIELD))

        # Inserting 'partner_id_code' into relevant field
        self.driver.find_element(By.XPATH, ApiElements.API_AUTHORIZATION_PARTNER_ID_FIELD).send_keys(partner_id_code)

        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.API_AUTHORIZATION_TIME_GENERATE_BUTTON))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.API_AUTHORIZATION_ACCESS_KEY_GENERATE_BUTTON))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.API_GENERIC_SEND_BUTTON))).click()


    @allure.step("Api.authorization_process_verification() | Verifying authentication")
    def authorization_process_verification(self):
            self.driver.execute_script("arguments[0].scrollIntoView();",
                                       self.driver.find_element(By.XPATH, ApiElements.API_AUTHORIZATION_RESPONSE))
            time.sleep(2)

            print("DEBUG | RESPONSE is " + self.driver.find_element(By.XPATH, ApiElements.API_AUTHORIZATION_RESPONSE).text)

            if "expire" in self.driver.find_element(By.XPATH, ApiElements.API_AUTHORIZATION_RESPONSE).text:
                # Api authorization verification was successful
                pass
            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="authorizationProcessverificationFailed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.step("Api.create_customer() | Creating a customer using api")
    def create_customer(self, email_value, password_value, country_value, first_name_value, last_name_value, phone_value):
        ApiSideMenuElements.navigate_to(self.driver, ApiSideMenuItems.C_CUSTOMER.value).click()

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH,
                                                                                              ApiElements.CUSTOMER_EMAIL_FIELD))

        # Insert email (Random)
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.CUSTOMER_EMAIL_FIELD)))



        print("API EMAIL DEBUG - " + email_value)
        time.sleep(2)
        email_field.clear()
        email_field.send_keys(email_value)


        # Insert values into mandatory fields
        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_PASSWORD_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_PASSWORD_FIELD).send_keys(password_value)

        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_COUNTRY_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_COUNTRY_FIELD).send_keys(country_value)

        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_FIRST_NAME_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_FIRST_NAME_FIELD).send_keys(first_name_value)

        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_LAST_NAME_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_LAST_NAME_FIELD).send_keys(last_name_value)

        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_PHONE_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_PHONE_FIELD).send_keys(phone_value)

        if len(self.driver.find_elements(By.XPATH, ApiElements.CREATE_CUSTOMER_TERMS_AND_CONDITIONS_FIELD)) > 0:
            self.driver.find_element(By.XPATH, ApiElements.CREATE_CUSTOMER_TERMS_AND_CONDITIONS_FIELD).clear()
            self.driver.find_element(By.XPATH, ApiElements.CREATE_CUSTOMER_TERMS_AND_CONDITIONS_FIELD).send_keys("1")

        # Submit (js)
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_CREATE_BUTTON))

        self.driver.find_element(By.XPATH, ApiElements.CUSTOMER_CREATE_BUTTON).click()

        time.sleep(5)

        return email_value

    @allure.step("Api.read_customer() | Read a customer using api")
    def read_customer(self, email_value):
        ApiSideMenuElements.navigate_to(self.driver, ApiSideMenuItems.R_CUSTOMER.value).click()

        self.driver.execute_script("scrollBy(0,+1000);")

        time.sleep(5)

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(
            By.XPATH, ApiElements.READ_CUSTOMER_EMAIL_FIELD))

        time.sleep(5)

        # Insert email (Random)
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.READ_CUSTOMER_EMAIL_FIELD)))

        email_field.clear()

        print("API EMAIL DEBUG - " + email_value)

        email_field.send_keys(email_value)

        self.driver.find_element(By.XPATH, ApiElements.READ_CUSTOMER_SEND_BUTTON).click()

    @allure.step("Api.read_customer_response_verification() | Read Customer response verification")
    def read_customer_response_verification(self, api_action, email_value, country_value, first_name_value,
                                            last_name_value):
        time.sleep(3)
        response = ApiResponse.api_response_code(self.driver, api_action)

        assert email_value in response
        assert country_value in response
        assert first_name_value in response
        assert last_name_value in response

    @allure.step("Api.read_customers() | Read Customers using api")
    def read_customers(self):
        ApiSideMenuElements.navigate_to(self.driver, ApiSideMenuItems.R_CUSTOMERS.value).click()

        time.sleep(1)

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(
            By.XPATH, ApiElements.READ_CUSTOMERS_PAGE_FIELD))

        time.sleep(1)

        # Insert page
        page_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.READ_CUSTOMERS_PAGE_FIELD)))

        page_field.clear()

        page_field.send_keys('1')

        # Insert limit
        limit_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.READ_CUSTOMERS_LIMIT_FIELD)))

        limit_field.clear()

        limit_field.send_keys('5')

        # Click Send button
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(
            By.XPATH, ApiElements.READ_CUSTOMERS_SEND_BUTTON))
        self.driver.find_element(By.XPATH, ApiElements.READ_CUSTOMERS_SEND_BUTTON).click()

    @allure.step("Api.create_customer() | Read customers response verification")
    def read_customers_response_verification(self, api_action):
        time.sleep(3)
        response = ApiResponse.api_response_code(self.driver, api_action)

        if "crmId" in response:
            pass
        else:
            assert False


    @allure.step("Api.update_customer() | Update a customer using api")
    def update_customer(self, email_value, first_name_value, postal_code_value, phone_value):
        time.sleep(3)
        ApiSideMenuElements.navigate_to(self.driver, ApiSideMenuItems.U_COSTUMER.value).click()

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(
            By.XPATH, ApiElements.UPDATE_CUSTOMER_EMAIL_FIELD))

        time.sleep(3)

        # Insert email
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.UPDATE_CUSTOMER_EMAIL_FIELD)))

        email_field.clear()

        email_field.send_keys(email_value)

        # Insert first name
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.UPDATE_CUSTOMER_FIRST_NAME_FIELD)))

        first_name_field.clear()

        first_name_field.send_keys(first_name_value)

        # Insert postal code
        postal_code_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.UPDATE_CUSTOMER_POSTAL_CODE_FIELD)))

        postal_code_field.clear()

        postal_code_field.send_keys(postal_code_value)

        # Insert phone
        phone_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.UPDATE_CUSTOMER_PHONE_FIELD)))

        phone_field.clear()

        phone_field.send_keys(phone_value)

        # Click Send button
        self.driver.find_element(By.XPATH, ApiElements.UPDATE_CUSTOMER_SEND_BUTTON).click()

    @allure.step("Api.create_customer() | Creating a lead using api")
    def create_lead(self,country_value , email_value, first_name_value, last_name_value, phone_value):
        time.sleep(2)
        # Navigate to [C] Leads element
        ApiSideMenuElements.navigate_to(self.driver, ApiSideMenuItems.C_LEADS.value).click()

        # Scroll to 'Referral field' in [C] Leads section
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(By.XPATH, ApiElements.LEAD_REFERRAL_FIELD))

        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.LEAD_EMAIL_FIELD)))

        email_field.clear()

        # Insert values into mandatory fields
        self.driver.find_element(By.XPATH, ApiElements.LEAD_COUNTRY_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.LEAD_COUNTRY_FIELD).send_keys(country_value)

        self.driver.find_element(By.XPATH, ApiElements.LEAD_EMAIL_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.LEAD_EMAIL_FIELD).send_keys(email_value)

        self.driver.find_element(By.XPATH, ApiElements.LEAD_FIRST_NAME_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.LEAD_FIRST_NAME_FIELD).send_keys(first_name_value)

        self.driver.find_element(By.XPATH, ApiElements.LEAD_LAST_NAME_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.LEAD_LAST_NAME_FIELD).send_keys(last_name_value)

        self.driver.find_element(By.XPATH, ApiElements.LEAD_PHONE_FIELD).clear()
        self.driver.find_element(By.XPATH, ApiElements.LEAD_PHONE_FIELD).send_keys(phone_value)

        # Submit (js)
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(By.XPATH, ApiElements.LEAD_CREATE_BUTTON))

        self.driver.find_element(By.XPATH, ApiElements.LEAD_CREATE_BUTTON).click()

        time.sleep(5)

        return email_value

    @allure.step("Api.response_code_verification() | Verifying response code")
    def response_code_verification(self, api_action):
        # Verifying customer creation, use dynamic element to get resposne
        time.sleep(6)
        response = ApiResponse.api_response_code(self.driver, api_action)

        if "ok" in response:
            pass
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Api.response_code_verification",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("Api.response_code_verification() | Verifying response code")
    def duplicate_customer_response_verification(self, api_action):
        # Verifying customer creation, use dynamic element to get resposne
        time.sleep(3)
        response = ApiResponse.api_response_code(self.driver, api_action)

        assert "Customer already exists" in response

    @allure.step("Api.read_customers() | Read Customers using api")
    def read_leads(self):
        ApiSideMenuElements.navigate_to(self.driver, ApiSideMenuItems.R_LEADS.value).click()

        time.sleep(2)
        
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(
            By.XPATH, ApiElements.READ_LEADS_PAGE_FIELD))

        # Insert page
        page_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.READ_LEADS_PAGE_FIELD)))

        page_field.clear()

        page_field.send_keys('1')

        # Insert limit
        limit_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ApiElements.READ_LEADS_LIMIT_FIELD)))

        limit_field.clear()

        limit_field.send_keys('5')

        # Click Send button
        self.driver.find_element(By.XPATH, ApiElements.READ_LEADS_SEND_BUTTON).click()

    @allure.step("Api.create_customer() | Creating a customer using api")
    def read_leads_response_verification(self, api_action):
        time.sleep(5)
        response = ApiResponse.api_response_code(self.driver, api_action)

        if "id" in response:
            pass

        else:
            assert False

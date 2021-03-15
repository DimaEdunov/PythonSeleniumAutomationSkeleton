import time
from enum import Enum
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import allure

from src.elements.CaElements import CaElements
from src.elements.dynamic_elements.CA.CaDynamicElements import CaDynamicElementsActions, CaDynamicElementsConstants


class ClientAreaPluginConstants(Enum):
    # Sign Up Elements
    random_number_variable = str(randint(0, 10000))
    FIRST_NAME = "Yarin"
    LAST_NAME = "AUTO"
    EMAIL = "pandaqa+" + random_number_variable + "CA@pandats.com"
    VALID_PHONE = "49508773429"
    INVALID_PHONE = "123"
    PASSWORD = "123456789a"

class ClientAreaPlugin(object):

    def __init__(self, driver, ca_url):
        self.driver=driver
        self.ca_url=ca_url

    @allure.step("ClientAreaPlugin.go_to() | Navigate to Home Page of the brand")
    def go_to(self):
        self.driver.get(self.ca_url)
        time.sleep(8)

    @allure.step("ClientAreaPlugin.sign_up_new_client() | Sign up a new client to the platform")
    def sign_up_new_client(self,firstname,lastname,email,phone,password):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CaElements.HEADER_SIGN_UP_BUTTON))).click()

        time.sleep(3)

        CaDynamicElementsActions.ca_input(self.driver, CaDynamicElementsConstants.FIRST_NAME_INPUT.value).send_keys(firstname)
        CaDynamicElementsActions.ca_input(self.driver, CaDynamicElementsConstants.LAST_NAME_INPUT.value).send_keys(lastname)
        CaDynamicElementsActions.ca_input(self.driver, CaDynamicElementsConstants.SIGN_UP_EMAIL_INPUT.value).send_keys(email)
        CaDynamicElementsActions.ca_input(self.driver, CaDynamicElementsConstants.PHONE_INPUT.value).send_keys(phone)
        CaDynamicElementsActions.ca_input(self.driver, CaDynamicElementsConstants.SIGN_UP_PASSWORD_INPUT.value).send_keys(password)
        CaDynamicElementsActions.ca_input(self.driver, CaDynamicElementsConstants.SIGN_UP_CONFIRM_PASSWORD_INPUT.value).send_keys(password)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CaElements.TERMS_AND_CONDITIONS_CHECKBOX))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CaElements.SUBMIT_BUTTON))).click()


    @allure.step("ClientAreaPlugin.log_in_client() | Log in to the platform")
    def log_in_client(self, email, password):
        if len(self.driver.find_elements(By.XPATH, CaElements.HEADER_CLIENT_AREA_DROPDOWN)) > 0:
            self.log_out_client()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CaElements.HEADER_LOGIN_BUTTON))).click()

        CaDynamicElementsActions.ca_input(self.driver, CaDynamicElementsConstants.LOGIN_EMAIL_INPUT.value).send_keys(email)
        CaDynamicElementsActions.ca_input(self.driver, CaDynamicElementsConstants.LOGIN_PASSWORD_INPUT.value).send_keys(password)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CaElements.LOGIN_BUTTON))).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CaElements.HEADER_CLIENT_AREA_DROPDOWN)))

    @allure.step("ClientAreaPlugin.log_in_verification() | Verify log in of a client")
    def log_in_verification(self):
        time.sleep(3)
        if len(self.driver.find_elements(By.XPATH, CaElements.HEADER_CLIENT_AREA_DROPDOWN)) > 0:
            pass
        else:
            assert False

    @allure.step("ClientAreaPlugin.log_out_client() | Log out a client")
    def log_out_client(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CaElements.HEADER_CLIENT_AREA_DROPDOWN))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CaElements.SIGN_OUT_CLIENT_BUTTON))).click()
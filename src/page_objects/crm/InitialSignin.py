import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.elements.CrmElements import CrmElements
from selenium.common.exceptions import NoSuchElementException

from src.elements.dynamic_elements.CrmSideMenuElements import CrmSideMenu, Modules


class InitialSignin(object):
    # Todo: Add try, exception around all methods with TimeOut and ElementNotFound
    def __init__(self, driver, crm_url):
        self.crm_url = crm_url
        self.driver = driver

    @allure.step("InitialSignin.go_to() | Navigate to CRM")
    def go_to(self):
        self.driver.get(self.crm_url)
        time.sleep(8)

        # If go_to() is not used in the main_screen (Sign-In), then wait for a side menu element to appear
        if len(self.driver.find_elements(By.XPATH, CrmElements.OLD_SIGN_IN_USER_NAME_FIELD))==0 and\
                len(self.driver.find_elements(By.XPATH, CrmElements.NEW_SIGN_IN_PASSWORD_FIELD))==0 :

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_WAIT_VERIFICATION_ELEMENT)))


    @allure.step("InitialSignin.sign_in() | Sign into crm")
    def sign_in(self, crm_version, user, password):

        time.sleep(7)
        # IF for OLD Sign-In screen
        if len(self.driver.find_elements(By.XPATH, CrmElements.OLD_SIGN_IN_PASSWORD_FIELD))>0:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CrmElements.OLD_SIGN_IN_USER_NAME_FIELD))).send_keys(user)

            self.driver.find_element(By.XPATH, CrmElements.OLD_SIGN_IN_PASSWORD_FIELD).send_keys(password)

            checkbox = self.driver.find_element(By.XPATH, CrmElements.NEW_UI_OLD_SIGN_IN_CHECKBOX)

            is_selected = checkbox.is_selected()

            print("Log : '%s' forex was chosen" % crm_version)

            if crm_version == "new" and is_selected == False:
                self.driver.execute_script("arguments[0].click();", checkbox)

            elif crm_version == "old" and is_selected == True:
                self.driver.execute_script("arguments[0].click();", checkbox)

            self.driver.find_element(By.XPATH, CrmElements.OLD_SIGN_IN_SUBMIT_BUTTON).click()
            time.sleep(15)

        else:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, CrmElements.NEW_SIGN_IN_USER_NAME_FIELD))).send_keys(user)

            self.driver.find_element(By.XPATH, CrmElements.NEW_SIGN_IN_PASSWORD_FIELD).send_keys(password)

            self.driver.find_element(By.XPATH, CrmElements.NEW_SIGN_IN_SUBMIT_BUTTON).click()
            time.sleep(15)

    @allure.step("InitialSignin.sign_in_verification() | Sign-in Verification")
    def sign_in_verification(self):
        if len(self.driver.find_elements(By.XPATH, CrmElements.OLD_SIGN_IN_USER_NAME_FIELD))>0:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="SignInVerificationfailed",
                          attachment_type=AttachmentType.PNG)
            assert False
        else:
            pass

    @allure.step("InitialSignin.sign_out() | Sign-out")
    def sign_out(self):
        print("DEBUG -> Signing out")

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.SIDE_MENU_USER_NAME_ITEM))).click()

        time.sleep(5)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.SIDE_MENU_SIGN_OUT))).click()

        time.sleep(5)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.SIDE_MENU_SIGN_OUT_YES_BUTTON))).click()



        time.sleep(1)
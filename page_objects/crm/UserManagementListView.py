import time
from enum import Enum
from time import sleep
from selenium.webdriver.common.keys import Keys
import allure
import random
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmSideMenuElements import CrmSideMenu, Modules


class UserManagementConstants(Enum):
    # Create user right slider
    random_number = str(random.randrange(1, 999999))
    USER_NAME = "pandatest" + random_number
    EMAIL = "pandaqa+%s@pandats.com" % random_number
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"

    NAME = "first_name last_name"
    PANDA_USER = "Panda Auto"
    PASSWORD = "Test12345"


class UserManagementListView(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("UserManagementListView.go_to() | Navigating to User Management module")
    @allure.severity(allure.severity_level.NORMAL)
    def go_to(self):
        try:

            time.sleep(2.5)

            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_SETTINGS))).click()

            # Navigating to user management module screen
            user_management_module = CrmSideMenu.side_menu_items(self.driver, Modules.USER_MANAGEMENT_MODULE_.value)
            self.driver.execute_script("arguments[0].click();", user_management_module)

            time.sleep(10)

            WebDriverWait(self.driver, 25).until(
                EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

            self.driver.switch_to_frame(self.driver.find_element(By.XPATH,
                                                                 CrmElements.USER_MANAGEMENT_IFRAME))
            sleep(0.1)
            WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.USER_MANAGEMENT_CRM_USERS_TAB))).click()

        except:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="UserManagementListView.go_to",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("UserManagementListView.searching_by_username() | Searching by username")
    @allure.severity(allure.severity_level.NORMAL)
    def searching_by_username(self):
        sleep(5)
        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_SPINNER)))

        username_field = WebDriverWait(self.driver, 45).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.USER_MANAGEMENT_USER_NAME_SEARCH_FIELD)))

        username_field.send_keys(UserManagementConstants.USER_NAME.value, Keys.ENTER)

        sleep(1)

        WebDriverWait(self.driver, 55).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_SPINNER)))

    @allure.step("UserManagementListView.create_user() | Create User")
    @allure.severity(allure.severity_level.NORMAL)
    def create_user(self):
        sleep(2)

        # click New User button
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.USER_MANAGEMENT_NEW_USER_BUTTON))).click()

        # ser User name
        user_name_field = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.USER_MANAGEMENT_USER_NAME_FIELD)))
        user_name_field.send_keys(UserManagementConstants.USER_NAME.value)

        # set email
        email_field = self.driver.find_element(By.XPATH, CrmElements.USER_MANAGEMENT_EMAIL_FIELD)
        email_field.send_keys(UserManagementConstants.EMAIL.value)

        # set first name
        first_name_field = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.USER_MANAGEMENT_FIRST_NAME_FIELD)))
        first_name_field.clear()
        first_name_field.send_keys(UserManagementConstants.FIRST_NAME.value)

        sleep(2)

        # set role
        self.driver.find_element(By.XPATH, CrmElements.USER_MANAGEMENT_ROLE_FIELD).click()

        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_SPINNER)))

        handle = self.driver.window_handles[1]
        self.driver.switch_to.window(handle)

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.USER_MANAGEMENT_ROLE_VALUE))).click()
        handle = self.driver.window_handles[0]
        self.driver.switch_to.window(handle)

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, CrmElements.USER_MANAGEMENT_IFRAME))


        # set password
        sleep(0.1)
        password_field = self.driver.find_element(By.XPATH, CrmElements.USER_MANAGEMENT_PASSWORD_FIELD)
        password_field.send_keys(UserManagementConstants.PASSWORD.value)

        sleep(2)

        # confirm password
        confirm_password_field = self.driver.find_element(By.XPATH, CrmElements.USER_MANAGEMENT_CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(UserManagementConstants.PASSWORD.value)

        # set last name
        last_name_field = self.driver.find_element(By.XPATH, CrmElements.USER_MANAGEMENT_LAST_NAME_FIELD)
        last_name_field.send_keys(UserManagementConstants.LAST_NAME.value)

        time.sleep(5)

        otp_checkbox = self.driver.find_element(By.XPATH,  CrmElements.USER_MANAGEMENT_DISABLE_OTP_CHECKBOX)
        self.driver.execute_script("arguments[0].click();", otp_checkbox)

        # click save button
        sleep(1)
        save_button = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.USER_MANAGEMENT_SAVE_BUTTON)))
        self.driver.execute_script("arguments[0].click();", save_button)
        sleep(0.5)
        WebDriverWait(self.driver, 45).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

    @allure.step("UserManagementListView.create_user_verification() | Create User Verification")
    @allure.severity(allure.severity_level.NORMAL)
    def create_user_verification(self):
        try:
            time.sleep(5)
            self.driver.find_element(By.XPATH,
                                     CrmElements.USER_MANAGEMENT_USER_FOUND
                                     % UserManagementConstants.USER_NAME.value)

        except:
            assert False

    @allure.step("UserManagementListView.login_as() | Login as")
    @allure.severity(allure.severity_level.NORMAL)
    def login_as(self):
        sleep(3)

        more_button = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_MORE_BUTTON)))
        self.driver.execute_script("arguments[0].scrollIntoView();", more_button)
        self.driver.execute_script("arguments[0].click();", more_button)

        sleep(0.5)
        # click login as button
        login_as_icon = self.driver.find_element(By.XPATH, CrmElements.USER_MANAGEMENT_LOGIN_AS_BUTTON)
        self.driver.execute_script("arguments[0].click();", login_as_icon)

        sleep(1)

        WebDriverWait(self.driver, 35).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))
        self.driver.switch_to_default_content()

    @allure.step("UserManagementListView.login_as_verification() | Login as verification")
    @allure.severity(allure.severity_level.NORMAL)
    def login_as_verification(self):
        # username verification (login as mode)
        name = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_LOGIN_NAME_VALUE))).text

        assert name == UserManagementConstants.NAME.value

        # sign out from login as mode
        sleep(0.1)
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_SIGN_OUT_BUTTON))).click()

        sleep(0.5)

        WebDriverWait(self.driver, 35).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))

        # username verification
        name = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_LOGIN_NAME_VALUE))).text

        print("\nConstant vlaue is : "+UserManagementConstants.PANDA_USER.value)
        print("Element value is : " +name)

        assert name == UserManagementConstants.PANDA_USER.value

    @allure.step("UserManagementListView.delete_user() | Delete user")
    @allure.severity(allure.severity_level.NORMAL)
    def delete_user(self):
        sleep(3)

        more_button = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_MORE_BUTTON)))

        print(str(len(self.driver.find_elements(By.XPATH,CrmElements.USER_MANAGEMENT_MORE_BUTTON ))))
        self.driver.execute_script("arguments[0].scrollIntoView();", more_button)

        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", more_button)
        sleep(1)

        # click delete icon
        delete_icon = self.driver.find_element(By.XPATH, CrmElements.USER_MANAGEMENT_DELETE_ICON)
        self.driver.execute_script("arguments[0].click();", delete_icon)

        sleep(1)
        # click delete button
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.USER_MANAGEMENT_DELETE_BUTTON))).click()

        sleep(2)
        # Verify message about user deleting
        WebDriverWait(self.driver, 175).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_DELETE_MESSAGE)))

    @allure.step("UserManagementListView.delete_user_verification() | Delete user verification")
    @allure.severity(allure.severity_level.NORMAL)
    def delete_user_verification(self):
        sleep(2)
        WebDriverWait(self.driver, 25).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_SPINNER)))

        WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, CrmElements.USER_MANAGEMENT_NO_DATA_MESSAGE)))

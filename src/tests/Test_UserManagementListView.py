import os
import subprocess
import time
from time import sleep

import allure
import pytest
from allure_commons.types import AttachmentType
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.UserManagementListView import UserManagementListView, UserManagementConstants
from src.tests.conftest import get_brand_url



@pytest.mark.usefixtures("driver", "brand")
class Test_UserManagementListView:

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('User Management List View')
    @allure.story('Create User')
    @pytest.mark.run(order=1)
    def test_create_user(self, driver, brand):
        try:

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 9 : Go to crm main screen
            crm_main_screen.go_to()

            # Step 1: Go to User Management module
            user_management_module = UserManagementListView(driver)
            user_management_module.go_to()

            # Step 2: Create user
            user_management_module.create_user()

            # Step 3: User verification
            user_management_module.searching_by_username()
            user_management_module.create_user_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_user",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('User Management List View')
    @allure.story('Login As')
    @pytest.mark.run(order=2)
    def test_login_as(self, driver, brand):
        try:
            # Step 1: Perform Login as
            user_management_module = UserManagementListView(driver)
            user_management_module.login_as()

            # Step 2: Login as verification
            user_management_module.login_as_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_login_as",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('User Management List View')
    @allure.story('Delete User')
    # This decorator gives an order of a test
    @pytest.mark.run(order=3)
    def test_delete_user(self, driver, brand):
        try:
            # Step 1: Go to User Management module
            user_management_module = UserManagementListView(driver)
            user_management_module.go_to()

            # Step 2: Searching of user by username
            user_management_module.searching_by_username()

            # Step 3: Delete user
            user_management_module.delete_user()

            # Step 4: Delete user verification
            user_management_module.delete_user_verification()


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_delete_user",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False
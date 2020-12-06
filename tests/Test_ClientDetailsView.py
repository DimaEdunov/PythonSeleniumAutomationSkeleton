import os
import subprocess
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldName, FieldNameConstants
from src.elements.dynamic_elements.CrmDetailsViewSectionElements import Section
from src.elements.dynamic_elements.ApiResponseCode import ApiAction
from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar

from src.page_objects.api.Api import Api, ApiConstants
from src.page_objects.crm.AffiliatesListView import AffiliatesListView
from src.page_objects.crm.ClientsDetailsView import ClientDetailsView
from src.page_objects.crm.ClientsListView import ClientsListView
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView
from src.page_objects.crm.CrossModuleListView import CrossModuleListView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_ClientDetailsView():


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Create MT4 User')
    @pytest.mark.run(order=1)
    def test_create_mt_account(self, driver, brand):

        try:
            """
            This part will create a client using api, then we will perform actions on that account (MT actions)
            """
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            # Create affiliates object
            affiliates = AffiliatesListView(driver)

            # Step 2: Go to Affiliates module
            affiliates.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 3: Search for 'dev' via affiliates searchbar
            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "PandaDev")

            # Step 4: Get secret key
            secret_key = affiliates.get_secret_key()

            api = Api(driver)

            # Step 5: Go to api
            api.go_to()

            # Step 6: Apply authentication proccess using 'secret key'
            api.authorization_process(secret_key)

            # Step 7: Verify authentication process
            api.authorization_process_verification()

            api = Api(driver)

            # Step 8 : Create customer via api
            api.create_customer(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_E.value,
                                ApiConstants.PASSWORD.value,
                                ApiConstants.COUNTRY_VALUE.value,
                                ApiConstants.FIRST_NAME_VALUE_1.value,
                                ApiConstants.LAST_NAME_VALUE_1.value,
                                ApiConstants.PHONE_INVALID.value)

            # Step 9 : Create customer verification
            api.response_code_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)

            # Step 10 : Go to crm main screen
            crm_main_screen.go_to()

            clients_module = ClientsListView(driver)

            # Step 11 : Go to Clients module
            clients_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 12 : Select Test Clients[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 13 : Search for the created client via 'Email'
            client_details_view = ClientDetailsView(driver)

            details_view_cross_module = CrossModuleDetailsView(driver)

            # Step 14 : Navigate to client details view via search bar
            details_view_cross_module.go_to_via_searchbar_using_email(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_E.value,
                                                                      "clients")
            """
            Creation of client until this point
            """

            time.sleep(20)

            client_details_view.open_trading_account_menu()

            # Step 15: Create MT account
            client_details_view.create_trading_account("live")

            # Step 17: Verify MT account
            client_details_view.create_trading_account_verification("live")




        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_mt_user",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Change field via pencil')
    @pytest.mark.run(order=2)
    def test_clients_change_info_via_pencil(self, driver, brand):
        try:

            cross_module_details_view = CrossModuleDetailsView(driver)

            cross_module_details_view.open_section(Section.ADDRESS_INFORMATION.value)

            cross_module_details_view.edit_field_via_pencil(FieldName.CITY_FIELD,
                                                            FieldNameConstants.ADDRESS_FIELD_VALUE)

            cross_module_details_view.edit_field_via_pencil_verification(FieldName.CITY_FIELD,
                                                                         FieldNameConstants.ADDRESS_FIELD_VALUE)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_change_field_value",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Deposit')
    @pytest.mark.run(order=3)
    def test_deposit(self, driver, brand):

        try:
            client_details_view = ClientDetailsView(driver)

            client_details_view.open_trading_account_menu()

            client_details_view.make_a_deposit("0.75")

            try:
                client_details_view.make_a_deposit_verification()
            except:
                client_details_view.make_a_deposit_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_deposit",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Withdraw')
    @pytest.mark.run(order=4)
    def test_withdraw(self, driver):
        try:
            # Instanse of ClientsDetailsView object
            client_details_view = ClientDetailsView(driver)

            client_details_view.open_trading_account_menu()

            # Step 1 : Withdraw of of 0.25
            client_details_view.make_a_withdraw("0.25")

            try:
                # Step 2: Withdraw verification
                client_details_view.make_a_withdraw_verification()

            except:
                # Retry once there is a delay in data replication
                client_details_view.make_a_withdraw_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_withdraw",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Credit in')
    @pytest.mark.run(order=5)
    def test_credit_in(self, driver):
        try:
            client_details_view = ClientDetailsView(driver)

            client_details_view.open_trading_account_menu()

            client_details_view.make_a_credit_in("0.55")

            client_details_view.make_a_credit_in_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_credit_in",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Credit out')
    @pytest.mark.run(order=6)
    def test_credit_out(self, driver):
        try:
            client_details_view = ClientDetailsView(driver)

            client_details_view.open_trading_account_menu()

            client_details_view.make_a_credit_out("0.31")

            client_details_view.make_a_credit_out_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_credit_out",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Transfer Between TA')
    @pytest.mark.run(order=7)
    def test_transfer_between_ta(self, driver, brand):
        try:

            client_details_view = ClientDetailsView(driver)

            client_details_view.open_trading_account_menu()

            client_details_view.create_trading_account("live")

            client_details_view.create_trading_account_verification("live")

            client_details_view.open_trading_account_menu()

            client_details_view.transfer_between_ta("0.1")

            client_details_view.transfer_between_ta_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_withdraw",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Change CRM password')
    @pytest.mark.run(order=8)
    def test_change_crm_password(self, driver, brand):
        try:

            client_details_view = ClientDetailsView(driver)

            client_details_view.change_crm_password()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_change_crm_password",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Check CRM password')
    @pytest.mark.run(order=9)
    def test_check_crm_password(self, driver, brand):
        try:

            client_details_view = ClientDetailsView(driver)

            client_details_view.check_crm_password()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_check_crm_password",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Add Interaction')
    @pytest.mark.run(order=10)
    def test_add_interaction(self, driver, brand):

        try:

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            crm_main_screen.go_to()

            clients_module = ClientsListView(driver)

            clients_module.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            client_details_view = ClientDetailsView(driver)

            details_view_cross_module = CrossModuleDetailsView(driver)
            details_view_cross_module.go_to_via_searchbar_using_email(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_E.value,
                                                                      "clients")

            cross_module_details_view = CrossModuleDetailsView(driver)

            cross_module_details_view.add_event(CrossModuleDetailsView.subject_input1)
            client_details_view.client_details_view_add_interaction_verification(CrossModuleDetailsView.subject_input1)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test make an interaction",
                          attachment_type=AttachmentType.PNG)

            self.driver.refresh()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Client details View')
    @allure.story('Update MT4 User')
    @pytest.mark.run(order=11)
    def test_update_mt4_user(self, driver, brand):
        try:

            client_details_view = ClientDetailsView(driver)

            client_details_view.open_trading_account_menu()

            client_details_view.create_trading_account("demo")

            client_details_view.open_trading_account_menu()

            right_slider_leverage_value = client_details_view.update_mt4_user()

            client_details_view.update_mt4_user_verification(right_slider_leverage_value)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_update_mt4_user",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False
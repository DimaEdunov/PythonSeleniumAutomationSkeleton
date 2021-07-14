import os
import subprocess
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.ApiResponseCode import ApiAction
from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar

from src.page_objects.api.Api import Api, ApiConstants
from src.page_objects.crm.AffiliatesListView import AffiliatesListView
from src.page_objects.crm.ClientsDetailsView import ClientDetailsView
from src.page_objects.crm.ClientsListView import ClientsListView
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.CrossModuleListView import CrossModuleListView
from src.page_objects.crm.LeadsDetailsView import LeadsDetailsView
from src.page_objects.crm.LeadsListView import LeadsListView
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_Api:
    
    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Api')
    @allure.story('Authorization Process')
    @pytest.mark.run(order=1)
    def test_authorization_process(self, driver, brand):
        try:

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

        except:
            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            allure.attach(driver.get_screenshot_as_png(),
                          name="test_authorization_process",
                          attachment_type=AttachmentType.PNG)

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Api')
    @allure.story('Create Customer')
    @pytest.mark.run(order=2)
    def test_create_customer(self, driver, brand):
        try:
            # Api object instance
            api = Api(driver)

            # Step 1: Create customer via api
            created_user_email = api.create_customer(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_A.value,
                                ApiConstants.PASSWORD.value,
                                ApiConstants.COUNTRY_VALUE.value,
                                ApiConstants.FIRST_NAME_VALUE_1.value,
                                ApiConstants.LAST_NAME_VALUE_1.value,
                                ApiConstants.PHONE_INVALID.value)

            # Step 2: Create customer verification
            api.response_code_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 3: Go to crm main screen
            crm_main_screen.go_to()

            clients_module = ClientsListView(driver)

            # Step 4: Go to Clients module
            clients_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 5: Select Test Clients[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 6: Search for the created client via 'Email'
            client_details_view = ClientDetailsView(driver)

            details_view_cross_module = CrossModuleDetailsView(driver)

            # Step 7: Navigate to client details view via search bar
            details_view_cross_module.go_to_via_searchbar_using_email(
                created_user_email, "clients")

            # Step 8: Verify create client via api
            client_details_view.create_client_verification(
                created_user_email,
                ApiConstants.FIRST_NAME_VALUE_1.value,
                ApiConstants.LAST_NAME_VALUE_1.value)

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_customer",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Api')
    @allure.story('Read Customer')
    @pytest.mark.run(order=3)
    def test_read_customer(self, driver, brand):
        try:
            # Create affiliates object
            affiliates = AffiliatesListView(driver)

            # Step 1: Go to Affiliates module
            affiliates.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Search for 'dev' via affiliates searchbar
            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "PandaDev")

            # Step 3: Get secret key
            secret_key = affiliates.get_secret_key()

            api = Api(driver)

            # Step 4: Go to api
            api.go_to()

            # Step 5: Apply authentication proccess using 'secret key'
            api.authorization_process(secret_key)

            # Step 6: Verify authentication process
            api.authorization_process_verification()

            # Api object instance
            api = Api(driver)

            # Step 7: Read customer via api
            api.read_customer(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_A.value)

            # Step 8: Read customer response verification
            api.read_customer_response_verification(
                ApiAction.READ_CUSTOMER_RESPONSE.value,
                ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_A.value,
                ApiConstants.COUNTRY_VALUE.value,
                ApiConstants.FIRST_NAME_VALUE_1.value,
                ApiConstants.LAST_NAME_VALUE_1.value)

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_read_customer",
                          attachment_type=AttachmentType.PNG)
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Api')
    @allure.story('Duplicate Customer')
    @pytest.mark.run(order=4)
    def test_duplicate_customer(self, driver, brand):
        try:
            # Api object instance
            api = Api(driver)

            # Step 1: Duplicate customer via api
            created_user_email =api.create_customer(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_A.value,
                                ApiConstants.PASSWORD.value,
                                ApiConstants.COUNTRY_VALUE.value,
                                ApiConstants.FIRST_NAME_VALUE_1.value,
                                ApiConstants.LAST_NAME_VALUE_1.value,
                                ApiConstants.PHONE_DUPLICATE_VALUE.value)

            # Step 2: Duplicate customer verification
            api.duplicate_customer_response_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_duplicate_customer",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Api')
    @allure.story('Read Customers')
    @pytest.mark.run(order=5)
    def test_read_customers(self, driver, brand):
        try:
            # Api object instance
            driver.refresh()
            time.sleep(8)
            api = Api(driver)

            # Step 1: Read Customers via api
            api.read_customers()

            # Step 2: Read Customers verification
            api.read_customers_response_verification(ApiAction.READ_CUSTOMERS_RESPONSE.value)

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_read_customers",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Api')
    @allure.story('Update Customer')
    @pytest.mark.run(order=6)
    def test_update_customer(self, driver, brand):
        try:
            # Api object instance
            driver.refresh()
            time.sleep(7)
            api = Api(driver)

            # Step 1: Update customer via api
            api.update_customer(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_A.value,
                                ApiConstants.FIRST_NAME_UPDATE_VALUE.value,
                                ApiConstants.POSTAL_CODE_VALUE.value,
                                ApiConstants.PHONE_UPDATE_VALUE.value)

            # Step 2: Update customer verification
            api.response_code_verification(ApiAction.UPDATE_CUSTOMER_RESPONSE.value)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 3: Go to crm main screen
            crm_main_screen.go_to()

            clients_module = ClientsListView(driver)

            # Step 4: Go to Clients module
            clients_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 5: Select Test Clients[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 6: Search for the created client via 'Email'
            client_details_view = ClientDetailsView(driver)

            details_view_cross_module = CrossModuleDetailsView(driver)

            # Step 7: Navigate to client details view via search bar
            details_view_cross_module.go_to_via_searchbar_using_email(
                ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_A.value, "clients")

            # Step 8: Verify update client via api
            client_details_view.api_update_client_verification(
                ApiConstants.FIRST_NAME_UPDATE_VALUE.value,
                ApiConstants.POSTAL_CODE_VALUE.value,
                ApiConstants.PHONE_UPDATE_VALUE.value)

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_update_customer",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Api')
    @allure.story('Create Lead')
    @pytest.mark.run(order=7)
    def test_create_lead(self, driver,brand):
        try:

            # Create affiliates object
            affiliates = AffiliatesListView(driver)

            # Step 1: Go to Affiliates module
            affiliates.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Search for 'dev' via affiliates searchbar
            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "PandaDev")

            # Step 3: Get secret key
            secret_key = affiliates.get_secret_key()

            api = Api(driver)

            # Step 4: Go to api
            api.go_to()

            # Step 5: Apply authentication proccess using 'secret key'
            api.authorization_process(secret_key)

            # Step 6: Verify authentication process
            api.authorization_process_verification()

            # Step 7: Create lead
            lead_email_value = api.create_lead(
                ApiConstants.COUNTRY_DE.value,
                ApiConstants.LEAD_EMAIL_VALUE_1.value,
                ApiConstants.FIRST_NAME_VALUE_1.value,
                ApiConstants.LAST_NAME_VALUE_1.value,
                ApiConstants.PHONE_INVALID.value)


            # Step 8 : Create customer verification
            api.response_code_verification(ApiAction.CREATE_LEAD_RESPONSE.value)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 9 : Go to crm main screen
            crm_main_screen.go_to()

            # Step 10: Go to leads details view
            leads_module = LeadsListView(driver)

            # step 11: go to leads module
            leads_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 12 : Select Test Clients[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Create object of Cross-module details view
            details_view_cross_module = CrossModuleDetailsView(driver)

            # Step 13 : Navigate to lead details view of created lead
            details_view_cross_module.go_to_via_searchbar_using_email(lead_email_value, "leads")

            # Create object of leads details view
            leads_details_view = LeadsDetailsView(driver)

            # Step 14 : Verify create lead via api
            leads_details_view.create_lead_verification(
                lead_email_value,
                ApiConstants.FIRST_NAME_VALUE_1.value,
                ApiConstants.LAST_NAME_VALUE_1.value)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_lead",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Api')
    @allure.story('Read Leads')
    @pytest.mark.run(order=8)
    def test_read_leads(self, driver, brand):
        try:
            # Create affiliates object
            affiliates = AffiliatesListView(driver)

            # Step 1: Go to Affiliates module
            affiliates.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Search for 'dev' via affiliates searchbar
            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "PandaDev")

            # Step 3: Get secret key
            secret_key = affiliates.get_secret_key()

            api = Api(driver)

            # Step 4: Go to api
            api.go_to()

            # Step 5: Apply authentication proccess using 'secret key'
            api.authorization_process(secret_key)

            # Step 6: Verify authentication process
            api.authorization_process_verification()

            # Step 7: Read Leads via api
            api.read_leads()

            # Step 8: Read Leads verification
            api.read_leads_response_verification(ApiAction.READ_LEADS_RESPONSE.value)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 9 : Go to crm main screen
            crm_main_screen.go_to()

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_read_leads",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.ApiResponseCode import ApiAction
from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldElements, FieldName, FieldNameConstants
from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.page_objects.api.Api import ApiConstants, Api
from src.page_objects.crm.AffiliatesListView import AffiliatesListView
from src.page_objects.crm.ClientsDetailsView import ClientDetailsView
from src.page_objects.crm.ClientsListView import ClientsListView
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView
from src.page_objects.crm.CrossModuleListView import CrossModuleListView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.LeadsListView import CreateLeadConstants, LeadsListView
from src.tests.conftest import get_brand_url, brand


@pytest.mark.usefixtures("driver", "brand")
class Test_Dragon:

    @pytest.mark.regression
    @allure.feature('Dragon Tests')
    @allure.story('Dragon - Api - client, valid phone registration')
    @pytest.mark.run(order=1)
    def test_client_api_registration_valid_phone(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            crm_main_screen.go_to()

            affiliates = AffiliatesListView(driver)
            affiliates.go_to()
            affiliates.go_to()
            affiliates.go_to()


            list_view_cross_module = CrossModuleListView(driver)
            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "PandaDev")

            secret_key = affiliates.get_secret_key()

            api = Api(driver)
            api.go_to()

            api.authorization_process(secret_key)
            api.authorization_process_verification()

            api = Api(driver)

            #Create customer via api
            api.create_customer(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_F.value,
                                ApiConstants.PASSWORD.value,
                                ApiConstants.COUNTRY_VALUE.value,
                                ApiConstants.FIRST_NAME_VALUE_1.value,
                                ApiConstants.LAST_NAME_VALUE_1.value,
                                ApiConstants.PHONE_VALID.value)

            api.response_code_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            crm_main_screen.go_to()

            clients_module = ClientsListView(driver)
            clients_module.go_to()

            list_view_cross_module = CrossModuleListView(driver)
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            details_view_cross_module = CrossModuleDetailsView(driver)

            # Search for client via email
            details_view_cross_module.search_via_email(
                ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_F.value)

            # Phone verification
            list_view_cross_module.listview_phone_verification("valid")

            # Navigate back to list view
            clients_module.go_to()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="dragon_clients_module",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.regression
    @allure.feature('Dragon Tests')
    @allure.story('Dragon - Api - client, invalid phone registration')
    @pytest.mark.run(order=2)
    def test_client_api_registration_invalid_phone(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            crm_main_screen.go_to()

            affiliates = AffiliatesListView(driver)
            affiliates.go_to()

            list_view_cross_module = CrossModuleListView(driver)
            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "PandaDev")

            secret_key = affiliates.get_secret_key()

            api = Api(driver)
            api.go_to()

            api.authorization_process(secret_key)
            api.authorization_process_verification()

            api = Api(driver)

            #Create customer via api
            api.create_customer(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_D.value,
                                ApiConstants.PASSWORD.value,
                                ApiConstants.COUNTRY_VALUE.value,
                                ApiConstants.FIRST_NAME_VALUE_1.value,
                                ApiConstants.LAST_NAME_VALUE_1.value,
                                ApiConstants.PHONE_INVALID.value)

            api.response_code_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            crm_main_screen.go_to()

            clients_module = ClientsListView(driver)
            clients_module.go_to()

            list_view_cross_module = CrossModuleListView(driver)
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            details_view_cross_module = CrossModuleDetailsView(driver)

            # Search for client via email
            details_view_cross_module.search_via_email(
                ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_D.value)

            # Phone verification
            list_view_cross_module.listview_phone_verification("valid")


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="dragon_clients_module",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.regression
    @allure.feature('Dragon Tests')
    @allure.story('Dragon - Api - client, invalid phone registration')
    @pytest.mark.run(order=3)
    def test_client_change_phone_field_to_invalid_and_valid(self, driver):
        try:
            driver.refresh()

            time.sleep(5)

            cross_module_details_view = CrossModuleDetailsView(driver)

            cross_module_details_view.go_to_via_searchbar_using_email(ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_D.value, "clients")

            cross_module_details_view = CrossModuleDetailsView(driver)

            cross_module_details_view.details_view_phone_verification("valid")

            cross_module_details_view.edit_field_via_pencil(FieldName.PHONE_FIELD,
                                                            FieldNameConstants.INVALID_PHONE_A)

            cross_module_details_view.details_view_phone_verification("invalid")

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_client_change_phone_field_to_invalid_and_valid",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.regression
    @allure.feature('Dragon Tests')
    @allure.story('Dragon - Api - lead, invalid phone registration')
    @pytest.mark.run(order=4)
    def test_leads_change_phone_field_to_invalid_and_valid(self, driver,brand):
        try:
            driver.refresh()

            time.sleep(5)
            """START - Creation of lead via api for this Dragon test"""
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
                ApiConstants.LEAD_EMAIL_VALUE_3.value,
                ApiConstants.FIRST_NAME_VALUE_1.value,
                ApiConstants.LAST_NAME_VALUE_1.value,
                ApiConstants.PHONE_INVALID.value)

            # Step 8 : Create customer verification
            api.response_code_verification(ApiAction.CREATE_LEAD_RESPONSE.value)

            """END - Creation of lead via api for this Dragon test"""

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
            cross_module_details_view = CrossModuleDetailsView(driver)

            cross_module_details_view.details_view_phone_verification("invalid")

            cross_module_details_view.go_to_via_searchbar_using_email(ApiConstants.LEAD_EMAIL_VALUE_3.value, "leads")

            cross_module_details_view.edit_field_via_pencil(FieldName.PHONE_FIELD,
                                                            FieldNameConstants.VALID_PHONE)

            cross_module_details_view.details_view_phone_verification("valid")

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_client_change_phone_field_to_invalid_and_valid",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False
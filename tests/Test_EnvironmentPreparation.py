
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldNameConstants, FieldName
from src.page_objects.crm.FinancialTransactionsListView import FinancialTransactionsListView
from src.page_objects.crm.TasksListView import TasksListView
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
from src.tests.conftest import get_brand_url

@pytest.mark.usefixtures("driver", "brand")
class Test_EnvironmentPreparation:

    @pytest.mark.environment
    @allure.feature('Api')
    @allure.story('Create Customer')
    @pytest.mark.run(order=1)
    def test_customer_creation(self, driver, brand):
        try:
            affiliates = AffiliatesListView(driver)

            affiliates.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "dev")

            secret_key = affiliates.get_secret_key()

            api = Api(driver)
            api.go_to()

            api.authorization_process(secret_key)

            api.authorization_process_verification()

            api = Api(driver)

            # Create 1st customer/client - '@test'
            api.create_customer(ApiConstants.ENVIRONMENT_PREP_CUSTOMER_1.value,
                                ApiConstants.PASSWORD.value,
                                ApiConstants.COUNTRY_VALUE.value,
                                ApiConstants.FIRST_NAME_VALUE_1.value,
                                ApiConstants.LAST_NAME_VALUE_1.value,
                                ApiConstants.PHONE_INVALID.value)

            api.response_code_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)

            # Create 2nd customer/client - 'qa qa'
            api.create_customer(ApiConstants.ENVIRONMENT_PREP_CUSTOMER_2.value,
                                ApiConstants.PASSWORD.value,
                                ApiConstants.COUNTRY_VALUE.value,
                                ApiConstants.FIRST_NAME_VALUE_1.value,
                                ApiConstants.LAST_NAME_VALUE_1.value,
                                ApiConstants.PHONE_INVALID.value)

            api.response_code_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)

            # Create 3nd customer/client - 'dima edunov'
            api.create_customer(ApiConstants.ENVIRONMENT_PREP_CUSTOMER_3.value,
                                ApiConstants.PASSWORD.value,
                                ApiConstants.COUNTRY_VALUE.value,
                                ApiConstants.FIRST_NAME_VALUE_2.value,
                                ApiConstants.LAST_NAME_VALUE_2.value,
                                ApiConstants.PHONE_INVALID.value)

            api.response_code_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)


            api.create_customer("CAautotests@pandats.com",
                                "123456789a",
                                "de",
                                "Yarin",
                                "AUTO",
                                "49508771234")

            api.response_code_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)


        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_lead_creation",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.environment
    @allure.feature('Api')
    @allure.story('Create Lead')
    @pytest.mark.run(order=2)
    def test_lead_creation(self, driver, brand):
        try:
            #
            api = Api(driver)
            #1st lead Creation - 'donottouch+automationLeadPencil@pandats.com'
            lead_email_value_1 = api.create_lead(
                ApiConstants.COUNTRY_DE.value,
                ApiConstants.ENVIRONMENT_PREP_LEAD_1.value,
                ApiConstants.FIRST_NAME_VALUE_1.value,
                ApiConstants.LAST_NAME_VALUE_1.value,
                ApiConstants.PHONE_INVALID.value)

            #Create customer verification
            api.response_code_verification(ApiAction.CREATE_LEAD_RESPONSE.value)

           #2nd lead Creation - '@test'
            lead_email_value_2 = api.create_lead(
                ApiConstants.COUNTRY_DE.value,
                ApiConstants.ENVIRONMENT_PREP_LEAD_2.value,
                ApiConstants.FIRST_NAME_VALUE_1.value,
                ApiConstants.LAST_NAME_VALUE_1.value,
                ApiConstants.PHONE_INVALID.value)

            #Create customer verification
            api.response_code_verification(ApiAction.CREATE_LEAD_RESPONSE.value)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_lead_creation",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False



    @pytest.mark.environment
    @allure.feature('Client details View')
    @allure.story('Preparation client - Assign To "Anastasiia V')
    @pytest.mark.run(order=3)
    def test_preparation_client_assign_to(self, driver, brand):

        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            crm_main_screen.go_to()

            clients_module = ClientsListView(driver)

            clients_module.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            clients_details_view = ClientDetailsView(driver)

            clients_details_view.go_to_via_searchbar_using_client_name(SearchBar.CLIENT_NAME_VALUE_ENVIRONMENT_PREPARATION.value)

            clients_details_view.client_assigned_to("Anastasiia V")

            time.sleep(20)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_preparation_client_assign_to",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.environment
    @allure.feature('Client details View')
    @allure.story('Preparation client - Create "demo" account')
    @pytest.mark.run(order=4)
    def test_preparation_create_demo_account(self, driver, brand):

        try:
            clients_details_view = ClientDetailsView(driver)
            time.sleep(20)
            # Step 15: Create MT account
            clients_details_view.create_trading_account("demo")

            # Step 17: Verify MT account
            clients_details_view.create_trading_account_verification("demo")

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_preparation_create_demo_account",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            self.driver.refresh()
            assert False

    @pytest.mark.environment
    @allure.feature('Client details View')
    @allure.story('Deposit')
    @pytest.mark.run(order=5)
    def test_preparation_deposit(self, driver, brand):

        try:
            # Instanse of ClientsDetailsView object
            client_details_view = ClientDetailsView(driver)

            client_details_view.open_trading_account_menu()
            # Step 1 : Deposit of 0.75
            client_details_view.make_a_deposit("0.75")

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_deposit",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.environment
    @allure.feature('Client details View')
    @allure.story('Change field via pencil')
    @pytest.mark.run(order=6)
    def test_change_field_value(self, driver, brand):
        try:
            cross_module_details_view = CrossModuleDetailsView(driver)

            cross_module_details_view.edit_field_via_pencil(FieldName.MOBILE, FieldNameConstants.INVALID_PHONE_A)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_change_field_value",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.environment
    @allure.feature('Tasks')
    @allure.story('Create new task assign to "Panda Auto"')
    @pytest.mark.run(order=7)
    def test_tasks_create(self, driver, brand):
        try:
            tasks_list_view = TasksListView(driver)

            tasks_list_view.go_to()

            tasks_list_view.create_task("call")


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_tasks_create",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.environment
    @allure.feature('Financial Transactions')
    @allure.story('Create new task assign to "Panda Auto"')
    @pytest.mark.run(order=8)
    def test_financial_transactions_create_filter(self, driver, brand):
        try:
            financial_transaction_list_view = FinancialTransactionsListView(driver)

            financial_transaction_list_view.go_to()

            financial_transaction_list_view.create_new_filter()


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_tasks_create",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False



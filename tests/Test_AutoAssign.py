import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.ApiResponseCode import ApiAction
from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.page_objects.api.Api import Api, ApiConstants
from src.page_objects.crm.AffiliatesListView import AffiliatesListView
from src.page_objects.crm.AutoAssign import AutoAssign
from src.page_objects.crm.ClientsListView import ClientsListView
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView
from src.page_objects.crm.CrossModuleListView import CrossModuleListView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.LeadsDetailsView import LeadsDetailsView
from src.page_objects.crm.LeadsListView import LeadsListView
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
# Test name structure is taken from the QA checklist : 'Test_FeatureName_TestedBehaviorName'
class Test_AutoAssign(object):


    @pytest.mark.regression
    @allure.feature('Auto Assign')
    @allure.story('Add Rule Leads')
    @pytest.mark.run(order=1)
    def test_add_rule_leads(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            auto_assign = AutoAssign(driver)

            auto_assign.go_to()

            auto_assign.sort_last_item_first_in_list()

            auto_assign.create_rule("automation_leads_test", "leads")

            auto_assign.rule_verification("automation_leads_test")



        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
            name="test_add_rule",attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Auto Assign')
    @allure.story('Create Lead From API -Rule checkeup')
    @pytest.mark.run(order=2)
    def test_create_lead_from_api_rule_checkup(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # going to 'main screen'
            crm_main_screen.go_to()

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
                ApiConstants.COUNTRY_LI.value,
                ApiConstants.LEAD_EMAIL_VALUE_2.value,
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

            leads_details_view.create_lead_auto_assign_verification("Panda Auto")



        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_lead_from_api_rule_checkup",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False


    @pytest.mark.regression
    @allure.feature('Auto Assign')
    @allure.story('Edit Rule')
    @pytest.mark.run(order=3)
    def test_edit_rule(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # going to 'main screen'
            crm_main_screen.go_to()

            auto_assign = AutoAssign(driver)

            auto_assign.go_to()

            auto_assign.sort_last_item_first_in_list()

            auto_assign.edit_rule()

            auto_assign.rule_verification("EDITED automation_leads_test")

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_edit_rule",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False


    @pytest.mark.regression
    @allure.feature('Auto Assign')
    @allure.story('Delete Rule')
    @pytest.mark.run(order=4)
    def test_delete_rule_leads(self, driver, brand):
        try:
            auto_assign = AutoAssign(driver)

            auto_assign.rule_verification("EDITED automation_leads_test")

            auto_assign.delete_rule()

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_delete_rule",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False


    @pytest.mark.regression
    @allure.feature('Auto Assign')
    @allure.story('Add Rule Clients')
    @pytest.mark.run(order=5)
    def test_add_rule_clients(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            auto_assign = AutoAssign(driver)

            auto_assign.go_to()

            auto_assign.create_rule("automation_clients_test", "clients")

            auto_assign.sort_last_item_first_in_list()

            auto_assign.rule_verification("automation_clients_test")

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_add_rule", attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False



    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Auto Assign')
    @allure.story('Create Client From API -Rule checkeup')
    @pytest.mark.run(order=6)
    def test_create_client_from_api_rule_checkup(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # going to 'main screen'
            crm_main_screen.go_to()

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
            client_email_value = api.create_customer(
                ApiConstants.CUSTOMER_EMAIL_VALUE_OPTION_C.value,
                ApiConstants.PASSWORD.value,
                ApiConstants.COUNTRY_LI.value,
                ApiConstants.FIRST_NAME_VALUE_1.value,
                ApiConstants.LAST_NAME_VALUE_1.value,
                ApiConstants.PHONE_INVALID.value)

            # Step 8 : Create customer verification
            api.response_code_verification(ApiAction.CREATE_CUSTOMER_RESPONSE.value)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 9 : Go to crm main screen
            crm_main_screen.go_to()

            # Step 10: Go to leads details view
            clients_module_module = ClientsListView(driver)

            # step 11: go to leads module
            clients_module_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 12 : Select Test Clients[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Create object of Cross-module details view
            details_view_cross_module = CrossModuleDetailsView(driver)

            # Step 13 : Navigate to lead details view of created lead
            details_view_cross_module.go_to_via_searchbar_using_email(client_email_value, "clients")

            # Create object of leads details view
            leads_details_view = LeadsDetailsView(driver)

            leads_details_view.create_lead_auto_assign_verification("Panda Auto")



        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_lead_from_api_rule_checkup",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False


    @pytest.mark.regression
    @allure.feature('Auto Assign')
    @allure.story('Delete Rule')
    @pytest.mark.run(order=7)
    def test_delete_rule_clients(self, driver, brand):
        try:
            auto_assign = AutoAssign(driver)

            auto_assign.go_to()

            auto_assign.sort_last_item_first_in_list()

            auto_assign.rule_verification("automation_clients_test")

            auto_assign.delete_rule()

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # going to 'main screen'
            crm_main_screen.go_to()



        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_delete_rule",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False
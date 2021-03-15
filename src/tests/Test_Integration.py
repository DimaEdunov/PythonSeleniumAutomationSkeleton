import allure
import pytest
from allure_commons.types import AttachmentType


from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.page_objects.ca.ClientAreaPlugin import ClientAreaPlugin, ClientAreaPluginConstants
from src.page_objects.crm.ClientsDetailsView import ClientDetailsView
from src.page_objects.crm.ClientsListView import ClientsListView
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView
from src.page_objects.crm.CrossModuleListView import CrossModuleListView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver_ca", "brand")
class Test_Integration:

    @pytest.mark.dev
    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Integration')
    @allure.story('Registration Process')
    @pytest.mark.run(order=1)
    def test_registration_process(self, driver_ca, brand):
        try:

            ca_main_screen = ClientAreaPlugin(driver_ca, get_brand_url(brand).get("ca"))

            # Step 1: Go to the home page of the brand
            ca_main_screen.go_to()

            # Step 2: Register a new client to the platform
            ca_main_screen.sign_up_new_client(ClientAreaPluginConstants.FIRST_NAME.value,
                                              ClientAreaPluginConstants.LAST_NAME.value,
                                              ClientAreaPluginConstants.EMAIL.value,
                                              ClientAreaPluginConstants.VALID_PHONE.value,
                                              ClientAreaPluginConstants.PASSWORD.value)
            # Step 3: Go to crm main screen
            ca_main_screen.log_in_verification()

            crm_main_screen = InitialSignin(driver_ca, get_brand_url(brand).get("crm"))

            # Step 4: Go to crm main screen
            crm_main_screen.go_to()

            # Step 5: Sign in the crm
            crm_main_screen.sign_in("new", "pandaauto", "Pc37hho6p1JFKk")

            # Step 6: sign in verification
            crm_main_screen.sign_in_verification()

            clients_module = ClientsListView(driver_ca)

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver_ca)

            # Step 7: Select Test Clients[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 8: Search for the created client via 'Email'
            client_details_view = ClientDetailsView(driver_ca)

            details_view_cross_module = CrossModuleDetailsView(driver_ca)

            # Step 9: Navigate to client details view via search bar
            details_view_cross_module.go_to_via_searchbar_using_email(
                ClientAreaPluginConstants.EMAIL.value, "clients")

            # Step 10: Verify the creation of the new client via broker's platform
            client_details_view.create_client_verification(
                ClientAreaPluginConstants.EMAIL.value,
                ClientAreaPluginConstants.FIRST_NAME.value,
                ClientAreaPluginConstants.LAST_NAME.value)


        except:
            allure.attach(driver_ca.get_screenshot_as_png(),
                          name="test_registration_process",
                          attachment_type=AttachmentType.PNG)

            assert False

    @pytest.mark.dev
    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Integration')
    @allure.story('Sign in Process')
    @pytest.mark.run(order=1)
    def test_sign_in_process(self, driver_ca, brand):
        try:

            ca_main_screen = ClientAreaPlugin(driver_ca, get_brand_url(brand).get("ca"))

            # Step 1: Go to the home page of the brand
            ca_main_screen.go_to()

            # Step 2: Login to the platform with a pre existing CA test client
            ca_main_screen.log_in_client(ClientAreaPluginConstants.EMAIL.value, ClientAreaPluginConstants.PASSWORD.value)

        except:
            allure.attach(driver_ca.get_screenshot_as_png(),
                          name="test_sign_in_process",
                          attachment_type=AttachmentType.PNG)

            assert False

import os
import subprocess
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmDetailsViewFieldElements import FieldName, FieldNameConstants
from src.elements.dynamic_elements.CrmDetailsViewSectionElements import Section

from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.page_objects.crm.ClientsListView import ClientsListView
from src.page_objects.crm.CrossModuleDetailsView import CrossModuleDetailsView, EditFieldValues
from src.page_objects.crm.CrossModuleListView import CrossModuleListView, CrossModuleInputs
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.LeadsDetailsView import LeadsDetailsView
from src.page_objects.crm.LeadsListView import LeadsListView, CreateLeadConstants
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_LeadsDetailsView:

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Leads Details View')
    @allure.story('Edit personal details - Edit button')
    @pytest.mark.run(order=1)
    def test_edit_personal_details_edit_button(self, driver, brand):
        try:

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            # Create object for 'LeadsModule'
            leads_module = LeadsListView(driver)

            # step 1: go to leads module
            leads_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2 : Select Test Clients[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Create LeadsDetailsView object
            leads_details_view = LeadsDetailsView(driver)

            # Step 3 : Navigate to created lead - details view page
            list_view_cross_module.go_to_via_saerchbar("donottouch+automationLeadPencil@pandats.com", "leads")

            # Create object for 'DetailsView' cross-module logics
            details_view_cross_module = CrossModuleDetailsView(driver)

            # Step 4 : edit button - First Name, Last Name, City
            details_view_cross_module.edit_fields_edit_button(EditFieldValues.FIRST_NAME_NEW.value,
                                                              EditFieldValues.LAST_NAME_NEW.value,
                                                              EditFieldValues.CITY_NEW.value)

            cross_module_details_view = CrossModuleDetailsView(driver)
            cross_module_details_view.open_section(Section.ADDRESS_INFORMATION.value)

            # Step 5: Verify 'edit button' on lead details view
            leads_details_view.lead_edit_button_change_field_verification(EditFieldValues.FIRST_NAME_NEW.value,
                                                                          EditFieldValues.LAST_NAME_NEW.value,
                                                                          EditFieldValues.CITY_NEW.value)

            # Step 6: edit button, set default values | CleanUP : First Name, Last Name, City
            details_view_cross_module.edit_fields_edit_button(EditFieldValues.FIRST_NAME_DEFAULT.value,
                                                              EditFieldValues.LAST_NAME_DEFAULT.value,
                                                              EditFieldValues.CITY_DEFAULT.value)

        except:

            allure.attach(driver.get_screenshot_as_png(),

                          name="test_edit_personal_details_edit_button",

                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Leads details View')
    @allure.story('Change field via pencil')
    @pytest.mark.run(order=2)
    def test_leads_change_info_via_pencil(self, driver, brand):
        try:

            cross_module_details_view = CrossModuleDetailsView(driver)

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
    @allure.feature('Leads Details View')
    @allure.story('Convert Lead - Convert button')
    @pytest.mark.run(order=3)
    def test_convert_lead(self, driver, brand):
        try:
            # Create object for 'LeadsModule'
            leads_module = LeadsListView(driver)

            # step 1: go to leads module
            leads_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # step 2: create new lead
            email_value = leads_module.create_lead(CreateLeadConstants.FIRST_NAME_VALUE.value,
                                                   CreateLeadConstants.LAST_NAME_VALUE.value,
                                                   CreateLeadConstants.LEAD_EMAIL_VALUE.value)

            # Step 3: Select Test Leads[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Create LeadsDetailsView object
            leads_details_view = LeadsDetailsView(driver)

            # Step 4: convert lead
            leads_details_view.convert_lead('test', 'test', 'haifa', '0802206034', 'haifa', '123',
                                            'Afghanistan', '1', 'JAN', '1971')

            # Create object for 'ClientsModule'
            clients_module = ClientsListView(driver)

            # step 5: go to clients module
            clients_module.go_to()

            # Step 6: Select Test Clients[] filter
            list_view_cross_module.set_test_filter(Filters.FILTER_TEST.value)

            # Step 9 : verification of convert lead by search it's client and go to it's details view
            list_view_cross_module.go_to_via_saerchbar(email_value, "clients")
            time.sleep(5)

        except:
            allure.attach(driver.get_screenshot_as_png(),

                          name="test_convert_lead",

                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            crm_main_screen.go_to()
            assert False





from datetime import *
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar

from src.page_objects.crm.AffiliatesListView import AffiliatesListView
from src.page_objects.crm.CrossModuleListView import CrossModuleListView, ModuleNames, VerificationExportFields
from src.page_objects.crm.InitialSignin import InitialSignin
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_AffiliatesListView():

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Affiliates')
    @allure.story('Create Affiliate')
    # This decorator gives an order of a test
    @pytest.mark.run(order=1)
    def test_create_affiliate(self, driver, brand):
        try:
            time.sleep(5)
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            # Create affiliates object
            affiliates = AffiliatesListView(driver)

            # Step 3: Go to Affiliates module
            affiliates.go_to()

            # Step 3: create affiliate
            affiliates.create_affiliate("qa test affiliate")

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 4: search for created partner name
            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "qa test affiliate")

            # step 4: create affiliate verification 'partner name'
            list_view_cross_module.search_via_searchbar_verification("qa test affiliate")

            # step 5: create affiliate verification 'ip'
            list_view_cross_module.search_via_searchbar_verification("1.1.1.1")

            # step 6: create affiliate verification 'blocked countries'
            list_view_cross_module.search_via_searchbar_verification("Afghanistan")

        except:


            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_affiliate",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Affiliates')
    @allure.story('Delete Affiliate')
    # This decorator gives an order of a test
    @pytest.mark.run(order=2)
    def test_delete_affiliate(self, driver, brand):
        try:

            time.sleep(5)
            # Create affiliates object
            affiliates = AffiliatesListView(driver)

            # Step 1: Go to Affiliates module
            affiliates.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: search for created partner name
            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "qa test affiliate")

            # step 3: create affiliate verification 'partner name'
            list_view_cross_module.search_via_searchbar_verification("qa test affiliate")

            # step 4: create affiliate verification 'ip'
            list_view_cross_module.search_via_searchbar_verification("1.1.1.1")

            # step 5: create affiliate verification 'blocked countries'
            list_view_cross_module.search_via_searchbar_verification("Afghanistan")

            # step 6: Delete affiliate
            affiliates.remove_created_affiliate()

            # step 7: Delete affiliate verification
            affiliates.remove_created_affiliate_verification()

        except:


            allure.attach(driver.get_screenshot_as_png(),
                          name="test_delete_affiliate",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Affiliates')
    @allure.story('Export selected records')
    @pytest.mark.run(order=3)
    def test_export_selected_records(self, driver, brand):
        try:

            time.sleep(5)
            # Create affiliates object
            affiliates = AffiliatesListView(driver)

            # Step 1: Go to Affiliates module
            affiliates.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 2: Export Excel file
            excel_test_data = list_view_cross_module.export_records('affiliate', 'export_selected_records')

            # Step 3: Verify data is correct
            list_view_cross_module.export_verification(ModuleNames.AFFILIATES.value, 'excel', excel_test_data, VerificationExportFields.AFFILIATES)



        except:

            allure.attach(driver.get_screenshot_as_png(),
                          name="test_export_selected_records",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Affiliates List View')
    @allure.story('Searching by columns')
    @pytest.mark.run(order=4)
    def test_searching_by_columns(self, driver, brand):

        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main screen
            crm_main_screen.go_to()

            affiliates_list_view = AffiliatesListView(driver)

            affiliates_list_view.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            list_view_cross_module.search_via_searchbar(SearchBar.PARTNER_NAME, "PandaDev")

            list_view_cross_module.search_via_searchbar_verification("PandaDev")

        except:

            allure.attach(driver.get_screenshot_as_png(),
                          name="test_searching_by_columns",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
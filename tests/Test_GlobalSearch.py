import os
import subprocess
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmListViewFilterElements import Filters
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar
from src.page_objects.crm.ClientsListView import ClientsListView
from src.page_objects.crm.CrossModuleListView import CrossModuleListView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.page_objects.crm.LeadsDetailsView import LeadsDetailsView
from src.page_objects.crm.LeadsListView import LeadsListView, CreateLeadConstants
from src.page_objects.crm.TasksListView import TasksListView
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_LeadsListView:


    @pytest.mark.regression
    @allure.feature('Global Search')
    @allure.story('Search lead in global search')
    @pytest.mark.run(order=1)


    def test_search_lead_in_global_search(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            time.sleep(10)

            leads_module = LeadsListView(driver)

            # step 4: go to leads module
            leads_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 5 : Select All filter
            list_view_cross_module.set_test_filter(Filters.FILTER_ALL.value)

            # step 6: search lead via search bar
            searched = list_view_cross_module.search_lead_or_client_via_search_bar(SearchBar.EMAIL, "@test", "Lead")

            # step 7: search lead via global search

            searched = list_view_cross_module.search_lead_or_client_via_global_search(searched)

            # step 8: Verify the searched lead via global search is desirable lead
            list_view_cross_module.search_lead_or_client_via_global_search_verification(searched)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="search_lead_or_client_via_global_search_verification",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.regression
    @allure.feature('Global search - Tasks module')
    @allure.story('Search Client In Global Search')
    @pytest.mark.run(order=2)
    def test_search_client_in_global_search(self, driver, brand):
        try:
            time.sleep(5)
            clients_module = ClientsListView(driver)

            # step 4: go to clients module
            clients_module.go_to()

            # Create object for 'ListView' cross-module logics
            list_view_cross_module = CrossModuleListView(driver)

            # Step 5 : Select All filter
            list_view_cross_module.set_test_filter(Filters.FILTER_ALL.value)

            # step 6: search client via search bar
            searched = list_view_cross_module.search_lead_or_client_via_search_bar(SearchBar.EMAIL, "@test", "Client")

            # step 7: search client via global search

            tasks_module = TasksListView(driver)

            # step 8: go to tasks module
            tasks_module.go_to()

            searched = list_view_cross_module.search_lead_or_client_via_global_search(searched)

            # step 9: Verify the searched client via global search is desirable client
            list_view_cross_module.search_lead_or_client_via_global_search_verification(searched)


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_search_lead_via_global_search",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

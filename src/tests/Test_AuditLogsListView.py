import os
import subprocess
import time
from time import sleep
import allure
import pytest
from allure_commons.types import AttachmentType
from src.page_objects.crm.AuditLogsListView import AuditLogsListView
from src.page_objects.crm.CrossModuleListView import CrossModuleListView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.tests.conftest import get_brand_url
from src.elements.dynamic_elements.CrmListViewSearchbarElements import SearchBar



@pytest.mark.usefixtures("driver", "brand")
# Test name structure is taken from the QA checklist : 'Test_FeatureName_TestedBehaviorName'
class Test_AuditLogsListView(object):

    @pytest.mark.regression
    @allure.feature('Audit Logs')
    @allure.story('Searching by columns')
    @pytest.mark.run(order=1)
    def test_searching_columns(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            audit_logs_list_view = AuditLogsListView(driver)

            # Step 2: Go to Audit Logs module
            audit_logs_list_view.go_to()

            list_view_cross_module = CrossModuleListView(driver)

            time.sleep(4)

            # Step 5: search via searchbar - MODULE_LEADS/ACTION_DETAIL_VIEW
            list_view_cross_module.search_via_searchbar(SearchBar.COLUMN_MODULE, "Clients")
            list_view_cross_module.search_via_searchbar_verification("Accounts")
            driver.refresh()

            time.sleep(2)

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_searching_columns",
                          attachment_type=AttachmentType.PNG)
            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False



import allure
import pytest
from allure_commons.types import AttachmentType

from src.elements.CrmElements import CrmElements
from src.page_objects.crm.InitialSignin import InitialSignin

from src.page_objects.crm.MyDashboardListView import MyDashboardListView
from src.page_objects.crm.TasksListView import TasksListView
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_MyDashboardListView:



    @pytest.mark.regression
    @allure.feature('MyDashboard List View')
    @allure.story('Edit Event')
    @pytest.mark.run(order=2)
    def test_edit_event(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to CRM Main  screen
            crm_main_screen.go_to()

            mydashboard_list_view = MyDashboardListView(driver)

            # step 2: go to leads module
            mydashboard_list_view.go_to()

            # step 3: Navigate to show mine tasks
            mydashboard_list_view.navigate_to_show_mine_tasks("Show mine")

            # step 4: Edit ticket
            mydashboard_list_view.edit_event(CrmElements.NEW_STATUS_ADDITIONAL_ACTIONS_FIRST_OPTION)

            # step 5: Back to previous status for next running
            mydashboard_list_view.edit_event(CrmElements.NEW_STATUS_ADDITIONAL_ACTIONS_SECOND_OPTION)

        except:

            allure.attach(driver.get_screenshot_as_png(),
                          name="test_edit_event",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False
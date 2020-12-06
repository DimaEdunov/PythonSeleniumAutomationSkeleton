import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.page_objects.crm.HelpDeskDetailsView import HelpDeskDetailsView
from src.page_objects.crm.HelpDeskListView import HelpDeskListView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_HelpDeskDetailsView:


    @pytest.mark.regression
    @allure.feature('Help Desk')
    @allure.story('Edit ticket via edit button')
    @pytest.mark.run(order=1)
    def test_edit_ticket_via_edit_button(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            time.sleep(10)

            """" Creation of a ticket - START """
            help_desk_list_view = HelpDeskListView(driver)

            help_desk_list_view.go_to()

            # Step 3: Create a new ticket
            help_desk_list_view.create_new_ticket()

            # Instance of an object 'HelpDeskDetailsView'
            help_desk_details_view = HelpDeskDetailsView(driver)

            # Step 4: navigate to help desk details view
            help_desk_details_view.go_to()

            # Step 5: Verify creation of ticket
            help_desk_details_view.create_edit_ticket_verification("title", "General Question", "Open")

            """ Creation of a ticket - END """

            # Instance of an object 'HelpDeskDetailsView'
            help_desk_details_view = HelpDeskDetailsView(driver)

            # Step 1 : Edit details via pencil
            help_desk_details_view.edit_ticket_via_edit_button()

            # Step 2 : Verify creation of ticket
            help_desk_details_view.create_edit_ticket_verification("title edited via edit", "General Question",
                                                                   "Pending")


        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_edit_ticket_via_edit_button",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Help desk')
    @allure.story('Edit ticket via pencil button')
    @pytest.mark.run(order=2)
    def test_edit_ticket_via_pencil(self, driver, brand):
        try:
            # Instance of an object 'HelpDeskDetailsView'
            help_desk_details_view = HelpDeskDetailsView(driver)

            # Step 1 : Edit details via pencil
            help_desk_details_view.edit_ticket_via_pencil()

            # Step 2 : Verify details were changed.
            help_desk_details_view.edit_ticket_via_pencil_verification()

        except:
            allure.attach(driver.get_screenshot_as_png(),
                          name="HelpDeskModule.test_edit_ticket_via_pencil",
                          attachment_type=AttachmentType.PNG)

            # Recovery step
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()
            assert False

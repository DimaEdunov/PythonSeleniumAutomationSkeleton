

import allure
import pytest
from allure_commons.types import AttachmentType
from src.page_objects.crm.CampaignListView import CampaignListView
from src.page_objects.crm.InitialSignin import InitialSignin
from src.tests.conftest import get_brand_url


@pytest.mark.usefixtures("driver", "brand")
class Test_CampaignListView(object):

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Campaign')
    @allure.story('Create new campaign')
    @pytest.mark.run(order=1)
    def test_create_new_campaign(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            campaign_list_view = CampaignListView(driver)

            # Step 2: Go to campaign module
            campaign_list_view.go_to()

            # Step 3 : create new campaign
            campaign_name = campaign_list_view.create_new_campaign()

            # Step 4 : newly created campaign verification
            campaign_list_view.create_new_campaign_verification()

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_create_new_campaign",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Campaign')
    @allure.story('Edit campaign')
    @pytest.mark.run(order=2)
    def test_edit_campaign(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            crm_main_screen.go_to()

            campaign_list_view = CampaignListView(driver)

            campaign_list_view.go_to()

            campaign_list_view.edit_campaign()

            campaign_list_view.edit_campaign_verification()

        except:
            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
            name="test_edit_campaign",
            attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature('Campaign')
    @allure.story('Delete new campaign')
    @pytest.mark.run(order=3)
    def test_delete_new_campaign(self, driver, brand):
        try:
            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))

            # Step 1: Go to Crm main screen
            crm_main_screen.go_to()

            campaign_list_view = CampaignListView(driver)

            # Step 2: Go to campaign module
            campaign_list_view.go_to()

            # Step 3: Delete campaign
            campaign_list_view.delete_new_campaign()

            # Step 4: Delete verification
            campaign_list_view.delete_new_campaign_verification()

        except:

            # Recovery step
            allure.attach(driver.get_screenshot_as_png(),
                          name="test_delete_new_campaign",
                          attachment_type=AttachmentType.PNG)

            crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
            crm_main_screen.go_to()

            assert False


    # @pytest.mark.regression
    # @pytest.mark.sanity
    # @allure.feature('Campaign')
    # @allure.story('Info Link')
    # @pytest.mark.run(order=3)
    # def test_info_link(self, driver, brand):
    #     try:
    #         campaign_list_view = CampaignListView(driver)
    #
    #         # Step 3: Delete campaign
    #         campaign_list_view.open_info_link()
    # 
    #         # Step 4: Delete verification
    #         campaign_list_view.open_info_link_verification()
    #
    #         crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
    #
    #         # Step 1: Go to Crm main screen
    #         crm_main_screen.go_to()
    #
    #     except:
    #
    #         # Recovery step
    #         allure.attach(driver.get_screenshot_as_png(),
    #                       name="test_info_link",
    #                       attachment_type=AttachmentType.PNG)
    #
    #         crm_main_screen = InitialSignin(driver, get_brand_url(brand).get("crm"))
    #         crm_main_screen.go_to()
    #
    #         assert False
import random
import string
from datetime import *
import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmSideMenuElements import Modules, CrmSideMenu
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from src.infrastructure.dynamic_helpers.ScrollActions import ScrollActions
from src.infrastructure.dynamic_helpers.SwitchTo import SwitchTo


class CampaignListView(object):

    campaign_name = "qaAutomation" + ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    campaign_name_edit = "qaAutomation" + ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    def __init__(self, driver):
        self.driver = driver

    @allure.step("CampaignListView.go_to() | Go to Campaign")
    def go_to(self):

        module = CrmSideMenu.side_menu_items(self.driver, Modules.CAMPAIGNS_MODULE.value)
        self.driver.execute_script("arguments[0].scrollIntoView();", module)
        # Navigating to clients module screen
        CrmSideMenu.side_menu_items(self.driver, Modules.CAMPAIGNS_MODULE.value).click()
        time.sleep(3)

    @allure.step("CampaignListView.create_new_campaign() | Create a new campaign")
    def create_new_campaign(self):

        WebDriverWait(self.driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, CrmElements.MODULE_IFRAME)))

        create_new_button = self.driver.find_element(By.XPATH, CrmElements.ADD_NEW_CAMPAIGN_BUTTON)

        create_new_button.click()

        time.sleep(5)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CAMPAIGN_NAME_FIELD))).send_keys(CampaignListView.campaign_name)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CAMPAIGN_ASSIGN_TO_FIELD_CLICK))).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CAMPAIGN_ASSIGN_TO_FIELD))).send_keys("Panda Auto")

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CAMPAIGN_ASSIGN_TO_RESULTS_LIST)))

        time.sleep(2)
        self.driver.find_elements(By.XPATH,CrmElements.CAMPAIGN_ASSIGN_TO_RESULTS_LIST)[0].click()

        self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_RATE_FIELD).send_keys("1")

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CAMPAIGN_SAVE_BUTTON))).click()

    @allure.step("CampaignListView.create_new_campaign_verification() | Create a new campaign verification")
    def create_new_campaign_verification(self):

        time.sleep(3)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, CrmElements.CAMPAIGN_LIST_VIEW_FIRST_ROW)))

        first_row_parent_item = self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_LIST_VIEW_FIRST_ROW)
        first_rom_cell_items = first_row_parent_item.find_elements(By.XPATH, CrmElements.CAMPAIGN_CELL_ITEM_ELEMENT)

        counter = 0
        for cell_content in first_rom_cell_items:
            counter += 1
            if counter < 300 and CampaignListView.campaign_name in cell_content.text:
                break

            if counter > 300:
                assert False


    @allure.step("CampaignListView.edit_campaign() | Edit campaign ")
    def edit_campaign(self):
        time.sleep(5)

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_SEARCHHBAR_IFRAME))

        self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_SEARCH_CAMPAIGN_FIELD).clear()

        self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_SEARCH_CAMPAIGN_FIELD).send_keys(CampaignListView.campaign_name)
        time.sleep(5)

        hoverer = ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_EDIT_BUTTON)).move_by_offset(20, 0)
        hoverer.perform()

        self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_EDIT_BUTTON).click()

        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, CrmElements.CAMPAIGN_NAME_FIELD))).send_keys(CampaignListView.campaign_name_edit)
        time.sleep(5)

        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, CrmElements.CAMPAIGN_SAVE_BUTTON))).click()


    @allure.step("CampaignListView.edit_campaign_verification() | Edit campaign verification")
    def edit_campaign_verification(self):
        time.sleep(3)

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, CrmElements.CAMPAIGN_LIST_VIEW_FIRST_ROW)))

        first_row_parent_item = self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_LIST_VIEW_FIRST_ROW)
        first_rom_cell_items = first_row_parent_item.find_elements(By.XPATH, CrmElements.CAMPAIGN_CELL_ITEM_ELEMENT)

        counter = 0
        for cell_content in first_rom_cell_items:
            counter += 1
            if counter < 300 and CampaignListView.campaign_name in cell_content.text:
                break
            if counter > 300:
                assert False


    @allure.step("CampaignListView.delete_new_campaign() | Delete a new campaign ")
    def delete_new_campaign(self):
        time.sleep(5)

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_SEARCHHBAR_IFRAME))

        self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_SEARCH_CAMPAIGN_FIELD).clear()

        self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_SEARCH_CAMPAIGN_FIELD).send_keys(CampaignListView.campaign_name + CampaignListView.campaign_name_edit)
        time.sleep(4)

        hoverer = ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH,
                                     CrmElements.CAMPAIGN_DELETE_BUTTON)).move_by_offset(20, 0)

        hoverer.perform()

        self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_DELETE_BUTTON).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CAMPAIGN_DELETE_CONFIRMATION_BUTTON))).click()

    @allure.step("CampaignListView.delete_new_campaign_verification() | Delete a new campagin verification")
    def delete_new_campaign_verification(self):

        time.sleep(3)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, CrmElements.CAMPAIGN_LIST_VIEW_FIRST_ROW)))

        first_row_parent_item = self.driver.find_element(By.XPATH, CrmElements.CAMPAIGN_LIST_VIEW_FIRST_ROW)
        first_rom_cell_items = first_row_parent_item.find_elements(By.XPATH, CrmElements.CAMPAIGN_CELL_ITEM_ELEMENT)

        counter = 0
        for cell_content in first_rom_cell_items:
            counter += 1

            if counter < 300 and CampaignListView.campaign_name in cell_content.text:
                assert False

            if counter > 300:
                break

    def open_info_link(self):

        # Get 'CRM' screen ID of screen 'FIRST SCREEN'
        first_screen_identifier = self.driver.window_handles[0]

        # Clicking on 'API Link'
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.INFO_LINK)))

        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(By.XPATH, CrmElements.INFO_LINK))

        # Get 'API's screen ID of screen 'SECOND SCREEN'
        second_screen_identifier = self.driver.window_handles[1]

        # Create object of SwitchTo
        switch_to_helper = SwitchTo(first_screen_identifier, second_screen_identifier, self.driver)

        # Switch to second screen ID -> 'API' screen
        switch_to_helper.switch_to("1")

        # Get second's screen URL -> 'API' screen
        second_screen_url = self.driver.current_url

        self.driver.close()

        # Switch back to 'FIRST SCREEN' - > CRM
        switch_to_helper.switch_to("0")

        # Open 'API' url in 'FIRST SCREEN'
        self.driver.get(second_screen_url)


    def open_info_link_verification(self):

        time.sleep(3)
        if ".pdf" in self.driver.current_url:
            pass

        else:
            assert False


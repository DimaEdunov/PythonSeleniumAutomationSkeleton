from enum import Enum
import time as time_wait

import allure
import random
import string
from datetime import *
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmSideMenuElements import CrmSideMenu, Modules
from src.elements.dynamic_elements.CrmMyDashboardElements import MyDashboardConstants, MyDashboardElements
from src.infrastructure.dynamic_helpers.ScrollActions import ScrollActions

class CreateMyDashboardConstants(Enum):
    # Create lead right slider
    NEW_EVENT_STATUS = "Planned"

    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    PASSWORD = "Aa111111"
    COUNTRY_VALUE = "de"
    FIRST_NAME_VALUE = "Jack" + random_character
    LAST_NAME_VALUE = "Jackson" + random_character
    random_number = datetime.now().strftime('%H%M%S%f')
    LEAD_EMAIL_VALUE = "pandaqa+" + random_number + "@pandats.com"


class MyDashboardListView(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("MyDashboardModule.go_to() | Navigating to My Dashboard Module")
    @allure.severity(allure.severity_level.NORMAL)
    def go_to(self):
        try:
            # Scrolling to element 'Affiliates' module
            ScrollActions.scroll_to(self.driver.find_element(By.XPATH, CrmElements.SIDE_MENU_MY_DASHBOARD))

            # Clicking on 'Affiliates'
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_MY_DASHBOARD))).click()


            time_wait.sleep(5)

            WebDriverWait(self.driver, 50).until(
                EC.invisibility_of_element_located((By.XPATH, CrmElements.SPINNER)))
            time_wait.sleep(3)

        except:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="MyDashboardModule.go_to",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("MyDashboard.navigate_to_show_mine_tasks() | Navigate to my tasks")
    @allure.severity(allure.severity_level.NORMAL)
    def navigate_to_show_mine_tasks(self, tab_name):

        WebDriverWait(self.driver, 60).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, CrmElements.MODULE_IFRAME)))

        time_wait.sleep(2)
        print("Show all : " + str(len(self.driver.find_elements(By.XPATH, "//*[@id='main-tabs']/li[text()=' Show all ']"))))
        time_wait.sleep(2)
        print("Event Type : " + str(len(self.driver.find_elements(By.XPATH, "//a[@data-column-label='Event Type']"))))
        time_wait.sleep(2)


        if tab_name == "Show mine":
            show_mine_tab = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.SHOW_MINE_BUTTON)))

        elif tab_name == "Show all":
            show_mine_tab = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.SHOW_ALL_BUTTON)))

        self.driver.execute_script("arguments[0].scrollIntoView();", show_mine_tab)
        show_mine_tab.click()

    @allure.step("MyDashboard.edit_event() | Edit Event")
    @allure.severity(allure.severity_level.NORMAL)
    def edit_event(self, new_status):

        # Editing the event in -> my dashboard -> show mine tasks
        time_wait.sleep(3)

        check_previous_status = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.CHECK_STATUS_OF_USER)))

        user_previous_status = check_previous_status.text

        pencil_icon = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.PENCIL_ICON)))

        self.driver.execute_script("arguments[0].click();", pencil_icon)

        time_wait.sleep(1)

        # Change status in additional status
        additional_actions = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ADDITIONAL_ACTIONS_BUTTON)))

        self.driver.execute_script("arguments[0].click();", additional_actions)

        time_wait.sleep(1)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.STATUS_ADDITIONAL_ACTIONS))).click()

        new_status_additional_actions_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, new_status)))

        time_wait.sleep(1)

        new_status_additional_actions_element.click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.CHANGE_ADDITIONAL_STATUS_BUTTON))).click()

        time_wait.sleep(1)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.EDIT_TICKET_SAVE_BUTTON))).click()

        time_wait.sleep(2)
        check_user_status = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CrmElements.CHECK_STATUS_OF_USER)))

        # Check if status is changed
        if check_user_status.text == user_previous_status:
            assert False

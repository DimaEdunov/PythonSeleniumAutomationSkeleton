from enum import Enum
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class ActionsConstants(Enum):

    #CrossModule
    #Tasks
    SMS_ACTION = 'sms'
    C2C_ACTION = 'phone'
    EMAIL_ACTION = 'email'
    EDIT_ACTION = 'edit'
    DELETE_ACTION = 'delete'

class ListViewActionsMenu(object):

    @staticmethod
    def hover_more_button(driver, row):
        actions = ActionChains(driver)
        actions_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//table/tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))][%s]//mat-icon[.='more_vert']" % row)))
        actions.move_to_element(actions_menu).perform()

    @staticmethod
    def choose_actions_menu_item(driver, row, action_name):
        action_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                            "//table/tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))][%s]//button[@title='%s']//mat-icon" % (row, action_name))))
        driver.execute_script("arguments[0].click();", action_item)



    @staticmethod
    def column_sort_button(driver, column_name):

        return WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,
                                            "//th[contains(text(),' %s ')]//button" % column_name)))


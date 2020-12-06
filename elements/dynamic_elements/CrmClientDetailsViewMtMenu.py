from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CrmClientDetailsViewMtMenuConstants(Enum):
    # MT button names
    CREATE_TRADING_ACCOUNT_TYPE_1 = "Create Trading Account"
    CREATE_TRADING_ACCOUNT_TYPE_2 = "Create MT User"
    UPDATE_TRADING_ACCOUNT = "Update Trading Account"
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"
    TRANSFER_BETWEEN_TA = "Transfer between TA"
    CREDIT_IN = "Credit in"
    CREDIT_OUT = "Credit out"
    CHANGE_TA_PASSWORD = "Manage TA Password"

    # MT Menus
    MT_ACTIONS_MENU_TYPE_1 = "Trading Accounts Actions"
    MT_ACTIONS_MENU_TYPE_2 = "MT Actions"
    CRM_ACTIONS_MENU = "CRM Actions"
    MANAGE_TA_PASSWORD = "Manage Password"


class CrmClientDetailsViewMtActions():

    @staticmethod
    def mt_sidemenu_button(driver, mt_menu_button):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@id='cdk-accordion-child-3' or @id='cdk-accordion-child-2']//div[text()=' %s ']//i" % mt_menu_button)))

        return driver.find_element(By.XPATH,
                                   "//div[@id='cdk-accordion-child-3' or @id='cdk-accordion-child-2']//div[text()=' %s ']//i" % mt_menu_button)

    @staticmethod
    def open_close_mt_menu(driver, menu_type):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='mat-expansion-panel-header-3']//mat-panel-title[contains(text(),'%s')]" % menu_type)))

        return driver.find_element(By.XPATH,
                                   "//*[@id='mat-expansion-panel-header-3']//mat-panel-title[contains(text(),'%s')]" % menu_type)


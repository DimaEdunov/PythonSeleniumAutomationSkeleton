from enum import Enum
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Modules(Enum):
    HELP_DESK_MODULE = "Help Desk"
    CAMPAIGNS_MODULE = "Campaigns"
    AUDIT_LOGS_MODULE = "Audit Logs"
    LEADS_MODULE = "Leads"
    CLIENTS_MODULE = "Clients"
    TASKS_MODULE = "Tasks"
    AFFILIATES_MODULE = "Affiliates"
    DOCUMENTS_MODULE = "Documents"
    TRADING_ACCOUNTS_MODULE = "Trading Accounts"
    FINANCIAL_TRANSACTIONS_MODULE = "Financial Transactions"
    MY_DASHBOARD_MODULE = "My Dashboard"
    USER_MANAGEMENT_MODULE_ = "User Management"
    CRM_CONFIGURATION_MODULE = "CRM Configuration"
    TRADES = "Trades"
    AUTO_ASSIGN_MODULE = "AutoAssign"
    # Workflows module is no 'CRMElements'


    # Top user item - For sign-out, is in CrmElements

class CrmSideMenu (object):

    # 'Settings' item is exceptional and can be found in CrmElements.py
    @staticmethod
    def side_menu_items(driver, module_name):
        time.sleep(4)
        module = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='nav-menu']//a[contains(text(), '%s')]" % module_name)))
        time.sleep(2)
        return module
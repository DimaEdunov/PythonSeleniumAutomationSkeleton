import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmSideMenuElements import Modules, CrmSideMenu


class TradesListView():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("TradesListView.go_to() | Navigating to Trades")
    def go_to(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SIDE_MENU_WAIT_VERIFICATION_ELEMENT)))

        time.sleep(3)
        trading_accounts = CrmSideMenu.side_menu_items(self.driver, Modules.TRADES.value)
        self.driver.execute_script("arguments[0].scrollIntoView();", trading_accounts)

        # Navigating to clients module screen
        CrmSideMenu.side_menu_items(self.driver, Modules.CAMPAIGNS_MODULE.value).click()
        time.sleep(3)

        # Navigating to clients module screen
        trading_accounts.click()

        time.sleep(3)
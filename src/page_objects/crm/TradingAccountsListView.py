import allure

from src.elements.dynamic_elements.CrmSideMenuElements import Modules, CrmSideMenu


class TradingAccountsListView():

    def __init__(self, driver):
        self.driver = driver

    @allure.step("TradingAccountsListView.go_to() | Navigating to Trading accounts")
    def go_to(self):
        # Navigating to clients module screen
        CrmSideMenu.side_menu_items(self.driver, Modules.TRADING_ACCOUNTS_MODULE.value).click()
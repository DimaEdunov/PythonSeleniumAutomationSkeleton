import time

import allure
from allure_commons.types import AttachmentType

from src.elements.dynamic_elements.CrmListViewFilterElements import FilterElements, Filters
from src.elements.dynamic_elements.CrmSideMenuElements import CrmSideMenu, Modules


class AuditLogsListView:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("AuditLogsListView.go_to() | Navigating to Audit Logs Module")
    def go_to(self):
        try:
            # Navigating to audit logs module screen
            CrmSideMenu.side_menu_items(self.driver, Modules.AUDIT_LOGS_MODULE.value).click()

            time.sleep(5)

        except:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="AuditLogsListView.go_to",
                          attachment_type=AttachmentType.PNG)
            assert False

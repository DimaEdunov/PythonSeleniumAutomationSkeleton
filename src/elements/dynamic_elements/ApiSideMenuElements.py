from enum import Enum
from selenium.webdriver.common.by import By


class ApiSideMenuItems(Enum):

    # Side Menu elements
    # Note : 'Partner Secret' field key is not part of the 'ul' list
    AUTHORIZATION_SECTION = "Authorization"
    C_CUSTOMER = "[C] Customer"
    R_CUSTOMER = "[R] Customer"
    R_CUSTOMERS = "[R] Customers"
    U_COSTUMER = "[U] Customer"
    C_LEADS = "[C] Leads"
    R_LEADS = "[R] Leads"


class ApiSideMenuElements(object):
    @staticmethod
    def navigate_to(driver, side_menu_element):
        if (side_menu_element ==
                ApiSideMenuItems.AUTHORIZATION_SECTION or
                ApiSideMenuItems.R_CUSTOMER or
                ApiSideMenuItems.U_COSTUMER or
                ApiSideMenuItems.C_CUSTOMER or
                ApiSideMenuItems.R_CUSTOMERS or
                ApiSideMenuItems.C_LEADS or
                ApiSideMenuItems.R_LEADS):

            side_menu_item = driver\
                .find_element(By.XPATH, "//a[text()='%s']" % side_menu_element)

            return side_menu_item

        else:
            print("Wrong 'side_menu_element' chosen")

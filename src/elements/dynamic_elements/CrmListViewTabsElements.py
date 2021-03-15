import time
from enum import Enum

from selenium.webdriver.common.by import By
from src.elements.CrmElements import CrmElements


class TabNames(Enum):
    # Affiliate Filter Enums
    ALL = "All"
    BAD = "BAD"
    FTD = "FTD"
    NEW = "New"
    ONLINE = "Online"
    APPROVED = "Approved"
    PENDING = "Pending"
    CLOSED = "Closed"
    IN_PROGRESS = "In Progress"
    SHOW_ALL = "Show all"
    SHOW_MINE = "Show mine"

class TabElements():

    @staticmethod
    def choose_tab_element(driver, tab_name):
        time.sleep(2)

        return driver.find_element(By.XPATH,
                            "//button//span[contains(text(),'%s')]"% tab_name)

    @staticmethod
    def get_number_of_records(driver):
        time.sleep(10)
        print("xxxxxxxxxxx")
        print(len(driver.find_elements(By.XPATH,CrmElements.SHOW_RECORDS_BUTTON)))
        if len(driver.find_elements(By.XPATH,CrmElements.SHOW_RECORDS_BUTTON)) > 0:
            driver.find_element(By.XPATH,CrmElements.SHOW_RECORDS_BUTTON).click()
            time.sleep(3.5)
        return driver.find_element(By.XPATH, "//span[contains(@class,'total-records')]").text
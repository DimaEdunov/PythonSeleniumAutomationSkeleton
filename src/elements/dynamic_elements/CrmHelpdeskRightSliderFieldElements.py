from datetime import *
import time
from enum import Enum
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

""" Works in all modules beside Help-Dep """
class HelpdeskRightSliderFieldConstants(Enum):

    # Field names
    TITLE = "Title"
    DESCRIPTION_INFORMATION = "Description information"


    # Name of picklist
    ASSIGNED_TO_NAME_OF_PICKLIST = "assigned_id"
    LEAD_STATUS_NAME_OF_PICKLIST = "Lead Status"
    STATUS_NAME_OF_PICKLIST = "ticket_statuses"
    CATEGORY_NAME_OF_PICKLIST = "ticket_types"

    # Value in picklist
    ASSIGNED_TO_PICKLIST_VALUE = "Panda Auto"
    STATUS_FTD_PICKLIST_VALUE = "FTD"
    STATUS_OPEN_PICKLIST_VALUE = "Open"
    STATUS_IN_PROGRESS_PICKLIST_VALUE = "In Progress"
    CATEGORY_PICKLIST_VALUE = "General Question"
    RELATES_TO_PICKLIST_VALUE = "dima edunov"

class HelpdeskRightSliderElements():

    @staticmethod
    def insert_value_to_field(driver, field_name):

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                   "//div[contains(label,'%s')]//following-sibling::mat-form-field//input" % field_name)))


        return driver.find_element(By.XPATH,"//div[contains(label,'%s')]//following-sibling::mat-form-field//input" % field_name)


    @staticmethod
    def insert_value_to_picklist(driver, pick_list_name, value_name):
        time.sleep(2)
        driver.find_element(By.XPATH, "//nice-select[@id='%s']" % pick_list_name).click()
        time.sleep(2)

        pick_list = driver.find_element(By.XPATH, "//nice-select[@id='%s']//span[text()='%s']" % (pick_list_name, value_name))

        time.sleep(5)
        return pick_list


    @staticmethod
    def choose_item_from_relates_to_picklist(driver, relates_to_value):
        time.sleep(2)

        relates_to_clickable = driver.find_element(By.XPATH, "//span[text()='Related to']")
        relates_to_clickable.click()
        time.sleep(2)

        relates_to = driver.find_element(By.XPATH, "//span[contains(text(),' Relates To ')]//following-sibling::div//input")
        relates_to.send_keys(relates_to_value)
        time.sleep(2)
        return driver.find_elements(By.XPATH,"//*[@class='input-wrap open']//*[@class='options-list ng-star-inserted']")[0]
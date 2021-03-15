from datetime import *
import time
from enum import Enum
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class MyDashboardConstants(Enum):
    """Constants of My Dashboard module they used to find right column and right value in the column"""
    # Columns names
    EVENT_TYPE_TAB = "Event Type"
    STATUS_TAB = "Status"

    # Value in column
    EVENT_TYPE_VALUE = "2"
    STATUS_VALUE = "4"



class MyDashboardElements():

    @staticmethod
    def choose_date_of_birth(driver, year, month, day):
        # Open calendar
        date_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//input[@placeholder='Choose date of birth']")))

        driver.execute_script("arguments[0].click();", date_field)

        # Click on current date
        current_date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "(//span[@class='mat-button-wrapper' and contains(text(),'2020')])[1]")))

        current_date.click()

        previous_year_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "(//button[@class='mat-calendar-previous-button mat-icon-button mat-button-base'])[1]")))

        previous_year_button.click()
        time.sleep(0.5)
        previous_year_button.click()

        select_year = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(text(),'%s')]" % year)))

        select_year.click()

        select_month = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(text(),'%s')]" % month)))

        select_month.click()

        select_day = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(text(),'%s')]" % day)))

        select_day.click()

        set_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[text()='Set'])[1]")))

        set_btn.click()

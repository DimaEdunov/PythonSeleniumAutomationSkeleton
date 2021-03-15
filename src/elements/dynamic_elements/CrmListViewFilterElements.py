from enum import Enum
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Filters(Enum):
    # Client Module Enums
    FILTER_TEST = "Test"
    FILTER_TEST_FINANCIAL = "Test Financial Auto []"
    FILTER_ALL = "All"
    FILTER_SORTING_FILTER = "Sorting Filter"
    FILTER_NEW = "New"


class FilterElements(object):

    @staticmethod
    def filter_choose_element(driver, filter_name):

        # Old filter elements - From Sunday the 28.06.20 is DEPRICATED. Currently still set for QA ENVs
        if len(driver.find_elements(By.XPATH,
                                    "//nice-select[@searchplaceholder='Search filter']//span[@class='placeholder']")) > 0:
            driver.find_element(By.XPATH,
                                "//nice-select[@searchplaceholder='Search filter']//span[@class='placeholder']").click()


        elif len(driver.find_elements(By.XPATH,
                                      "//custom-view//div[@class='cv-search']//span[@class='placeholder']")) > 0:

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//custom-view//div[@class='cv-search']//span[@class='placeholder']"))).click()

        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@class='input-wrap open']//input").clear()

        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@class='input-wrap open']//input").send_keys(filter_name)

        time.sleep(2)
        return driver.find_element(By.XPATH,
                                   "//*[@class='input-wrap open']//ul//li//a[contains(@title, '%s')]" % filter_name)

    @staticmethod
    def filter_tab_choose_element(driver, tab_name):

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//custom-view//button/span[text()=' %s ']" % tab_name))).click()
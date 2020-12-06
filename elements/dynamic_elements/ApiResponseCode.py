import time
from enum import Enum
from selenium.webdriver.support.wait import WebDriverWait
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ApiAction(Enum):
    CREATE_CUSTOMER_RESPONSE = "//*[@id='api-Customers-createCustomer-0.0.0']/form/fieldset/div[5]/pre/code"
    UPDATE_CUSTOMER_RESPONSE = "//*[@id='api-Customers-updateCustomer-0.0.0']/form/fieldset/div[5]/pre/code"
    READ_CUSTOMER_RESPONSE = "//*[@id='api-Customers-readCustomer-0.0.0']/form/fieldset/div[5]/pre/code"
    READ_CUSTOMERS_RESPONSE = "//*[@id='api-Customers-readCustomers-0.0.0']/form/fieldset/div[5]/pre/code"
    READ_LEADS_RESPONSE = "//*[@id='api-Leads-readLeads-0.0.0']/form/fieldset/div[5]/pre/code"
    CREATE_LEAD_RESPONSE = "//*[@id='api-Leads-Leads-0.0.0']/form/fieldset/div[5]/pre/code"


class ApiResponse():

    @staticmethod
    def api_response_code(driver, response_element):
        driver.execute_script("arguments[0].scrollIntoView();", WebDriverWait(driver, timeout=25).until(
                                  EC.presence_of_element_located((By.XPATH, response_element))))

        print("DEBUG | RESPONSE is " + driver.find_element(By.XPATH, response_element).text)
        response = driver.find_element(By.XPATH, response_element).text
        return response

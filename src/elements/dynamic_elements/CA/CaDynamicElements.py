from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CaDynamicElementsConstants(Enum):
    # SIGN UP POPUP ELEMENTS
    FIRST_NAME_INPUT = "firstName"
    LAST_NAME_INPUT = "lastName"
    SIGN_UP_EMAIL_INPUT = "email"
    PHONE_INPUT = "phone"
    SIGN_UP_PASSWORD_INPUT = "password"
    SIGN_UP_CONFIRM_PASSWORD_INPUT = "passwordConfirm"
    COUNTRY_NAME_SEARCH = "countrySearch"

    # LOG IN POPUP ELEMENTS
    LOGIN_EMAIL_INPUT = "login"
    LOGIN_PASSWORD_INPUT = "password"


class CaDynamicElementsActions():

    @staticmethod
    def ca_input(driver, ca_input):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@name='%s']" % ca_input)))

        return driver.find_element(By.XPATH,
                                   "//input[@name='%s']" % ca_input)
import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver", "brand")
class Test_Maintenance_DeleteFilters():


        @allure.feature('Maintenese')
        @allure.story('Delete filters')
        @pytest.mark.run(order=1)
        def test_delete_all_filters(self, driver, brand):

            # Navigate to wanted module manually
            print("WAIT!")
            time.sleep(15)


            # This for lop runs 3,000 times, and delets filters
            x=0
            while x<3000:
                # Find filter element
                if len(driver.find_elements(By.XPATH,
                                            "//nice-select[@searchplaceholder='Search filter']//span[@class='placeholder']")) > 0:
                    driver.find_element(By.XPATH,
                                        "//nice-select[@searchplaceholder='Search filter']//span[@class='placeholder']").click()


                elif len(driver.find_elements(By.XPATH,
                                              "//custom-view//div[@class='cv-search']//span[@class='placeholder']")) > 0:


                    driver.find_element(By.XPATH,
                                            "//custom-view//div[@class='cv-search']//span[@class='placeholder']").click()

                print("FILTER MENU OPENED")
                time.sleep(4)

                # Delete filter, last in the list of displayed filters
                print("Length " +str(len(driver.find_elements(By.XPATH, "//*[@class='actions-wrap ng-star-inserted']/ul[@class='actions-menu']//button[@title='Delete']"))))
                delete_btn = driver.find_elements(By.XPATH, "//*[@class='actions-wrap ng-star-inserted']/ul[@class='actions-menu']//button[@title='Delete']")[-1]
                driver.execute_script("arguments[0].click();", delete_btn)

                time.sleep(2)

                delete_btn = driver.find_element(By.XPATH,
                    "//div[contains(@class,'mat-dialog-actions')]/button/span[text()=' Delete ']")
                delete_btn.click()

                time.sleep(2)

                # Click on 'OK' button
                button = driver.find_element(By.XPATH,"//*[text()=' OK ']")
                driver.execute_script("arguments[0].click();", button)

                time.sleep(2)

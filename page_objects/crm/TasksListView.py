from datetime import *
import vobject as vobject
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from src.elements.CrmElements import CrmElements
from src.elements.dynamic_elements.CrmRightSliderFieldElements import RightSliderElements, RightSliderConstants
from src.elements.dynamic_elements.CrmSideMenuElements import Modules, CrmSideMenu
from src.elements.dynamic_elements.CrmListViewTableActionsMenuElements import *
from src.elements.dynamic_elements.CrmListViewTableElements import *


class TasksListView():

    def __init__(self, driver):
        self.driver = driver

    @allure.step("TaskListView.go_to() | Navigating to Tasks")
    def go_to(self):
        # Navigating to Tasks module screen
        CrmSideMenu.side_menu_items(self.driver, Modules.TASKS_MODULE.value).click()

        time.sleep(6)

    @allure.step("TaskListView.create_task() | Create a new task")
    def create_task(self, event_type):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ADD_EVENT_BUTTON))).click()

        assign_to_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                RightSliderConstants.ASSIGN_TO_NAME_OF_PICKLIST.value,
                                                                                                RightSliderConstants.ASSIGN_TO_PICKLIST_VALUE.value)
        self.driver.execute_script("arguments[0].click();", assign_to_pick_list)

        global event_type_pick_list
        # Choose event type
        if event_type == "Call":

            event_type_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                     RightSliderConstants.EVENT_TYPE_PICKLIST.value,
                                                                                                     RightSliderConstants.CALL_VALUE.value)
            self.driver.execute_script("arguments[0].click();", event_type_pick_list)

        elif event_type == "Meeting":

            event_type_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                     RightSliderConstants.EVENT_TYPE_PICKLIST.value,
                                                                                                     RightSliderConstants.MEETING_VALUE.value)
            self.driver.execute_script("arguments[0].click();", event_type_pick_list)



        time.sleep(1)

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.SUBJECT_FIELD.value).send_keys(
            "subject qa")

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.RIGHT_SLIDER_COMMENTS_FIELD))).send_keys("comments qa")

        time.sleep(1)
        attached_to_pick_list_item = RightSliderElements.choose_item_by_value_out_of_attached_to_picklist(self.driver,
                                                                                                          RightSliderConstants.ATTACHED_TO_PICKLIST.value,
                                                                                                          RightSliderConstants.ATTACHED_TO_PICKLIST_VALUE.value)

        # Must use the following loop, as part of names from picklist do not have values and are not clicked,
        # Randomly, and different on each bran
        counter = 0
        for name_item in attached_to_pick_list_item:
            if "dima" in name_item.text:
                self.driver.execute_script("arguments[0].click();", attached_to_pick_list_item[counter])
                break
            counter += 1

        time.sleep(2)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SAVE_BUTTON))).click()

        time.sleep(1)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    @allure.step("TaskListView.mass_edit() | Tasks - Mass Edit")
    def mass_edit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SELECT_ALL_ITEMS_BUTTON))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.MASS_EDIT_BUTTON))).click()

        time.sleep(1)

        # Select 'Status' checkbox / Select 'Status' value
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.STATUS_CHECKBOX))).click()

        status_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                             RightSliderConstants.STATUS_NAME_OF_PICKLIST.value,
                                                                                             RightSliderConstants.TASK_STATUS_VALUE.value)
        self.driver.execute_script("arguments[0].click();", status_pick_list)

        # Select 'Event Type' checkbox / Select 'Event Type' value

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.EVENT_TYPE_CHECKBOX))).click()

        event_type_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                                 RightSliderConstants.EVENT_TYPE_PICKLIST.value,
                                                                                                 RightSliderConstants.MEETING_VALUE.value)
        self.driver.execute_script("arguments[0].click();", event_type_pick_list)

        # Save changes
        print("BEFORE spinner : " + str(datetime.now().strftime('%H%M%S')))
        WebDriverWait(self.driver, 50).until(
            EC.invisibility_of_element_located((By.XPATH, CrmElements.LOADING_SPINNER)))
        print("AFTER spinner : " + str(datetime.now().strftime('%H%M%S')))

        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SAVE_CHANGES_BUTTON))).click()

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    @allure.step("TaskListView.mass_edit_verification() | Verify results after performing Mass Edit Tasks")
    def mass_edit_verification(self):
        time.sleep(1)
        # Hover the actions menu of the last event.
        ListViewActionsMenu.hover_more_button(self.driver, 'last()')
        ListViewActionsMenu.choose_actions_menu_item(self.driver, 'last()', ActionsConstants.EDIT_ACTION.value)

        if RightSliderElements.field_value(self.driver, RightSliderConstants.STATUS_NAME_OF_PICKLIST.value).text == \
                RightSliderConstants.TASK_STATUS_VALUE.value \
                and RightSliderElements.field_value(self.driver, RightSliderConstants.EVENT_TYPE_PICKLIST.value).text == \
                RightSliderConstants.MEETING_VALUE.value:

            print("DEBUG - Verification passed")
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, CrmElements.CANCEL_BUTTON))).click()

        else:
            print("DEBUG - Verification failed")
            assert False



    @allure.step("TaskListView.edit_event() | Tasks - Edit Event")
    def edit_event(self):

        # Hover the actions menu of the last event.
        ListViewActionsMenu.hover_more_button(self.driver, 'last()')
        time.sleep(1)
        ListViewActionsMenu.choose_actions_menu_item(self.driver, 'last()', ActionsConstants.EDIT_ACTION.value)

        # Change 'Status' value
        status_pick_list = RightSliderElements.choose_item_by_value_out_of_specific_picklist(self.driver,
                                                                                             RightSliderConstants.STATUS_NAME_OF_PICKLIST.value,
                                                                                             RightSliderConstants.TASK_STATUS_VALUE.value)
        self.driver.execute_script("arguments[0].click();", status_pick_list)

        # Change 'Subject' value

        time.sleep(4)

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.SUBJECT_FIELD.value).clear()

        time.sleep(2)

        RightSliderElements.insert_value_to_field(self.driver, RightSliderConstants.SUBJECT_FIELD.value).send_keys(
            "QA_TEST edit event")

        # Save changes
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SAVE_BUTTON))).click()

        time.sleep(1)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    @allure.step("TaskListView.edit_event_verification() | Verify results after performing 'Tasks - Edit Event'")
    def edit_event_verification(self):

        if ColumnElements.get_cell_element_by_column_name(self.driver, 'last()', RightSliderConstants.STATUS_NAME_OF_PICKLIST.value).text\
                == RightSliderConstants.TASK_STATUS_VALUE.value\
                and ColumnElements.get_cell_element_by_column_name(self.driver, 'last()', RightSliderConstants.SUBJECT_FIELD.value).text\
                == "QA_TEST edit event":

            print("DEBUG - Verification passed")

        else:
            print("DEBUG - Verification failed")
            assert False


    @allure.step("TaskListView.delete_event() | Tasks - Delete Event")
    def delete_event(self):
        # Hover the actions menu of the last event.
        ListViewActionsMenu.hover_more_button(self.driver, 'last()')
        time.sleep(1)
        ListViewActionsMenu.choose_actions_menu_item(self.driver, 'last()', ActionsConstants.DELETE_ACTION.value)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, CrmElements.DELETE_BUTTON))).click()

        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    @allure.step("TaskListView.delete_event() | Tasks - Delete Event Verification")
    def delete_event_verification(self):

        time.sleep(2)
        if self.driver.find_element(By.XPATH, CrmElements.NO_RESULTS_TEXT_LIST_VIEW).is_displayed:
            print("DEBUG - Verification passed")

        else:
            print("DEBUG - Verification failed")
            assert False

    @allure.step("TaskListView.mass_delete() | Tasks - Mass Delete")
    def mass_delete(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.SELECT_ALL_ITEMS_BUTTON))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.MASS_DELETE_BUTTON))).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, CrmElements.DELETE_BUTTON))).click()

        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, CrmElements.OK_BUTTON))).click()

    def export_selected_record_iCal(self):

        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.REFRESH_BUTTON))).click()
        print("Refresh clicked")

        event_subject = ColumnElements.get_cell_element_by_column_name(self.driver, 1, Columns.SUBJECT.value).text
        start_date = ColumnElements.get_cell_element_by_column_name(self.driver, 1, Columns.START_DATE.value).text

        test_data = [event_subject, start_date]

        ColumnElements.select_record_via_checkbox_by_row_number(self.driver, 1)
        print("checkbox clicked")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.TOP_EXPORT_BUTTON))).click()

        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.ICAL_CHECKBOX))).click()
        print("iCal clicked")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CrmElements.EXPORT_CONFIRM_BUTTON))).click()

        time.sleep(5)

        return test_data

    def export_iCal_verification(self, test_data):
        crm_event_subject = test_data[0]
        print("crm_event_subject: " + crm_event_subject)

        # Parse the date from the string, convert the date into "%Y-%m-%d" format.
        # Once AC-15091 is fixed needs to change the line into => crm_start_date = test_data[1]
        crm_start_date = str(datetime.strptime(test_data[1], "%Y-%m-%d %H:%M").strftime("%Y-%m-%d"))
        print("crm_start_date: " + crm_start_date)

        with open('C:\web-automation-downloads\\tasks.ics', 'rt') as file_ical:
            data = file_ical.read()
            calendar = vobject.readOne(data)
            export_event_subject = calendar.vevent.summary.valueRepr()
            print("export_event_subject: " + export_event_subject)

            #  Once AC-15091 is fixed, needs to change the date format into "%Y-%m-%d %H:%M".
            export_start_date = str(calendar.vevent.dtstart.value.strftime("%Y-%m-%d"))
            print("export_start_date: " + export_start_date)

        if crm_event_subject == export_event_subject and crm_start_date == export_start_date:
            print("Verification Passed")

        else:
            print("DEBUG - Verification failed")
            assert False
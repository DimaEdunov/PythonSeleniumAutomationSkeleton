# All the following elements, are based on XPATH syntax identification
class CrmElements():

    # Cross module elements
    SPINNER = "//mat-spinner"
    DETAILS_VIEW_MAIN_EDIT_BUTTON = "//div[@class='wrap-navigation d-flex align-items-center']//button[span[i[contains(@class,'pencil')]]]"
    WORKFLOWS_MODULE = "//*[contains(text(),' Workflows ')]"
    SHOW_RECORDS_BUTTON = "//button[contains(text(),'show records')]"
    ACC_GENERAL_SELECTOR = "//span[contains(span,'ACC')]"
    REFRESH_BUTTON = "//span[contains(text(), 'Refresh')]"

    DETAILS_VIEW_FIELD_PENCIL_BUTTON = "//div[label='%s']//following-sibling::button//i[contains(@class,'pencil')]"
    DETAILS_VIEW_LIST_FIRST_ITEM = "(//div[label='%s']//following-sibling::div[@class='picklist-select']//span[text()])[2]"
    DETAILS_VIEW_LIST_ITEM = "//div[label='%s']//following-sibling::div[@class='picklist-select']//span[text()='%s']"
    DETAILS_VIEW_CONFIRM_BUTTON = "//div[label='%s']//following-sibling::*//field-confirm//div[@class='button-confirm']"
    DETAILS_VIEW_TAB = "//mat-expansion-panel-header[@aria-expanded='false']//mat-panel-title/div[contains(text(),'%s')]"
    DETAILS_VIEW_FIELD_VALUE = "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-txt-wrapper')]|//div[label='%s']//following-sibling::div//div[@class and text()]"
    MODULE_IFRAME = "//iframe[@name='tradeChartFrame']"
    DETAILS_VIEW_EDIT_BUTTON = "//div[@class='wrap-navigation d-flex align-items-center']//button[span[i[contains(@class,'pencil')]]]"
    LIST_VIEW_APPLY_BUTTON = "//button[contains(span,'Apply')]"
    RECORDS_COUNTER = "//div[contains(@class,'mat-paginator')]//span[contains(@class,'total-records')]"

    SIDE_MENU_WAIT_VERIFICATION_ELEMENT = "//div[@class='nav-menu']//a[contains(text(), 'Clients')]"
    SIDE_MENU_SETTINGS = "//div[@class='nav-menu']//*[@title='Settings']"
    CLOSE_GLOBAL_SEARCH_X_BUTTON ="//mat-sidenav[1]//button//span"
    NO_RESULTS_TEXT_LIST_VIEW = "//span[@class='no-results-text']"

    # Searchbar - Cross module elements
    FILTER_AGREE_BUTTON = "//span[contains(text(),'Apply')]"
    LISTVIEW_FIRST_ROW_CELL_ITEMS_LIST = "//tbody[@role='rowgroup']/tr[@role='row' and not (contains(@style,'hidden'))][1]/td"
    MORE_BUTTON = "//mat-icon[text()='more_vert'][1]"
    BIN_BUTTON = "//mat-icon[text()='delete'][1]"
    DELETE_BUTTON = "//button[span=' Delete ']"
    TEST_EMAIL_IN_SEARCH_BAR = "//div//tr[2]/td[6]/div/span[contains(text(), '@test')]"


    # Global Search - Cross module elements
    TEST_EMAIL_IN_GLOBAL_SEARCH = "//*[@class='mat-expansion-panel-content ng-trigger ng-trigger-bodyExpansion']//tbody//span"
    TEST_NAME_IN_GLOBAL_SEARCH = "//*[@class='mat-expansion-panel-content ng-trigger ng-trigger-bodyExpansion']//a//i"

    # Side-menu, name of user
    SIDE_MENU_USER_NAME_ITEM = "//div[@class='content-menu']//*[@class='user-info']"
    SIDE_MENU_SIGN_OUT = "//div[@class='content-menu']//*[@title='Sign Out']"
    SIDE_MENU_SIGN_OUT_YES_BUTTON = "//span[text()=' Yes ']"

    # Initial Sign-in screen
    NEW_SIGN_IN_USER_NAME_FIELD = "//input[@formcontrolname='userName']"
    NEW_SIGN_IN_PASSWORD_FIELD = "//input[@formcontrolname='password']"
    NEW_SIGN_IN_SUBMIT_BUTTON = "//button[@id='submit-btn']"

    OLD_SIGN_IN_USER_NAME_FIELD = "//*[@name='user_name']"
    OLD_SIGN_IN_PASSWORD_FIELD = "//*[@name='user_password']"
    NEW_UI_OLD_SIGN_IN_CHECKBOX = "//*[@id='new-ui-selected']"
    OLD_SIGN_IN_SUBMIT_BUTTON = "//*[@id='submitButton']"

    # Side-menu
    SIDE_MENU_SEARCH = "//side-menu//input[@placeholder='Search']"
    SIDE_MENU_MAGNIFYING_GLASS = "//side-menu//i[@class='mdi mdi-magnify']"
    SIDE_MENU_TASKS = "//*[@title='Tasks']"
    SIDE_MENU_LEADS = "//*[@title='Leads']"
    SIDE_MENU_CLIENTS = "//*[@title='Clients']"
    SIDE_MENU_TRADING_ACCOUNTS = "//*[@title='Trading Accounts']"
    SIDE_MENU_FINENCIAL_TRANSACTIONS = "//*[@title='Financial Transactions']"
    SIDE_MENU_SETTINGS = "//*[@title='Settings']"
    SIDE_MENU_EMAIL_MAKER = "//*[@title='EMAIL Maker']"
    SIDE_MENU_AUDIT_LOGS = "//*[@title='Audit Logs']"
    SIDE_MENU_AUTO_ASSIGN = "//*[@title='AutoAssign']"
    SIDE_MENU_TRADES = "//*[@title='Trades']"
    SIDE_MENU_SMS_NOTIFIER = "//*[@title='SMSNotifier']"
    SIDE_MENU_RECYCLE_BIN = "//*[@title='Recycle Bin']"
    SIDE_MENU_EMAIL = "//*[@title='Email']"
    SIDE_MENU_DOCUMENTS = "//*[@title='Documents']"
    SIDE_MENU_PERMISSION_HELPER = "//*[@title='Permission Helper']"
    SIDE_MENU_MY_DASHBOARD = "//*[@title='My Dashboard']"
    SIDE_MENU_PANDA_REPORTS = "//*[@title='Panda Reports']"
    SIDE_MENU_LEADER_BOARD = "//*[@title='Leader Board']"
    SIDE_MENU_AFFILIATES = "//*[@title='Affiliates']"
    SIDE_MENU_CAMPAIGNS = "//*[@title='Campaigns']"
    SIDE_MENU_HELP_DESK = "//*[@title='Help Desk']"

    #Affiliates (Main screen)
    AFFILIATES_API_LINK = "//a[@target='_blank']"
    FILTER_COPY_CONTENT_BUTTON = "//*[@class='mdi mdi-content-copy']"
    AFFILIATES_PARTNER_ID_TEXT = "//*[@class='d-flex align-items-center']//*[contains(@class,'td-text ng-tns')]"
    AFFILIATES_EXPORT_BUTTON = "//button[@title='Export Affiliates']"

    #Clients List View
    CRM_ID_LIST = "//tbody/tr[@role='row' and not(contains(@style,'hidden'))]//span[contains(text(),'ACC')]"
    CRM_EMAIL_LIST = "//list-view/pnd-grid//table/tbody/tr[2]/td[5]/div/span"

    # Clients Details View
    EDIT_CLIENT_SAVE_BUTTON = "//mat-sidenav//button[span=' Save ']"
    UPDATE_MT_ACCOUNT_BUTTON = "//span[contains(text(),'Update')]"
    TRADING_ACCOUNTS_ACTIONS_OPEN_MENU = "//*[@class='mat-content']//*[contains(text(),' Trading Accounts Actions ')]"
    TRADING_ACCOUNTS_DEMO_ACCOUNT_VERIFICATION = "//*[@id='trading-accounts']//*[@class='mat-table']//span[contains(text(),'Demo')]"
    TRADING_ACCOUNTS_LIVE_ACCOUNT_VERIFICATION = "//*[@id='trading-accounts']//*[@class='mat-table']//span[contains(text(),'Live')]"
    FINANCIAL_TRANSACTIONS_DEPOSIT_VERIFICATION = "//*[@id='financial-transactions']//*[@class='mat-table']//span[contains(text(),'0.75')]"
    FINANCIAL_TRANSACTIONS_WITHDRAW_VERIFICATION = "//*[@id='financial-transactions']//*[@class='mat-table']//span[contains(text(),'0.25')]"
    FINANCIAL_TRANSACTIONS_TRANSFER_BETWEEN_TA_VERIFICATION = "//*[@id='financial-transactions']//*[@class='mat-table']//span[contains(text(),'0.1')]"
    FINANCIAL_TRANSACTIONS_CREDIT_IN_VERIFICATION = "//*[@id='financial-transactions']//div[contains(span,'Credit in')]//parent::*//following-sibling::*//span[contains(text(),'0.55')]"
    FINANCIAL_TRANSACTIONS_CREDIT_OUT_VERIFICATION = "//*[@id='financial-transactions']//div[contains(span,'Credit out')]//parent::*//following-sibling::*//span[contains(text(),'0.31')]"
    UPDATE_MT_ACCOUNT_READ_ONLY_CHECKBOX = "//span[contains(text(),'Read only')]//preceding-sibling::*//label"

    ADD_INTERACTION_BUTTON = "//button[@title='Add Interaction']"

    ACTIVITIES_VERIFICATION = "//mat-expansion-panel[@id='activities']//div[@class='d-flex align-items-center']"
    INVALID_PHONE_ICON = "//img[@class='hone-icon ng-star-inserted']"
    CLIENT_DETAILS_VIEW_SUBJECT_FIELD = "//td[@style='min-width: auto;'][2]"
    CLIENT_DETAILS_VIEW_LEVERAGE_FIELD = "//mat-expansion-panel[@id='trading-accounts']//tr[@role='row' and not(contains(@style,'hidden'))][1]//td[@style='min-width: auto;'][9]"
    CLIENT_DETAILS_VIEW_READ_ONLY_FIELD = "//mat-expansion-panel[@id='trading-accounts']//tr[@role='row' and not(contains(@style,'hidden'))][1]//td[@style='min-width: auto;'][12]"

    #Leads List View
    CREATE_LEAD_BUTTON = "//button[@title='Create new']"
    LEAD_ID_LIST = "//tbody/tr[@role='row' and not(contains(@style,'hidden'))]//span[contains(text(),'LEA')]"
    LEAD_EMAIL_LIST = "//mat-sidenav-content//list-view//tbody/tr[2]/td[6]/div/span"

    # Leads Details View
    LEAD_NO = "(//div[contains(@class,'value-string')])[1]"
    LEADS_RIGHT_SLIDER_UI_LANGUAGE_PLACEHOLDER = "//span[contains(text(),' UI Language  ')]"


    CONVERT_LEAD_BUTTON = "//mat-sidenav//button[span=' Convert lead ']"
    CONVERT_LEAD_BUTTON_ORANGE = "//detail-header//button[@class='btn convert-lead-button']"
    CLIENT_EXIST_CLICKABLE_VALUE = "//div[label='Client Exist']//following-sibling::a"

    # Clients details view
    LEAD_EXIST_FIELD_VALUE = "//detail-view-internal//a/span"
    CREATE_NEW_DOCUMENT_BUTTON = "//create-new//button"


    # Right slider screen - General
    RIGHT_SLIDER_CREATE_LEAD_BUTTON = "//mat-sidenav//button[span=' Create lead ']"
    OK_BUTTON = "//button[span=' OK ']"
    UPDATE_LEAD_BUTTON = "//mat-sidenav//button[span=' Update lead ']"
    SAVE_CHANGES_BUTTON = "//mat-sidenav//button[span=' Save changes ']"
    SAVE_BUTTON = "//mat-sidenav//button[span=' Save ']"
    ASSIGN_BUTTON = "//mat-sidenav//button[span=' Assign ']"
    CANCEL_BUTTON = "//mat-sidenav//button[span=' Cancel ']"

    RIGHT_SLIDER_DATE_FIELD = "//input[@placeholder='Choose date of birth']"
    RIGHT_SLIDER_CURRENT_DATE_BUTTON = "(//span[@class='mat-button-wrapper' and contains(text(),'2020')])[1]"
    RIGHT_SLIDER_PREVIOUS_BUTTON = "(//button[@class='mat-calendar-previous-button mat-icon-button mat-button-base'])[1]"
    RIGHT_SLIDER_YEAR_VALUE = "//div[contains(text(),'1971')]"
    RIGHT_SLIDER_MONTH_VALUE = "//div[contains(text(),'JAN')]"
    RIGHT_SLIDER_DAY_VALUE = "(//div[contains(text(),'1')])[1]"
    RIGHT_SLIDER_SET_BUTTON = "(//span[text()='Set'])[1]"

    # Right slider screen - Client details view - MT Menu
    RIGHT_SLIDER_CREATE_BUTTON = "//span[text()=' Create ']"
    DEPOSIT_BUTTON = "//mat-sidenav//button[span=' Deposit ']"
    WITHDRAW_BUTTON = "//mat-sidenav//button[span=' Withdraw ']"
    TRANSFER_BUTTON = "//mat-sidenav//button[span=' Transfer ']"
    CHANGE_PASSWORD_FIELD = "//mat-sidenav//input[@formcontrolname='changePassword']"
    CHECK_PASSWORD_FIELD = "//mat-sidenav//input[@formcontrolname='checkPassword']"
    CHANGE_PASSWORD_BUTTON = "//button[@appearance='outline']//span[contains(text(),'Change')]"
    CHECK_PASSWORD_BUTTON = "//button[@appearance='outline']//span[contains(text(),'Check')]"
    CREDIT_IN_BUTTON = "//mat-sidenav//button[span=' Credit in ']"
    CREDIT_OUT_BUTTON = "//mat-sidenav//button[span=' Credit out ']"


    CHANGE_PASSWORD_MT_ACCOUNT_FIELD = "//input[@formcontrolname='changePassword']"
    CHANGE_PASSWORD_MT_ACCOUNT_BUTTON = "(//button[@appearance='outline'])[2]"

    CHECK_PASSWORD_MT_ACCOUNT_FIELD= "//input[@formcontrolname='checkPassword']"
    CHECK_PASSWORD_MT_ACCOUNT_BUTTON = "(//button[@appearance='outline'])[2]"

    CHANGE_CHECK_MT_PASSWORD_SELECT_TRADING_ACCOUNT_CHECKLIST_BOX = "//span[contains(text(),' Select trading Account  ')]//following-sibling::div"
    CHANGE_CHECK_MT_PASSWORD_SELECT_FIRST_ACCOUNT_IN_PICKLIST = "(//form//ul//li//a)[1]"

    # Client / Leads Listview -> Mass edit
    MASS_EDIT_BUTTON = "//div[contains(@class,'mass-actions')]/button/span[contains(text(),'Mass Edit')]"
    MASS_ASSIGN_BUTTON = "//div[contains(@class,'mass-actions')]/button/span[contains(text(),'Mass Assign')]"
    SELECT_ALL_ITEMS_BUTTON = "//th[@role='columnheader']//label[@class='mat-checkbox-layout']"
    ASSIGNED_TO_CHECKBOX = "//div[h3=' Choose fields to edit: ']//span[contains(text(),'Assigned To')]"
    LANGUAGE_CHECKBOX = "//div[h3=' Choose fields to edit: ']//span[contains(text(),'Language')]"
    STATUS_CHECKBOX ="//div[h3=' Choose fields to edit: ']//span[contains(text(),'Status')]"
    CLIENT_SOURCE_CHECKBOX ="//div[h3=' Choose fields to edit: ']//span[contains(text(),'Client Source')]"
    USER_NAME_ASSIGN_TO = "//div[label='Users']//following-sibling::div[@class='options-wrap ng-star-inserted']//span[contains(text(),'%s')]"

    # Help desk Listview
    CREATE_NEW_TICKET_BUTTON = "//button[@title='Create new']"
    CREATE_NEW_TICKET_SUBMIT_BUTTON = "//mat-sidenav//span[text()='Create ticket']"
    EDIT_TICKET_TICKET_SUBMIT_BUTTON = "//mat-sidenav//span[text()='Edit ticket']"
    RELATES_TO_FIELD = "//span[contains(text(),' Relates To ')]//following-sibling::div//input" # Exceptional
    HELP_DESK_ID = "//tbody/tr[@role='row' and not(contains(@style,'hidden'))]//span[contains(text(),'TT')]"

    # Global search
    X_CLOSE_BUTTON = "//div[@class='sidenav-head-container d-flex']//button//span"


    # My Dashboard Listview
    SHOW_MINE_BUTTON = "//*[@id='main-tabs']/li[text()=' Show mine ']"
    SHOW_ALL_BUTTON = "//*[@id='main-tabs']/li[text()=' Show all ']"
    LOADING_SPINNER = "//div[@class='spinner']"
    PENCIL_ICON = "//span[@class='glyphicon glyphicon-pencil cursor-pointer ng-star-inserted']"
    ADDITIONAL_ACTIONS_BUTTON = "//bs-modal[8]//div[1]/a"
    STATUS_ADDITIONAL_ACTIONS = "//select[@id='statusname']"
    NEW_STATUS_ADDITIONAL_ACTIONS_FIRST_OPTION = "//*[@id='statusname']/option[5]"
    NEW_STATUS_ADDITIONAL_ACTIONS_SECOND_OPTION = "//*[@id='statusname']/option[3]"
    CHANGE_ADDITIONAL_STATUS_BUTTON = "//account-mini-control//div[2]//button[@class='btn btn-primary']"
    EDIT_TICKET_SAVE_BUTTON = "//bs-modal[8]//div[2]//div[2]/div/div[3]/button"
    CHECK_STATUS_OF_USER = "//tasks-list//div[2]//div[1]//tbody/tr[2]/td[7]/grid-cell//span[2]"

    # Affiliates - add new affiliate screen
    CREATE_NEW_AFFILIATE_BUTTON = "//span[contains(text(),' Add new affiliate ')]"
    SHOW_LIMITE_FIELDS_BUTTON = "//*[@class='limit-fields-open ng-star-inserted']"
    ADD_BUTTON = "//span[text()='Add ']"
    ALLOWED_IP_FIELD = "//input[@formcontrolname='allowedIp']" #Exceptional field

    # Tasks - listview & DetailsView
    ADD_EVENT_BUTTON = "//span[text()=' Add Event ']"
    RIGHT_SLIDER_COMMENTS_FIELD = "//*[@id='comments']"
    EVENT_TYPE_CHECKBOX = "//div[h3=' Choose fields to edit: ']//span[contains(text(),'Event Type')]"
    EVENT_DURATION_CHECKBOX = "//div[h3=' Choose fields to edit: ']//span[contains(text(),'Event Duration')]"
    ATTACHED_TO_PICKLIST_ITEM = "//span[text()=' Attached To  ']//following-sibling::div/span"

    # Financial Transaction
    CREATE_NEW_FILTER_BUTTON_SAVE_CHANGES = "//div[@class='sidenav-actions']//button[@color='primary']"
    CREATE_NEW_FILTER_ADD_COLUMN_FIELD = "//span[contains (text(),'Choose or search columns and order')]"
    CREATE_NEW_FILTER_ADD_COLUMN_FIRST_RESULT_ITEM = "//div[@class='input-wrap open']//ul//a"
    CREATE_NEW_FILTER_INPUT_FIELD = "//section[@class='select-list']//input[@autocomplete='off']"
    CREATE_NEW_FILTER_BUTTON = "//button[@title='Create Filter']"



    # Campaign module (Listview + New Campaign
    ADD_NEW_CAMPAIGN_BUTTON = "//body//button[contains(text(),'Add Campaign')]"
    CAMPAIGN_SAVE_BUTTON = "//button[@id='Save']"
    CAMPAIGN_NAME_FIELD = "//input[@name='campaign_name']"
    CAMPAIGN_RATE_FIELD = "//input[@name='deal_value']"
    CAMPAIGN_ASSIGN_TO_FIELD_CLICK = "//span[@dir='ltr']"
    CAMPAIGN_ASSIGN_TO_FIELD = "/html/body/span/span/span[1]/input"
    CAMPAIGN_ASSIGN_TO_RESULTS_LIST = "//li[@role='group']//li"
    CAMPAIGN_LIST_NAME_OF_CAMPAIGN = "(//div[@role='row'])//div//div//a[contains(text(),'automationqa')]"
    CAMPAIGN_DELETE_BUTTON = "//div[@role='row'][1]//div[@title='Delete']"
    CAMPAIGN_DELETE_CONFIRMATION_BUTTON = "//button[contains(text(),'OK')]"
    CAMPAIGN_SEARCH_CAMPAIGN_FIELD = "(//div[@id='filterrow.ListGrid0']//div[3]/preceding-sibling::div[1]//input)[1]"
    INFO_LINK = '//td[@class="moduleName"]//a//following-sibling::a'
    CAMPAIGN_EDIT_BUTTON = "//div[@class='renderer_wrapper']//div[@title='Edit']"


    # Workflow Module List View (Main screen)
    NEW_WORKFLOW_BUTTON = "//span[contains(text(), 'New Workflow')]"
    NEXT_BUTTON = "//span[contains(text(), 'Next')]"
    WORKFLOWS_HEADER = "//h1[contains(text(),'Workflows')]"
    WORKFLOW_LIST_VIEW_NAME_SEARCH_FIELD = "//th[@role='columnheader' and contains(text(),'Name')]//input"
    WORKFLOW_LIST_VIEW_MORE_BUTTON = "//mat-icon[text()='more_vert']"
    WORKFLOW_LIST_VIEW_DELETE_BUTTON = "//mat-icon[text()='delete']"
    WORKFLOW_LIST_VIEW_CONFIRM_DELETE_BUTTON = "//span[text()=' Delete ']"
    WORKFLOW_LIST_VIEW_NO_RESULTS_MESSAGE = "//tr[@class='no-results']/td[text()='No results']"

    # Workflow Schedule
    WORKFLOW_NAME_FIELD = "//input[@id='wf_name']"
    WORKFLOW_PRIORITY_FIELD = "//input[@id='wf_priority']"
    WORKFLOW_EXECUTE_RADIOBUTTON = "//span[text()='Every time the record is modified.']"

    # Workflow Add Conditions
    PICKLIST_MODULE_ITEM = "//div[@class='select-filter']"
    MODULE_SEARCH_FIELD = "//span[@class='filter-search-container']/input[@placeholder='Search...']"
    WORKFLOW_PICKLIST_CHOOSE_MODULE = "//span[@option-value='Accounts']"
    ADD_CONDITION_GROUP_BUTTON = "//button[contains(text(), 'Add Condition Group')]"
    FILTER_CONDITION_LIST = "//div[@class='multi-select-title']/span[contains(text(),'Accept')]"
    CONDITION_LIST_SEARCH_FIELD = "(//span[@class='filter-search-container']/input[@placeholder='Search...'])[2]"
    CLIENT_STATUS_PICK_LIST_VALUE = "//span[text()=' Client Status ']"
    CLIENT_STATUS_SECOND_VALUE = "//select[contains(@class,'condition-value')]/option[2]"
    CONDITION_LIST = "//div[@class='select-wrap']/select[contains(@class,'condition-operator')]"
    CLIENT_STATUS_LIST = "//div[contains(@class,'select-wrap')]/select[contains(@class,'condition-value')]"
    SEARCH_FIELD = "//div[@class='select-options options-enabled']/span[@class='filter-search-container']/input[@placeholder='Search...']"
    COUNTRY_PICK_LIST_VALUE = "(//span[text()=' Country '])[2]"
    CONDITION_SECOND_LIST = "(//div[@class='select-wrap']/select[contains(@class,'condition-operator')])[2]"
    COUNTRY_LIST = "(//div[contains(@class,'select-wrap')]/select[contains(@class,'condition-value')])[2]"
    MID_CONDITION_LIST = "(//div[contains(@class,'select-wrap')]/select[contains(@class,'form-control')])[3]"
    EMAIL_PICK_LIST_VALUE = "(//span[text()=' Email '])[3]"
    THIRD_CONDITION_LIST = "(//div[@class='select-wrap']/select[contains(@class,'condition-operator')])[3]"
    ENTER_EMAIL_BUTTON = "//input[contains(@class,'condition-value')]"
    EMAIL_FIELD = "(//textarea[contains(@class,'form-control')])[3]"
    SAVE_ADD_CONDITION_BUTTON = "(//button[text()='Save '])[3]"
    MID_CONDITION_LIST_2 = "(//div[contains(@class,'select-wrap')]/select[contains(@class,'form-control')])[6]"

    # Workflow Add Tasks
    ADD_TASK_LIST = "//span[text()='Add Task']"
    UPDATE_FIELD_ITEM = "//span[text()='Update Field']"
    TASK_TITLE_FIELD = "//input[@placeholder='Task Title']"
    ADD_FIELD_BUTTON = "//button/b[contains(text(), 'Add Field')]"
    SELECT_FIELD_LIST = "//span[text()='Select field']"
    TASK_SEARCH_FIELD = "//span/input[@placeholder='Search...']"
    ADDRESS_ITEM = "//span[contains(text(), ' Address ')]"
    ADDRESS_TEXT_FIELD = "//div[@class='col-md-6']/input[contains(@class, 'form-control')]"
    ADDRESS_TEXT_AREA = "//div[@class='row current-value']/textarea"
    SAVE_VALUE_BUTTON = "(//button[text()='Save '])[2]"
    TASK_SEARCH_FIELD2 = "(//span/input[@placeholder='Search...'])[2]"
    TASKS_COUNTRY_PICK_LIST = "//div[@class='col-md-6']/select[contains(@class,'form-control')]"
    SAVE_WORKFLOWS_TASK_BUTTON = "(//button[text()='Save '])[1]"
    SAVE_WORKFLOW_BUTTON = "//span[text()=' Save ']"

    CAMPAIGN_LIST_VIEW_FIRST_ROW = "//*[@role='row'][1]"
    CAMPAIGN_CELL_ITEM_ELEMENT = "//*[@role='gridcell']"
    CAMPAIGN_SEARCHHBAR_IFRAME = "//campaigns//iframe[@name='tradeChartFrame']"

    # User Management module
    USER_MANAGEMENT_IFRAME = "//iframe[contains(@src,'UserManagement')]"
    USER_MANAGEMENT_CRM_USERS_TAB = "//a[contains(text(),'CRM Users')]"
    USER_MANAGEMENT_NEW_USER_BUTTON = "//button[contains(text(),'New User')]"
    USER_MANAGEMENT_USER_NAME_FIELD = "//input[@name='user_name']"
    USER_MANAGEMENT_EMAIL_FIELD = "//input[@name='email1']"
    USER_MANAGEMENT_FIRST_NAME_FIELD = "//input[@name='first_name']"
    USER_MANAGEMENT_ROLE_FIELD = "//input[@name='role_name']"
    USER_MANAGEMENT_SPINNER = "//div[@class ='jqx-grid-load']"
    USER_MANAGEMENT_ROLE_VALUE = "(//a[contains(@id,'user')])[5]"
    USER_MANAGEMENT_PASSWORD_FIELD = "//input[@name='user_password']"
    USER_MANAGEMENT_CONFIRM_PASSWORD_FIELD = "//input[@name='confirm_password']"
    USER_MANAGEMENT_LAST_NAME_FIELD = "//input[@name='last_name']"
    USER_MANAGEMENT_SAVE_BUTTON = "//div[@id='userManagementDialog']//button[contains(text(),'Save')]"
    USER_MANAGEMENT_CLEAR_FILTER_BUTTON = "//button[@id='clearfilteringbutton']/i"
    USER_MANAGEMENT_USER_NAME_SEARCH_FIELD = "//div[@id='row00userManagement']/div[3]/div/input"
    USER_MANAGEMENT_USER_FOUND = "//a[contains(@onclick,'userManagementDialog.loadUser')][contains(text(),'%s')]"
    USER_MANAGEMENT_MORE_BUTTON = "//div[@class='text-center action-buttons-dots']/i"
    USER_MANAGEMENT_LOGIN_AS_BUTTON = "//a[@title='Login As']"
    USER_MANAGEMENT_LOGIN_NAME_VALUE = "//div[@class='user-name']"
    USER_MANAGEMENT_SIGN_OUT_BUTTON = "//div[@class='sign-out']"
    USER_MANAGEMENT_DELETE_ICON = "//a[@title='Delete user']"
    USER_MANAGEMENT_DELETE_BUTTON = "(//button[contains(text(),'Delete')])[1]"
    USER_MANAGEMENT_DELETE_MESSAGE = "//div[contains(text(),'User was deleted')]"
    USER_MANAGEMENT_NO_DATA_MESSAGE = "//span[contains(text(),'No data to display')]"
    USER_MANAGEMENT_DISABLE_OTP_CHECKBOX = "//*[@name='crmuser_details']//input[@id='disable_otp']"

    # Auto Assign module
    CREATE_RULE_BUTTON = "//table//tbody//tr//button[contains(text(),'Add Rule')]"
    RULE_POPUP_LEAD_INPUT_CHECKBOX = "//form//input[@id='leadrule']"
    RULE_POPUP_CLIENT_INPUT_CHECKBOX = "//form//input[@id='clientrule']"
    RULE_POPUP_RULE_NAME_FIELD = "//form//input[@id='rule_name']"
    RULE_POPUP_RULE_TYPE_PICKLIST_BOX = "//select[@name='ruletype']"
    RULE_POPUP_RULE_BRAND_PICKLIST_BOX = "//select[@name='brand_id']"
    RULE_POPUP_RULE_BRAND_PICKLIST_FIRST_ITEM = "//*[@id='brand_id']/option[2]"
    RULE_POPUP_RULE_ASSIGN_TO_USER_CHECKBOX="//div[@class='col-md-12 p-l-0 p-r-0 text-center']//input[@value='1']"
    RULE_POPUP_RULE_ASSIGN_TO_PICKLIST_FIELD = "//*[@id='jqxTreeUsers']/input[1]"
    RULE_POPUP_RULE_ASSIGN_TO_ITEM = "//li[@username='Panda Auto']/div/div/div"
    RULE_POPUP_RULE_COUNTRY_PICKLIST_BOX = "//button[@class='multiselect dropdown-toggle btn btn-default']"
    RULE_POPUP_COUNTRY_SEARCH_FIELD = "//input[@class='form-control multiselect-search']"
    RULE_POPUP_COUNTRY_PICKLIST_CHECKBOX = "//input[@value='multiselect-all']"
    RULE_POPUP_RULE_SUBMIT_BUTTON = "//button[contains(text(),'Submit')]"
    AUTO_ASSIGN_OK_BUTTON = "//button[contains(text(),'OK')]"
    AUTO_ASSIGN_SORT_BY_PRIORITY_BUTTON = "//span[contains(text(),'Priority')]"
    AUTO_ASSIGN_FIRST_RULE_NAME_CELL = "(//div[@role='gridcell'])[2]//div"
    AUTO_ASSIGN_FIRST_RULE_PENCIL_CELL = "(//div[@role='gridcell'])[16]"
    AUTO_ASSIGN_POPUP_RULE_NAME_INPUT_VALUE = "//input[@value='automation_leads_test']"
    AUTO_ASSIGN_DELETE_FIRST_RULE_BUTTON = "(//div[@role='gridcell'])[17]//div"


    # Dragon
    LISTVIEW_VALID_PHONE_ICON_FIRST = "(//i[contains(@class,'checkbox')])[1]"
    LISTVIEW_INVALID_PHONE_ICON_FIRST = "//i[contains(@class,'close')])[1]"
    LISTVIEW_PHONE = "(//i[contains(@class,'phone')]//following-sibling::span)[1]"

    DETAILSVIEW_VALID_PHONE_ICON = "//mat-icon[contains(text(),'check_circle')]"
    DETAILSVIEW_INVALID_PHONE_ICON = "//mat-icon[contains(text(),'highlight_off')]"


    # Document List View
    UPLOAD_DOCUMENT_FIELD = '//input[@id="imagename"]'
    ADD_DOCUMENT_BUTTON = "//div[@class='sidenav-actions']//button[contains(@class,'btn mat-f')]"
    DOCUMENT_1ST_ITEM_LIST_VIEW = "//span//span[contains(text(),' DOC')]"
    DOCUMENT_DETAILS_VIEW_VERIFICATION = "//span[contains(text(),'qa qa')]"
    # DOCUMENTS_RIGHT_SLIDER_STATUS_PICKLIST_OPEN_BUTTON = "(//div[@class='select-wrap'])[3]//span[@class='placeholder']"
    DOCUMENTS_RIGHT_SLIDER_STATUS_PICKLIST_OPEN_BUTTON = "(//div[@class='select-wrap'])[3]"
    DOCUMENTS_RIGHT_SLIDER_STATUS_PICKLIST_ITEM_APPROVED = "//ul//li//a[@title='Approved']"
    DOCUMENTS_RIGHT_SLIDER_STATUS_SAVE_BUTTON = "//button//*[contains(text(),'Save')]"
    DOCUMENTS_DOWNLOAD_BUTTON = "//div[@id='cdk-accordion-child-1']//i[@class='mdi downloadFile']"
    DOCUMENTS_DOWNLOAD_OK_BUTTON = "//span[contains(text(),'OK')]"

    # Cross Module -> Mass buttons
    MASS_DELETE_BUTTON = "//div[contains(@class,'mass-actions')]/button/span[contains(text(),'Mass Delete')]"

    # Export
    TOP_EXPORT_BUTTON = "//export-action//button"
    EXPORT_CONFIRM_BUTTON = "//div[@class='sidenav-actions']//button//span[contains(text(),'Export')]"
    CSV_CHECKBOX = "//mat-sidenav//input[@value = 'csv']//ancestor::mat-radio-button"
    EXCEL_CHECKBOX = "//mat-sidenav//input[@value = 'excel']//ancestor::mat-radio-button"
    ICAL_CHECKBOX = "//mat-sidenav//input[@value = 'ics']//ancestor::mat-radio-button"

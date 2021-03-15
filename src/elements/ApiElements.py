# All the following elements, are based on XPATH syntax identification
class ApiElements():

    #Authorization section
    API_SIDE_MENU_PARTNER_SECRET_KEY_FIELD = "//input[@name='partnerSecretKey']"
    API_AUTHORIZATION_PARTNER_ID_FIELD = "//input[@placeholder='partnerId']"
    API_AUTHORIZATION_TIME_GENERATE_BUTTON = "//*[@id='time-generator']"
    API_AUTHORIZATION_ACCESS_KEY_GENERATE_BUTTON = "//*[@id='accessKey-generator']"
    API_GENERIC_SEND_BUTTON = "//button[@class='btn btn-primary sample-request-send']"
    API_AUTHORIZATION_RESPONSE = "//*[@id='api-Authorization-Authorization']//code[@class='sample-request-response-json']"

    #[C] Customer Section
    CUSTOMER_EMAIL_FIELD = "//*[@id='sample-request-param-field-email-Customers-createCustomer-0_0_0']"
    CUSTOMER_PASSWORD_FIELD = "//*[@id='sample-request-param-field-password-Customers-createCustomer-0_0_0']"
    CUSTOMER_COUNTRY_FIELD = "//*[@id='sample-request-param-field-country-Customers-createCustomer-0_0_0']"
    CUSTOMER_FIRST_NAME_FIELD = "//*[@id='sample-request-param-field-firstName-Customers-createCustomer-0_0_0']"
    CUSTOMER_LAST_NAME_FIELD = "//*[@id='sample-request-param-field-lastName-Customers-createCustomer-0_0_0']"
    CUSTOMER_PHONE_FIELD = "//*[@id='sample-request-param-field-phone-Customers-createCustomer-0_0_0']"
    READ_CUSTOMER_SEND_BUTTON = "//*[@id='api-Customers-readCustomer-0.0.0']/form/fieldset/div[4]/div/button"
    READ_CUSTOMERS_SEND_BUTTON = "//*[@id='api-Customers-readCustomers-0.0.0']/form/fieldset/div[4]/div/button"
    READ_CUSTOMERS_PAGE_FIELD = "//input[@id='sample-request-param-field-page-Customers-readCustomers-0_0_0']"
    READ_CUSTOMERS_LIMIT_FIELD = "//input[@id='sample-request-param-field-limit-Customers-readCustomers-0_0_0']"
    UPDATE_CUSTOMER_EMAIL_FIELD = "//input[@id='sample-request-param-field-email-Customers-updateCustomer-0_0_0']"
    UPDATE_CUSTOMER_FIRST_NAME_FIELD = "//input[@id='sample-request-param-field-firstName-Customers-updateCustomer-0_0_0']"
    UPDATE_CUSTOMER_POSTAL_CODE_FIELD = "//input[@id='sample-request-param-field-postalCode-Customers-updateCustomer-0_0_0']"
    UPDATE_CUSTOMER_PHONE_FIELD = "//input[@id='sample-request-param-field-phone-Customers-updateCustomer-0_0_0']"
    UPDATE_CUSTOMER_SEND_BUTTON = "//*[@id='api-Customers-updateCustomer-0.0.0']/form/fieldset/div[4]/div/button"
    READ_LEADS_PAGE_FIELD = "//input[@id='sample-request-param-field-page-Leads-readLeads-0_0_0']"
    READ_LEADS_LIMIT_FIELD = "//input[@id='sample-request-param-field-limit-Leads-readLeads-0_0_0']"
    READ_LEADS_SEND_BUTTON = "//*[@id='api-Leads-readLeads-0.0.0']/form/fieldset/div[4]/div/button"
    READ_CUSTOMER_EMAIL_FIELD = "//*[@id='sample-request-param-field-email-Customers-readCustomer-0_0_0']"

    #Field only for eBrokerHouse
    CREATE_CUSTOMER_TERMS_AND_CONDITIONS_FIELD = "//input[@id='sample-request-param-field-acceptTermsAndConditions-Customers-createCustomer-0_0_0']"

    CUSTOMER_CREATE_BUTTON = "//*[@id='api-Customers-createCustomer-0.0.0']/form/fieldset/div[4]/div/button"
    CREATE_CUSTOMER_RESPONSE = "//*[@id='api-Customers-createCustomer-0.0.0']/form/fieldset/div[5]/pre/code"


    # [C] Lead Section
    LEAD_REFERRAL_FIELD = "//input[@id='sample-request-param-field-referral-Leads-Leads-0_0_0']"
    LEAD_COUNTRY_FIELD = "//input[@id='sample-request-param-field-country-Leads-Leads-0_0_0']"
    LEAD_EMAIL_FIELD = "//input[@id='sample-request-param-field-email-Leads-Leads-0_0_0']"
    LEAD_FIRST_NAME_FIELD = "//input[@id='sample-request-param-field-firstName-Leads-Leads-0_0_0']"
    LEAD_LAST_NAME_FIELD = "//input[@id='sample-request-param-field-lastName-Leads-Leads-0_0_0']"
    LEAD_PHONE_FIELD = "//input[@id='sample-request-param-field-phone-Leads-Leads-0_0_0']"
    LEAD_CREATE_BUTTON = "//*[@id='api-Leads-Leads-0.0.0']/form/fieldset/div[4]/div/button"







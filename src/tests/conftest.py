import datetime
import os
import shutil
import subprocess
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from pathlib import Path
from datetime import *
import time
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
import smtplib
from src.page_objects.crm.InitialSignin import InitialSignin

def pytest_addoption(parser):
    """Configure UTF-8 encoding for special characters"""
    os.system('chcp 65001')
    os.system('set PYTHONIOENCODING=utf-8')
    
    print("inside conftest.pytest_addoption() - Getting brand browser name , and brand name out of cmd")

    parser.addoption(
        "--driver", action="store", default="chrome", help="Returning name of browser")

    parser.addoption(
        "--brand", action="store", default=None, help="Returning name of the brand")

    parser.addoption(
        "--headless", action="store", default="True", help="Returning Headless status")

    parser.addoption(
        "--developer", action="store", default="production", help="Returning Headless status")

# This method receives brand name from cmd, and returns the brand name to a test class
@pytest.fixture(scope="session")
def brand(request):
    if request.config.getoption("--brand") == None:
        return print("conftest.brand(): brand variable was not received")

    else:
        return request.config.getoption("--brand")

# This method receives driver type from cmd (Default value = 'chrome'), and returns the driver to a test class
# THIS DRIVER IS FOR CRM TESTS ONLY
@pytest.fixture(scope="session")
def driver(request):

    # This section is responsible for webdriver, checking whether to use Headless or Non Headless mode
    if request.config.getoption("--driver") == "chrome":
        options = Options()

        if request.config.getoption("--headless") == "False":
            options.headless = False
            print("Running in WITHOUT headless mode")
        else:
            options.headless = True
            print("Running WITH headless mode")


        prefs = {"download.default_directory": "c:\\web-automation-downloads"}
        options.add_experimental_option("prefs", prefs)

        #Argument Under Test
        # options.add_argument("enable-features=NetworkServiceInProcess")

        #Argument Under Test
        options.add_argument("disable-features=NetworkService")

        options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=options)


    elif request.config.getoption("--driver") == "firefox":
        driver = webdriver.Firefox()

    elif request.config.getoption("--driver") == "ie":
        driver = webdriver.Ie()

    else:
        return print("driver not found in conftest.browser() method")

    driver.maximize_window()

    brand_name = request.config.getoption("--brand")

    brand_urls = get_brand_url(brand_name)

    crm_main_screen = InitialSignin(driver, brand_urls.get("crm"))

    # Step 1: Go to crm main screen
    crm_main_screen.go_to()

    # Step 2: Sign in the crm
    crm_main_screen.sign_in("new", "CrmUser", "CrmPassword")

    # Step 3: sign in verification
    crm_main_screen.sign_in_verification()

    yield driver

    time.sleep(1)

    # Quit driver
    driver.quit()

    #All in the following method will happen AFTER the session is ended - DO NOT change this method's name
    # This method contains : Sending Email, Invocing allure report on the screen
    # See additional documentation in here: https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_unconfigure
    try:

        pytest_unconfigure(config=None)

    except AttributeError:
        print("Ignore this error")


# This method receives driver type from cmd (Default value = 'chrome'), and returns the driver to a test class
# THIS DRIVER IS FOR CA/WEBTRADER TESTS ONLY
@pytest.fixture(scope="session")
def driver_ca(request):

    # This section is responsible for webdriver, checking whether to use Headless or Non Headless mode
    if request.config.getoption("--driver") == "chrome":
        options = Options()

        if request.config.getoption("--headless") == "False":
            options.headless = False
            print("Running in WITHOUT headless mode")
        else:
            options.headless = True
            print("Running WITH headless mode")


        prefs = {"download.default_directory": "c:\\web-automation-downloads"}
        options.add_experimental_option("prefs", prefs)

        #Argument Under Test
        # options.add_argument("enable-features=NetworkServiceInProcess")

        #Argument Under Test
        options.add_argument("disable-features=NetworkService")

        options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=options)


    elif request.config.getoption("--driver") == "firefox":
        driver = webdriver.Firefox()

    elif request.config.getoption("--driver") == "ie":
        driver = webdriver.Ie()

    else:
        return print("driver not found in conftest.browser() method")

    driver.maximize_window()

    brand_name = request.config.getoption("--brand")

    brand_urls = get_brand_url(brand_name)


    yield driver

    time.sleep(1)

    # Quit driver
    driver.quit()

    #All in the following method will happen AFTER the session is ended - DO NOT change this method's name
    # This method contains : Sending Email, Invocing allure report on the screen
    # See additional documentation in here: https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_unconfigure
    try:

        pytest_unconfigure(config=None)

    except AttributeError:
        print("Ignore this error")





# Brand URL's
def get_brand_url(brand_name):
    if brand_name == "analystq":
        return {"crm": "www.analystq.ptscrm.com", "ca": "https://www.analystq.com"}

    if brand_name == "newforexstage2":
        return {"crm": "https://www.google.com", "ca": "https://www.google.com"}


# POST SESSION actions - HTML report sending by email, Allure report auto open
def pytest_unconfigure(config)->None:
    import os.path

    print("BRAND NAME : "+str(config.getoption('brand')))
    print("DEVELOPER NAME : "+str(config.getoption("--developer")))

    """ Open Allure report """
    report_fire_up = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print("Allure is opening up")
    os.popen("allure serve C:\AllureReports\Data")
    time.sleep(2)

    try:

        """ Time Calculation For HTML Report """
        # Path of report.html file within src/tests path
        base_path = Path(__file__).parent
        file_path = (base_path / "../tests/report.html").resolve()

        # Calculates raw timestamp of html report creation
        raw_value_of_report_creation_timestamp = os.path.getmtime(file_path)
        email_report_creation_time = datetime.fromtimestamp(raw_value_of_report_creation_timestamp)
        delta_time = datetime.now() - email_report_creation_time

        # Log of HTML report creation time
        print("Time passed since report was created in seconds - " + str(delta_time.seconds))

        if delta_time.seconds < 10:

            """ Subscription distribution for HTML report : 'Local' run vs 'Production' run """

            developer_list = {"dima" : "dima.e@pandats.com",
                              "yarin" : "yarin.b@pandats.com" ,
                              "anastasiia" : "anastasiia.vintrovich@pandats.com" ,
                              "natalie" : "natalie.l@pandats.com"}

            # Helper variables for loop
            developer_list_length = len(developer_list)
            loop_counter = 0
            cc = None

            # Local run
            for list_developer_name, list_developer_email in developer_list.items():
                print("LOOP COUNTER - " +str(loop_counter))
                if config.getoption("--developer") == list_developer_name:
                    cc = list_developer_email
                    print("1 HTML Report Subscription sent to : " +str(cc))
                    break

            # Production
                if config.getoption("--developer") == "production":
                    cc = "dima.e+1@pandats.com,yarin.b@pandats.com,yakov.t@pandats.com,anastasiia.vintrovich@pandats.com"
                    print("2 HTML Report Subscription sent to :" +str(cc))
                    break
                loop_counter += 1


            """ Creation and sending of HTML report """
            # Building an email + HTML report attachment
            fromaddr = "pandaautomation.report@gmail.com"
            to = "dima.e@pandats.com"

            rcpt = cc.split(",") + [to]

            # instance of MIMEMultipart
            msg = MIMEMultipart()

            # storing the senders email address
            msg['From'] = fromaddr

            # storing the receivers email address
            msg['To'] = to

            msg['Cc'] = cc

            # storing the subject
            msg['Subject'] = "Automation %s suite run completed for the brand : %s | %s " %(config.getoption('-m').title(),
                                                                                            config.getoption('brand').title(),
                                                                                            str(datetime.today().strftime('%d-%m-%Y , %H:%M')))

            # string to store the body of the mail
            body = "Automation run has been completed. \n\n" \
                   "Time : " +str(datetime.today().strftime('%d-%m-%Y , %H:%M')) +"\n" \
                   "Brand : " +config.getoption('brand').title() +"\n" \
                   "Suite : " +config.getoption('-m').title() +"\n\n\n" \
                   "To review the report - please download the file and open it locally on your device. \n\n" \
                    "- QA & Automation Team -"

            # attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))

            # open the file to be sent
            filename = file_path
            attachment = open(filename, "rb")

            # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')

            # To change the payload into encoded form
            p.set_payload((attachment).read())

            # encode into base64
            encoders.encode_base64(p)

            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            # attach the instance 'p' to instance 'msg'
            msg.attach(p)

            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            s.starttls()

            # Authentication
            s.login(SMTP_EMAIL_ADDRESS, SMTP_EMAIL_PASSWORD)

            # Converts the Multipart msg into a string
            text = msg.as_string()

            # sending the mail
            s.sendmail(fromaddr, rcpt, text)

            print("EMAIL SENT")

            # The temporary download directory removal
            shutil.rmtree("c:\\web-automation-downloads")

            # terminating the session
            s.quit()
    except OSError as e:
        pass

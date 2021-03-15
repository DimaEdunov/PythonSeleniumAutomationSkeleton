
import pytest
import requests



def test_pody_q8_registration():

    response = requests.post(
        'https://dev-q8-integration.pandats-api.io/api/Registration',
        params={"Content-Type" : "text/plain" , "Content-Length" : "" , "Host" : "", "User-Agent" : "PostmanRuntime/7.26.8", "Accept" : "*/*" , "Accept-Encoding" :  "gzip, deflate, br", "Connection" : "keep-alive","Email": "rawhi.h+testg123ender1232@pandats.com",
  "Password": "123456a",
  "FirstName": "rawhi",
  "LastName": "hannon",
  "Country": "tk",
  "Currency": "eur",
  "Tel1": "97258000000",
  "TandC": "1",
  "MarketingData": "hello world data!",
  "PhoneVerified": "0",
  "PhoneType": "mobile",
  "Refferal": "Hello refferal str",
  "IP": "8.8.8.8",
  "Language": "ara",
  "Promocode": "??",
  "AccountType": "Individual",
  "NationalIdNumber": "nationalId",
  "FieldOfWork": "Student",
  "WorkAddress": "45435435g",
  "Nationality": "de",
  "PandaPartnerID": "5555",
  "Gender": "F",
  "SMSVerified": "1"},
        headers={},

    )

    # View the new `text-matches` array which provides information
    # about your search term within the results
    json_response = response.json()
    print("\n\n print of output :" +str(json_response))
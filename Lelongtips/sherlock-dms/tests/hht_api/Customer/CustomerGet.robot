*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/hht_api/Customer/CustomerGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to get Customer Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Customer Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Customer    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Details using hqsalesperson
    Then expected return status code 200

2 - Able to get Customer ShipTo Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Customer ShipTo Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Customer    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer ShipTo Details using hqsalesperson
    Then expected return status code 200

3 - Able to get Customer Option Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Customer Option Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Customer    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Option Details using hqsalesperson
    Then expected return status code 200

4 - Able to get Customer Contact Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Customer Contact Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Customer    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Contact Details using hqsalesperson
    Then expected return status code 200

5 - Able to get Customer License Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Customer License Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Customer    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer License Details using hqsalesperson
    Then expected return status code 200

6 - Able to get Customer Invoice Terms Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Customer Customer Invoice Terms Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Customer    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Invoice Terms Details using hqsalesperson
    Then expected return status code 200

7 - Able to get Customer Geo Tree Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Customer Customer Geo Tree Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Customer    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Geo Tree Details using hqsalesperson
    Then expected return status code 200

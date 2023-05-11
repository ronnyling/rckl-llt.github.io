*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to get Distributor Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Distributor Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Distributor    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Distributor Details using hqsalesperson
    Then expected return status code 200

2 - Able to get Distributor Option Sync Details using HQsalesperson
    [Documentation]  Able to retrieve Distributor Option Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Distributor    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Distributor Option Details using hqsalesperson
    Then expected return status code 200

3 - Able to get Distributor Contact Sync Details using HQsalesperson
    [Documentation]  Able to retrieve Distributor Contact Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Distributor    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Distributor Contact Details using hqsalesperson
    Then expected return status code 200

4 - Able to get Distributor ShipTo Sync Details using HQsalesperson
    [Documentation]  Able to retrieve Distributor ShipTo Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Distributor    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Distributor ShipTo Details using hqsalesperson
    Then expected return status code 200

5 - Able to get Distributor Geo Tree Sync Details using HQsalesperson
    [Documentation]  Able to retrieve Distributor Geo Tree Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Distributor    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Distributor Geo Tree Details using hqsalesperson
    Then expected return status code 200


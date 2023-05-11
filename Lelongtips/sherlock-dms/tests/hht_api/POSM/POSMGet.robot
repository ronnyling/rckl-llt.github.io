*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/POSM/POSMGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1- Able to get POSM Focused Customer using HQsalesperson
    [Documentation]    Able to retrieve POSM Focused Customer using HQsalesperson
    [Tags]    hqsalesperson    POSM    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves POSM Focused Customer using hqsalesperson
    Then expected return status code 200

2- Able to get POSM Customer using HQsalesperson
    [Documentation]    Able to retrieve POSM Customer using HQsalesperson
    [Tags]    hqsalesperson    POSM    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves POSM Customer using hqsalesperson
    Then expected return status code 200
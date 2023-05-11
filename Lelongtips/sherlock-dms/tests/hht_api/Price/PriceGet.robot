*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Price/PriceGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to get Price Setup using HQsalesperson
    [Documentation]    Able to retrieve Price Setup using HQsalesperson
    [Tags]    hqsalesperson    Price    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Price Setup using hqsalesperson
    Then expected return status code 200

2 - Able to get Price Product using HQsalesperson
    [Documentation]    Able to retrieve Price Product using HQsalesperson
    [Tags]    hqsalesperson    Price    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Price Product using hqsalesperson
    Then expected return status code 200

3 - Able to get Margin Input Pricing using HQsalesperson
    [Documentation]    Able to retrieve Margin Input Pricing using HQsalesperson
    [Tags]    hqsalesperson    Price    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Margin Input Pricing using hqsalesperson
    Then expected return status code 200

4 - Able to get Formula Input Pricing using HQsalesperson
    [Documentation]    Able to retrieve Formula Input Pricing using HQsalesperson
    [Tags]    hqsalesperson    Price    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Formula Input Pricing using hqsalesperson
    Then expected return status code 200


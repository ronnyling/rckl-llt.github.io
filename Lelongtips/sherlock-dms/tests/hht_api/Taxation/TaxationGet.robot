*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Taxation/TaxationGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to get Tax Group using HQsalesperson
    [Documentation]    Able to retrieve Tax Group using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Tax Group using hqsalesperson
    Then expected return status code 200

2 - Able to get Tax Structure using HQsalesperson
    [Documentation]    Able to retrieve Tax Structure using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Tax Structure using hqsalesperson
    Then expected return status code 200

3 - Able to get Tax Definition using HQsalesperson
    [Documentation]    Able to retrieve Tax Definition using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Tax Definition using hqsalesperson
    Then expected return status code 200

4 - Able to get Tax Setting using HQsalesperson
    [Documentation]    Able to retrieve Tax Setting using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Tax Setting using hqsalesperson
    Then expected return status code 200

5 - Able to get Tax Assignment using HQsalesperson
    [Documentation]    Able to retrieve Tax Assignment using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Tax Assignment using hqsalesperson
    Then expected return status code 200

6 - Able to get Tax State using HQsalesperson
    [Documentation]    Able to retrieve Tax State using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Tax State using hqsalesperson
    Then expected return status code 200

7 - Able to get HSN Master using HQsalesperson
    [Documentation]    Able to retrieve HSN Master using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves HSN Master using hqsalesperson
    Then expected return status code 200

8 - Able to get HSN Tax Group Info using HQsalesperson
    [Documentation]    Able to retrieve HSN Tax Group Info using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves HSN Tax Group Info using hqsalesperson
    Then expected return status code 200

9 - Able to get SAC Master using HQsalesperson
    [Documentation]    Able to retrieve SAC Master using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves SAC Master using hqsalesperson
    Then expected return status code 200

10 - Able to get SAC Tax Group using HQsalesperson
    [Documentation]    Able to retrieve SAC Tax Group using HQsalesperson
    [Tags]    hqsalesperson    Taxation    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves SAC Tax Group using hqsalesperson
    Then expected return status code 200
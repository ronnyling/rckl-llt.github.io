*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Vssc/VsscGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to retrieve VSS Dynamic Call Card
    [Documentation]    To Verify VSS Dynamic Call Card endpoint is triggered successfully
    [Tags]    salesperson    VSSC    9.1
    Given user retrieves token access as salesperson
    When user retrieves VS Dynamic Call Card using Salesperson
    Then expected return status code 403

2- Able to get VS Score Card using HQsalesperson
    [Documentation]    Able to retrieve VS Score Card using HQsalesperson
    [Tags]    hqsalesperson    VSSC    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves VS Score Card using hqsalesperson
    Then expected return status code 200

3- Able to get VS Dynamic Call Card using HQsalesperson
    [Documentation]    Able to retrieve VS Dynamic Call Card using HQsalesperson
    [Tags]    hqsalesperson    VSSC    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves VS Dynamic Call Card using hqsalesperson
    Then expected return status code 200

4- Able to get VS Score Card Detail using HQsalesperson
    [Documentation]    Able to retrieve VS Score Card Detail using HQsalesperson
    [Tags]    hqsalesperson    VSSC    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves VS Score Card Detail using hqsalesperson
    Then expected return status code 200

5- Able to get VS Customer Detail using HQsalesperson
    [Documentation]    Able to retrieve VS Customer using HQsalesperson
    [Tags]    hqsalesperson    VSSC    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves VS Customer using hqsalesperson
    Then expected return status code 200

6- Able to get VS MSL Product Category using HQsalesperson
    [Documentation]    Able to retrieve VS MSL Product Category using HQsalesperson
    [Tags]    hqsalesperson    VSSC    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves VS MSL Product Category using hqsalesperson
    Then expected return status code 200

7- Able to get VS MSL using HQsalesperson
    [Documentation]    Able to retrieve VS MSL using HQsalesperson
    [Tags]    hqsalesperson    VSSC    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves VS MSL using hqsalesperson
    Then expected return status code 200

8- Able to get VS Merchandising Audit using HQsalesperson
    [Documentation]    Able to retrieve VS Merchandising Audit using HQsalesperson
    [Tags]    hqsalesperson    VSSC    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves VS Merchandising Audit using hqsalesperson
    Then expected return status code 200

9- Able to get VS Scorecard History using HQsalesperson
    [Documentation]    Able to retrieve VS Scorecard History using HQsalesperson
    [Tags]    hqsalesperson    VSSC    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves VS Scorecard History using hqsalesperson
    Then expected return status code 200
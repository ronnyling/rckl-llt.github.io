*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/DynamicSurvey/DynamicSurveyGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to retrieve Dynamic Survey Header
    [Documentation]    Able to retrieve Dynamic Survey Header
    [Tags]    salesperson    DynamicSurvey    9.1
    Given user retrieves token access as salesperson
    When user retrieves Dynamic Survey Customer using Salesperson
    Then expected return status code 200

2 - Able to retrieve Dynamic Survey Customer
    [Documentation]    Able to retrieve Dynamic Survey Customer
    [Tags]    salesperson    DynamicSurvey    9.1
    Given user retrieves token access as salesperson
    When user retrieves Dynamic Survey Customer using Salesperson

3 - Able to retrieve Dynamic Survey Question Score
    [Documentation]    Able to retrieve Dynamic Survey Question Score
    [Tags]    salesperson    DynamicSurvey    9.1
    Given user retrieves token access as salesperson
    When user retrieves Dynamic Survey Customer using Salesperson
    Then expected return status code 200

4 - Able to retrieve Dynamic Survey Answer Option
    [Documentation]    Able to retrieve Dynamic Survey Answer Option
    [Tags]    salesperson    DynamicSurvey    9.1
    Given user retrieves token access as salesperson
    When user retrieves Dynamic Survey Customer using Salesperson
    Then expected return status code 200

5 - Able to retrieve Dynamic Survey Question
    [Documentation]    Able to retrieve Dynamic Survey Question
    [Tags]    salesperson    DynamicSurvey    9.1
    Given user retrieves token access as salesperson
    When user retrieves Dynamic Survey Customer using Salesperson
    Then expected return status code 200

6 - Able to retrieve Dynamic Survey JSON File
    [Documentation]    Able to retrieve Dynamic Survey JSON File
    [Tags]    salesperson    DynamicSurvey    9.1
    Given user retrieves token access as salesperson
    When user retrieves Dynamic Survey Customer using Salesperson
    Then expected return status code 200

7- Able to get Dynamic Survey Header using HQsalesperson
    [Documentation]    Able to retrieve Dynamic Survey Header using HQsalesperson
    [Tags]    hqsalesperson    DynamicSurvey    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Dynamic Survey Header using hqsalesperson
    Then expected return status code 200

8- Able to get Dynamic Survey Customer using HQsalesperson
    [Documentation]    Able to retrieve Dynamic Survey Customer using HQsalesperson
    [Tags]    hqsalesperson    DynamicSurvey    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Dynamic Survey Customer using hqsalesperson
    Then expected return status code 200

9- Able to get Dynamic Survey Question Score using HQsalesperson
    [Documentation]    Able to retrieve Dynamic Survey Question Score using HQsalesperson
    [Tags]    hqsalesperson    DynamicSurvey    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Dynamic Survey Question Score using hqsalesperson
    Then expected return status code 200

10- Able to get Dynamic Survey Subject using HQsalesperson
    [Documentation]    Able to retrieve Dynamic Survey Subject using HQsalesperson
    [Tags]    hqsalesperson    DynamicSurvey    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Dynamic Survey Subject using hqsalesperson
    Then expected return status code 200

11- Able to get Dynamic Survey Answer Option using HQsalesperson
    [Documentation]    Able to retrieve Dynamic Survey Answer Option using HQsalesperson
    [Tags]    hqsalesperson    DynamicSurvey    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Dynamic Survey Answer Option using hqsalesperson
    Then expected return status code 200

12- Able to get Dynamic Survey Question using HQsalesperson
    [Documentation]    Able to retrieve Dynamic Survey Question using HQsalesperson
    [Tags]    hqsalesperson    DynamicSurvey    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Dynamic Survey Question using hqsalesperson
    Then expected return status code 200

13- Able to get Dynamic Survey History using HQsalesperson
    [Documentation]    Able to retrieve Dynamic Survey History using HQsalesperson
    [Tags]    hqsalesperson    DynamicSurvey    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Dynamic Survey History using hqsalesperson
    Then expected return status code 200
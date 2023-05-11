*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/DynamicSurvey/SurveyResult/SurveyResultGet.py

*** Test Cases ***
1 - Able to retrieve all Dynamic Survey result
    [Documentation]    Able to retrieve all Dynamic Survey result
    [Tags]    hqadm    distadm
    Given user retrieves token access as hqadm
    When user retrieves all dynamic survey result
    Then expected return status code 200

2 - Able to retrieve Dynamic Survey result details
    [Documentation]    Able to retrieve Dynamic Survery result details
    [Tags]    hqadm    distadm
    Given user retrieves token access as hqadm
    When user retrieves all dynamic survey result
    Then expected return status code 200
    When user retrieves dynamic survey result details
    Then expected return status code 200

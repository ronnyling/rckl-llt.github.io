*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/DynamicSurvey/SurveySetup/SurveySetupGet.py

*** Test Cases ***
1 - Able to retrieve all Dynamic Survey setup
    [Documentation]    Able to retrieve all Dynamic Survey setup
    [Tags]    hqadm    distadm
    Given user retrieves token access as hqadm
    When user retrieves all dynamic survey
    Then expected return status code 200

2 - Able to retrieve Dynamic Survey by id
    [Documentation]    Able to retrieve Dynamic Survery by id
    [Tags]    hqadm    distadm
    Given user retrieves token access as hqadm
    When user retrieves all dynamic survey
    Then expected return status code 200
    When user retrieves dynamic survey by id
    Then expected return status code 200

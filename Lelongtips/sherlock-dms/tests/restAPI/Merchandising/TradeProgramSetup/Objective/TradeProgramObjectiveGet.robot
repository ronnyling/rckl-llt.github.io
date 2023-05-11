*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Objective/TradeProgramObjectiveGet.py

*** Test Cases ***
1-Able to retrieve all trade program objective via API
    [Documentation]  This test is to retrieve all trade program objective via API
    [Tags]      hqadm
    Given user retrieves token access as hqadm
    When user retrieves all trade program objectives
    Then expected return status code 200

2-Able to retrieve trade program objective details via ID
    [Documentation]  This test is to retrieve trade program objective details via ID
    [Tags]      hqadm
    Given user retrieves token access as hqadm
    When user retrieves program objective details
    Then expected return status code 200

*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Objective/TradeProgramObjectivePost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Objective/TradeProgramObjectiveDelete.py

*** Test Cases ***
1-Able to retrieve all trade program objective via API
    [Documentation]  This test is to retrieve all trade program objective via API
    [Tags]    9.1
    Given user retrieves token access as hqadm
    When user post to trade program objective
    Then expected return status code 201
    And user delete trade program objective details
    Then expected return status code 200

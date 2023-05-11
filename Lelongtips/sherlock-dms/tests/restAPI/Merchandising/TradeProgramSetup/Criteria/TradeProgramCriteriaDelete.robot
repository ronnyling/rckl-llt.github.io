*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Criteria/TradeProgramCriteriaPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Criteria/TradeProgramCriteriaDelete.py

*** Test Cases ***
1-Able to retrieve all trade program criteria via API
    [Documentation]  This test is to retrieve all trade program criteria via API
    [Tags]    9.1
    Given user retrieves token access as hqadm
    When user post to trade program criteria
    Then expected return status code 201
    And user delete trade program criteria details
    Then expected return status code 200

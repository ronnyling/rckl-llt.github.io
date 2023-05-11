*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramDelete.py



*** Test Cases ***
1 - Able to post to trade program API
    [Documentation]  This test is to post to trade program API
    [Tags]      hqadm
    [Teardown]  user delete trade program details
    Given user retrieves token access as hqadm
    When user post to trade program
    Then expected return status code 201

2 - Able to post to trade program API for criteria
    [Documentation]  This test is to post to trade program API for criteria
    [Tags]      hqadm
    [Teardown]  user delete trade program details
    Given user retrieves token access as hqadm
    When user post to trade program
    Then expected return status code 201
    When user post to trade program for criteria
    Then expected return status code 201

3 - Able to post to trade program API for criteria objective
    [Documentation]  This test is to post to trade program API for criteria objective
    [Tags]      hqadm
    [Teardown]  user delete trade program details
    Given user retrieves token access as hqadm
    When user post to trade program
    Then expected return status code 201
    When user post to trade program for criteria
    Then expected return status code 201
    When user post to trade program for criteria objective
    Then expected return status code 201

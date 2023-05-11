*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramPut.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramDelete.py

*** Test Cases ***
1-Able to retrieve all trade program via API
    [Documentation]  This test is to retrieve all trade program via API
    [Tags]      hqadm
    [Teardown]  run keywords
    ...     user delete trade program details
    Given user retrieves token access as hqadm
    When user post to trade program
    And user post to trade program for criteria
    And user post to trade program for criteria objective
    Then expected return status code 201
    When user puts to trade program details
    Then expected return status code 200

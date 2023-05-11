*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramGet.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramDelete.py

*** Test Cases ***
1-Able to retrieve all trade program via API
    [Documentation]  This test is to retrieve all trade program via API
    [Tags]      hqadm
    Given user retrieves token access as hqadm
    When user retrieves all trade programs
    Then expected return status code 200

2-Able to retrieve all trade program details via API by using id
    [Documentation]  This test is to retrieve all trade program details via API by using id
    [Tags]      hqadm
    [Teardown]  user delete trade program details
    Given user retrieves token access as hqadm
    When user post to trade program
    Then expected return status code 201
    And user post to trade program for criteria
    Then expected return status code 201
    And user post to trade program for criteria objective
    Then expected return status code 201
    When user retrieves trade program details
    Then expected return status code 200
    When user retrieves criteria for trade program details
    Then expected return status code 200
    When user retrieves objective of criteria for trade program details
    Then expected return status code 200

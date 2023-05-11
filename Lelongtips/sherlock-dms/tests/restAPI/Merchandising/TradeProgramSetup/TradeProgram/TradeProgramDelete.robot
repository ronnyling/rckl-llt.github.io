*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/TradeProgram/TradeProgramDelete.py

*** Test Cases ***
1-Able to retrieve all program group via API
    [Documentation]  This test is to retrieve all program group via API
    [Tags]    9.1
    Given user retrieves token access as hqadm
    When user post to trade program
    Then expected return status code 201
    And user post to trade program for criteria
    Then expected return status code 201
    And user post to trade program for criteria objective
    Then expected return status code 201
    When user delete objective of criteria for trade program details
    Then expected return status code 200
    And user delete trade program details
    Then expected return status code 200


#2-Able to retrieve all program group via API by using id
#    [Documentation]  This test is to retrieve all program group via API
#    [Tags]    9.1     hqadm00
#    Given user retrieves token access as ${user_role}
#    When user retrieves all program groups
#

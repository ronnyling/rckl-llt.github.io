*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Objective/TradeProgramObjectivePost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Objective/TradeProgramObjectiveDelete.py



*** Test Cases ***
1 - Able to post to trade prsogram objective API
    [Documentation]  This test is to post to trade program objective API
    [Tags]      hqadm
    [Teardown]  user delete trade program objective details
    Given user retrieves token access as hqadm
    When user post to trade program objective
    Then expected return status code 201

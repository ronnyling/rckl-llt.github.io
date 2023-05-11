*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Criteria/TradeProgramCriteriaPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Criteria/TradeProgramCriteriaDelete.py



*** Test Cases ***
1 - Able to post to trade prsogram criteria API
    [Documentation]  This test is to post to trade program criteria API
    [Tags]      hqadm
    [Teardown]  user delete trade program criteria details
    Given user retrieves token access as hqadm
    When user post to trade program criteria
    Then expected return status code 201

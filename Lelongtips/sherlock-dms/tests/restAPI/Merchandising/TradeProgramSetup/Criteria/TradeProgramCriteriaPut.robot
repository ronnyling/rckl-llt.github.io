*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Criteria/TradeProgramCriteriaPut.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Criteria/TradeProgramCriteriaPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Criteria/TradeProgramCriteriaDelete.py

*** Test Cases ***
1-Able to retrieve all trade program criteria via API
    [Documentation]  This test is to retrieve all trade program criteria via API
    [Tags]      hqadm
    [Teardown]  run keywords
    ...     user delete trade program criteria details
    Given user retrieves token access as hqadm
    When user post to trade program criteria
    Then expected return status code 201
    When user puts to trade program criteria details
    Then expected return status code 200

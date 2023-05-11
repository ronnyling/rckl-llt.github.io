*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/Criteria/TradeProgramCriteriaGet.py

*** Test Cases ***
1-Able to retrieve all trade program criteria via API
    [Documentation]  This test is to retrieve all trade program criteria via API
    [Tags]      hqadm
    Given user retrieves token access as hqadm
    When user retrieves all trade program criterias
    Then expected return status code 200

2-Able to retrieve trade program criteria details via ID
    [Documentation]  This test is to retrieve trade program criteria details via ID
    [Tags]      hqadm
    Given user retrieves token access as hqadm
    When user retrieves program criteria details
    Then expected return status code 200

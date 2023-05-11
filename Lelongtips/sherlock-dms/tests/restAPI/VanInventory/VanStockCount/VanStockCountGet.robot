*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanStockCount/VanStockCountGet.py

*** Test Cases ***
1 - Able to retrieve van stock count listing
    [Documentation]    To retrieve van stock count listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves van stock count listing
    Then expected return status code 200

2 - Able to retrieve van stock count details
    [Documentation]    To retrieve van stock count details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    And user retrieves van stock count details
    Then expected return status code 200

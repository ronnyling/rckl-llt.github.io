*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanStockRequest/VanStockRequestGet.py

*** Test Cases ***
1 - Able to retrieve van stock request listing
    [Documentation]    To retrieve van stock request listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves van stock request listing
    Then expected return status code 200

2 - Able to retrieve van stock request details
    [Documentation]    To retrieve van stock request details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    And user retrieves van stock request details
    Then expected return status code 200

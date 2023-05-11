*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanStockIn/VanStockInGet.py

*** Test Cases ***
1 - Able to retrieve van stock in listing
    [Documentation]    To retrieve van stock in listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves van stock in listing
    Then expected return status code 200

2 - Able to retrieve van stock in details
    [Documentation]    To retrieve van stock in details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    And user retrieves van stock in details
    Then expected return status code 200

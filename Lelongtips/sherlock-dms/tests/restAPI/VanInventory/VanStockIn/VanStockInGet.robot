*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanStockOut/VanStockOutGet.py

*** Test Cases ***
1 - Able to retrieve van stock out listing
    [Documentation]    To retrieve van stock out listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves van stock out listing
    Then expected return status code 200

2 - Able to retrieve van stock out details
    [Documentation]    To retrieve van stock out details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    And user retrieves van stock out details
    Then expected return status code 200

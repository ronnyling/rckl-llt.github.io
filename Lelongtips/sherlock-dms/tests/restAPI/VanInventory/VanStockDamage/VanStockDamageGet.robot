*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanStockDamage/VanStockDamageGet.py

*** Test Cases ***
1 - Able to retrieve van stock damage listing
    [Documentation]    To retrieve van stock damage listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves van stock damage listing
    Then expected return status code 200

2 - Able to retrieve van stock damage details
    [Documentation]    To retrieve van stock damage details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    And user retrieves van stock damage details
    Then expected return status code 200

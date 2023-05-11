*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanStockIn/VanStockInGet.py
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanReplenishment/VanReplenishmentGet.py

*** Test Cases ***
1 - Able to retrieve van replenishment listing
    [Documentation]    To retrieve van replenishment listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves van replenishment listing
    Then expected return status code 200

2 - Able to retrieve van replenishment details
    [Documentation]    To retrieve van replenishment details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves van replenishment details
    Then expected return status code 200

*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAdjustment/StockAdjustmentGet.py

*** Test Cases ***
1 - Able to retrieve stock receipt listing
    [Documentation]    To retrieve stock receipt listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves stock adjustment listing
    Then expected return status code 201

2 - Able to retrieve stock adjustment details
    [Documentation]    To retrieve stock adjustment details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves stock adjustment listing
    Then expected return status code 201
    When user retrieves stock adjustment details
    Then expected return status code 201

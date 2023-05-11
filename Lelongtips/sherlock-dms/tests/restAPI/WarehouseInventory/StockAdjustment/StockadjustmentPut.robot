*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAdjustment/StockAdjustmentPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAdjustment/StockAdjustmentPut.py

*** Test Cases ***
1 - Able to save & confirm stock adjustment
    [Documentation]    To save & confirm stock adjustment
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user post to save stock adjustment
    And user puts to save stock adjustment
    Then expected return status code 200
    When user puts to confirm stock adjustment
    Then expected return status code 200




*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAdjustment/StockAdjustmentCancel.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAdjustment/StockAdjustmentPost.py

*** Test Cases ***
1 - Able to cancel stock adjustment
    [Documentation]    To cancel stock adjustment
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user post to save stock adjustment
    And user cancel stock adjustment
    Then expected return status code 201





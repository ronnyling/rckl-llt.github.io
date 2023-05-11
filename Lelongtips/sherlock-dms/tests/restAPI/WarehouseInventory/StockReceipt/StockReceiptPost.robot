*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockReceipt/StockReceiptPost.py

*** Test Cases ***
1 - Able to save & confirm stock receipt
    [Documentation]    To save & confirm stock receipt
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user post to save stock receipt
    Then expected return status code 201
    When user post to confirm stock receipt
    Then expected return status code 201






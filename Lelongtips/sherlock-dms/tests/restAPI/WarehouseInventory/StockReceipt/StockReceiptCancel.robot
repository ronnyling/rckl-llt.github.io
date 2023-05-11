*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockReceipt/StockReceiptCancel.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockReceipt/StockReceiptPost.py

*** Test Cases ***
1 - Able to cancel stock receipt
    [Documentation]    To cancel stock receipt
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user post to save stock receipt
    And user cancel stock receipt
    Then expected return status code 201

2 - Unable to save & confirm stock receipt
    [Documentation]    Unable to cancel confirmed stock receipt
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user post to confirm stock receipt
    And user cancel stock receipt
    Then expected return status code 201




*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockReceipt/StockReceiptGet.py

*** Test Cases ***
1 - Able to retrieve stock receipt listing
    [Documentation]    To retrieve stock receipt listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves stock receipt listing
    Then expected return status code 200

2 - Able to retrieve stock receipt details
    [Documentation]    To retrieve stock receipt listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves stock receipt listing
    Then expected return status code 200
    When user retrieves all inventory status from codetable
    Then expected return status code 200
    When user retrieves stock receipt details
    Then expected return status code 200
    When user retrieves all whs available for dist
    Then expected return status code 200
    When user retrieves bin batch details for stock receipt
    Then expected return status code 200



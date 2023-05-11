*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockOut/StockOutGet.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockOut/StockOutPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockOut/StockOutCancel.py

*** Test Cases ***
1 - Able to retrieve stock out listing
    [Documentation]    To retrieve stock out listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves stock out listing
    Then expected return status code 200

2 - Able to retrieve stock out details
    [Documentation]    To retrieve stock out details
    [Tags]     distadm
    [Teardown]  run keywords
    ...     user cancels stock out
    Given user retrieves token access as ${user_role}
    When user post to save stock out without stock movement for fully-managed
    Then expected return status code 200
    When user retrieves stock out details
    Then expected return status code 200

*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockOut/StockOutPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockOut/StockOutPut.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to put to save and confirm stock out
    [Documentation]    To put to save and confirm stock out
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to save stock out without stock movement for fully-managed
    Then expected return status code 200
    When user puts to save stock out
    Then expected return status code 200
    When user puts to confirm stock out
    Then expected return status code 200

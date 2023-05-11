*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/BinTransfer/BinTransferPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/BinTransfer/BinTransferPut.py

*** Test Cases ***
1 - Able to put bin transfer
    [Documentation]    To put bin transfer
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to save bin transfer
    Then expected return status code 201
    When user puts to save bin transfer
    Then expected return status code 200
    When user puts to confirm bin transfer
    Then expected return status code 200

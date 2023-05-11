*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/BinTransfer/BinTransferPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/BinTransfer/BinTransferCancel.py

*** Test Cases ***
1 - Able to put to cancel bin transfer
    [Documentation]    To put to cancel bin transfer
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to save bin transfer
    And user puts to cancel bin transfer
    Then expected return status code 201

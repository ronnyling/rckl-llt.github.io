*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/BinTransfer/BinTransferPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/BinTransfer/BinTransferPut.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to save & confirm bin transfer
    [Documentation]    To save & confirm bin transfer
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    [Teardown]  run keywords
    ...     user puts to confirm bin transfer
    Given user retrieves token access as ${user_role}
    When user post to save bin transfer
    Then expected return status code 201

2 - Able to save & confirm own warehouse transfer from fm whs to sm whs
    [Documentation]    To save & confirm own warehouse transfer from fm whs to sm whs
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to confirm bin transfer
    Then expected return status code 201

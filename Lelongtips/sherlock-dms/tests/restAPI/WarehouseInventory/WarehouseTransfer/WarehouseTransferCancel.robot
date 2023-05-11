*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/WarehouseTransfer/WarehouseTransferPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/WarehouseTransfer/WarehouseTransferCancel.py

*** Test Cases ***
1 - Able to put to cancel warehouse transfer from fm whs to um whs
    [Documentation]    To put to cancel warehouse transfer from fm whs to um whs
    [Tags]       distadm
    ${dist_src_dest}=    create dictionary
    ...    src_distributor_id=3CAF4BF6:F0A6331B-3CFD-4DB4-9792-A27221CC2250
    Given user retrieves token access as ${user_role}
    When user post to save own warehouse transfer from fully-managed to unmanaged
    When user puts to cancel warehouse transfer
    Then expected return status code 201

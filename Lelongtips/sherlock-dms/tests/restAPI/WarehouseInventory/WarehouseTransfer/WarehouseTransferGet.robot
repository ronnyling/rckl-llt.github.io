*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/WarehouseTransfer/WarehouseTransferGet.py

*** Test Cases ***
1 - Able to retrieve warehouse transfer listing
    [Documentation]    To retrieve warehouse transfer listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves warehouse transfer listing
    Then expected return status code 200

2 - Able to retrieve warehouse transfer details
    [Documentation]    To retrieve warehouse transfer details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves warehouse transfer listing
    Then expected return status code 200
    When user retrieves warehouse transfer details
    Then expected return status code 200




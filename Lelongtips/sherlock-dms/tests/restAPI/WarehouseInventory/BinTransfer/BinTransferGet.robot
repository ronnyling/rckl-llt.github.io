*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/BinTransfer/BinTransferGet.py

*** Test Cases ***
1 - Able to retrieve bin transfer listing
    [Documentation]    To retrieve bin transfer listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves bin transfer listing
    Then expected return status code 200

2 - Able to retrieve bin transfer details
    [Documentation]    To retrieve bin transfer details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves bin transfer listing
    Then expected return status code 200
    When user retrieves bin transfer details
    Then expected return status code 200




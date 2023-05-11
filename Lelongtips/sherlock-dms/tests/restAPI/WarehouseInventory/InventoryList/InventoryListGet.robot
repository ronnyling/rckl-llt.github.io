*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/InventoryList/InventoryListGet.py

*** Test Cases ***
1 - Able to retrieve warehouse inventory listing
    [Documentation]    To retrieve warehouse inventory listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves inventory summary for all warehouse
    Then expected return status code 200

1 - Able to retrieve warehouse inventory bin batch details
    [Documentation]    To retrieve warehouse inventory bin batch details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves warehouse with bin batch
    And user retrieves bin wise details for wh
    Then expected return status code 200





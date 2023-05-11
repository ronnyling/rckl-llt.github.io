*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAudit/StockAuditGet.py

*** Test Cases ***
1 - Able to retrieve stock audit listing
    [Documentation]    To retrieve stock audit listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves stock audit listing
    Then expected return status code 200

2 - Able to retrieve stock audit details
    [Documentation]    To retrieve stock audit details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves stock audit listing
    Then expected return status code 200
    When user retrieves stock audit details
    Then expected return status code 200

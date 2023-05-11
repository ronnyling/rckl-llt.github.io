*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAudit/StockAuditPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAudit/StockAuditPut.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAudit/StockAuditApproval.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to save and confirm stock then approve
    [Documentation]    To save and confirm stock audit
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to save stock audit by bin
    Then expected return status code 200
    When user puts to save stock audit
    Then expected return status code 200
    When user puts to confirm stock audit
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user puts to approve stock audit approval
    Then expected return status code 200

2 - Able to save and confirm stock audit then reject
    [Documentation]    To save and confirm stock audit
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to save stock audit by bin
    Then expected return status code 200
    When user puts to save stock audit
    Then expected return status code 200
    When user puts to confirm stock audit
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user puts to reject stock audit approval
    Then expected return status code 200

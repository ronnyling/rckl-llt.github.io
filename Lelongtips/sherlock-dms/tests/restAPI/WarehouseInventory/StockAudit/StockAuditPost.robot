*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAudit/StockAuditPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAudit/StockAuditPut.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAudit/StockAuditApproval.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to retrieve excluded products for stock audit
    [Documentation]    To retrieve excluded products for stock audit
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to retrieve excluded product for stock audit by bin
    Then expected return status code 200
    When user post to retrieve excluded product for stock audit by product
    Then expected return status code 200

2 - Able to save stock audit by bin
    [Documentation]    To save & confirm stock audit by bin
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    [Teardown]  run keywords
    ...     user puts to confirm stock audit
    Given user retrieves token access as ${user_role}
    When user post to retrieve excluded product for stock audit by bin
    And user post to save stock audit by bin
    Then expected return status code 200
    When user puts to confirm stock audit
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user puts to approve stock audit approval
    Then expected return status code 200


3 - Able to save stock audit by product
    [Documentation]    To save & confirm stock audit by product
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    [Teardown]  run keywords
    ...     user puts to confirm stock audit
    Given user retrieves token access as ${user_role}
    When user post to retrieve excluded product for stock audit by bin
    And user post to save stock audit by product
    Then expected return status code 200
    When user puts to confirm stock audit
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user puts to approve stock audit approval
    Then expected return status code 200

*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAudit/StockAuditPost.py
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockAudit/StockAuditCancel.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to cancel stock audit
    [Documentation]    To cancel stock audit
    [Tags]     distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to retrieve excluded product for stock audit by bin
    And user post to save stock audit by product
    Then expected return status code 200
    When user cancels stock audit
    Then expected return status code 201

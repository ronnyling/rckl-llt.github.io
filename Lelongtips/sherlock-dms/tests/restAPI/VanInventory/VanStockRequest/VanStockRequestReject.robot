*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanStockRequest/VanStockRequestReject.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to reject van stock request
    [Documentation]    To reject van stock request
    [Tags]     distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user puts to reject van stock request
    Then expected return status code 200

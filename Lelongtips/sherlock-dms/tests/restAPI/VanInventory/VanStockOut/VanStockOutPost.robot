*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanStockOut/VanStockOutPost.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to post van stock out for unmanaged whs
    [Documentation]    To post van stock out for unmanaged whs
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user pump db to generate van stock out data with open status
    Then expected return status code 200

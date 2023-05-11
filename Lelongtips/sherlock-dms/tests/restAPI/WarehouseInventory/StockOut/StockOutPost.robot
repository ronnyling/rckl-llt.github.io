*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/WarehouseInventory/StockOut/StockOutPost.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to post stock out for unmanaged whs
    [Documentation]    To post stock out for unmanaged whs
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to save stock out without stock movement for unmanaged
    Then expected return status code 200

2 - Able to post stock out for semi-managed whs
    [Documentation]    To post stock out for semi-managed whs
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to save stock out without stock movement for semi-managed
    Then expected return status code 200

3 - Able to post stock out for fully-managed whs
    [Documentation]    To post stock out for fully-managed whs
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to save stock out without stock movement for fully-managed
    Then expected return status code 200

4 - Able to post to confirm stock out for unmanaged whs
    [Documentation]    To post to confirm stock out for unmanaged whs
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to confirm stock out without stock movement for unmanaged
    Then expected return status code 200

5 - Able to post to confirm stock out with stock movement for unmanaged whs
    [Documentation]    To post to confirm stock out with stock movement for unmanaged whs
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user post to confirm stock out with stock movement for unmanaged
    Then expected return status code 200

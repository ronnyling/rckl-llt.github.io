*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehousePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

Test Setup        run keywords
...    user retrieves token access as hqadm
...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to delete Warehouse with randomly created data
    [Documentation]    To delete warehouse by passing in id via API
    [Tags]     distadm    9.0    NRSZUANQ-28236   DeleteDebug
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    When user deletes warehouse with created data
    Then expected return status code 200

2 - Unable to delete warehouse with invalid id
    [Documentation]    To delete warehouse by passing in invalid id via API
    [Tags]     distadm    9.0   DeleteDebug
    set test variable    ${invalid_warehouse_id}    C209B33D:8EF55ACF-0338-452F-A3FB-1122334455DF
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    When user deletes warehouse with invalid data
    Then expected return status code 404
    When user deletes warehouse with created data
    Then expected return status code 200

3 - Unable to delete Warehouse using HQ access
    [Documentation]    Unable to delete warehouse by using other than distributor access
    [Tags]     hqadm    hquser    sysimp    9.1     NRSZUANQ-28243
    Given user retrieves token access as distadm
    When user creates warehouse with random data
    Then expected return status code 201
    Given user retrieves token access as ${user_role}
    When user deletes warehouse with created data
    Then expected return status code 403
    Given user retrieves token access as distadm
    When user deletes warehouse with created data
    Then expected return status code 200

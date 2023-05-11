*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehousePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

Test Setup        run keywords
...    user retrieves token access as hqadm
...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to retrieve all Warehouse data
    [Documentation]  To retrieve all warehouse record via API
    [Tags]    distadm     9.0   DeleteDebug
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    When user gets all warehouse data
    Then expected return status code 200
    When user deletes warehouse with created data
    Then expected return status code 200

2 - Able to retrieve the warehouse by using ID
    [Documentation]    To retrieve the warehouse via ID via API
    [Tags]     distadm    9.0    NRSZUANQ-28235   DeleteDebug
    Given user retrieves token access as ${user_role}
    When user creates warehouse with random data
    Then expected return status code 201
    When user gets warehouse by using id
    Then expected return status code 200
    When user deletes warehouse with created data
    Then expected return status code 200

3 - Unable to retrieve warehouse with invalid ID
    [Documentation]  To ensure the user is unable to get warehouse by using invalid ID
    [Tags]    distadm    9.0   DeleteDebug
    set test variable       ${res_bd_warehouse_id}    aabbccdd:eeffgghh-1122-3344-5566
    Given user retrieves token access as ${user_role}
    When user gets warehouse by using id
    Then expected return status code 404

4 - Able to retrieve all Warehouse data using HQ access
    [Documentation]  To retrieve all warehouse record using other than distributor access via API
    [Tags]    hqadm   hquser   sysimp   9.1    NRSZUANQ-28240
    Given user retrieves token access as ${user_role}
    When user gets all warehouse data
    Then expected return status code 200

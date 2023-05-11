*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RoutePlan/RoutePlanGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RoutePlan/RoutePlanPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RoutePlan/RoutePlanDelete.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to retrieve all route plan
    [Documentation]    Able to retrieve all route plan
    [Tags]    distadm    9.3
    [Teardown]  run keywords
    ...     user deletes route plan
    Given user retrieves token access as ${user_role}
#    When ${user_role} creates route plan with random data
    When user creates route plan
    Then expected return status code 200
    When user retrieves all route plan
    Then expected return status code 200

2 - Able to retrieve route plan using valid ID
    [Documentation]    Able to retrieve route plan using valid ID
    [Tags]    distadm    hqadm    9.3
    [Teardown]  run keywords
    ...     user deletes route plan
    Given user retrieves token access as ${user_role}
    When user creates route plan
    Then expected return status code 200
    When user retrieves route plan by valid id
    Then expected return status code 200

3 - Unable to retrieve route plan using invalid ID
    [Documentation]    Unable to retrieve route plan using invalid ID
    [Tags]    distadm    hqadm    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves route plan by invalid id
    Then expected return status code 404
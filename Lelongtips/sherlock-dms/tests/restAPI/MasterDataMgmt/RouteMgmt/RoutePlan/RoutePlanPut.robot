*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RoutePlan/RoutePlanPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RoutePlan/RoutePlanPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RoutePlan/RoutePlanDelete.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to PUT route plan with random data
    [Documentation]    Able to update route plan with random generated data via API
    [Tags]    hqadm    distadm    9.3
    Given user retrieves token access as ${user_role}
    When user creates route plan
    Then expected return status code 200
    When ${user_role} updates route plan with random data
    Then expected return status code 200
    When user deletes route plan
    Then expected return status code 200
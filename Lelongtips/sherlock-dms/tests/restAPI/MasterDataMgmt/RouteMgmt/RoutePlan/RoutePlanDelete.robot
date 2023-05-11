*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RoutePlan/RoutePlanPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RoutePlan/RoutePlanDelete.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to DELETE route plan and get 200
    [Documentation]  To delete route plan via API
    [Tags]    distadm    hqadm    9.3
    Given user retrieves token access as ${user_role}
    When user creates route plan
    Then expected return status code 200
    When user deletes route plan
    Then expected return status code 200

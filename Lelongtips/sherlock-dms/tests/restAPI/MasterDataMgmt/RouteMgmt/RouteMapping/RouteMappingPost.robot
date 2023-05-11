*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteMappingPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteMappingGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteMappingDelete.py

Test Setup      user_creates_prerequisite_for_route_mapping


*** Test Cases ***
1 - Able to map route to the supervisor route and return 200
    [Documentation]    To map route to the supervisor route and return 200 via api
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user maps random route to supervisor route
    Then expected return status code 200

2 - Unable to map invalid route to the supervisor route and return 404
    [Documentation]    To map route to the supervisor route and return 404 via api
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user maps invalid route to supervisor route
    Then expected return status code 404



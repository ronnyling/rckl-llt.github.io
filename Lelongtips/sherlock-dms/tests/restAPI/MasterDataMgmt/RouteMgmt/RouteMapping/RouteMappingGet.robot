*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RoutePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteMappingGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteMappingPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteMappingDelete.py

Test Setup      user_creates_prerequisite_for_route_mapping


*** Test Cases ***
1 - Able to retrieve all Available Route for Mapping
    [Documentation]    To retrieve all route mapping via API
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all route mapping data
    Then expected return status code 200

2 - Unable to retrieve invalid available route for mapping and return 404
    [Documentation]    To retrieve invalid route mapping via API
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves invalid route mapping data
    Then expected return status code 404

3 - Able to retrieve mapped route information and return 200
    [Documentation]    To retrieve all route that mapped to supervisor route via api and return 200
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user maps random route to supervisor route
    Then expected return status code 200
    When user retrieves mapped route data
    Then expected return status code 200

4 - Unable to retrieve mapped route information and return 204
    [Documentation]    To retrieve empty data from created supervisor route without route mapping and return 204
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves mapped route data
    Then expected return status code 204

5 - Unable to retrieve deleted route mapping and return 404
    [Documentation]    To retrieve deleted route mapping and return 404 via api
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user maps random route to supervisor route
    Then expected return status code 200
    When user deletes created route mapping data
    Then expected return status code 200
    When user deletes created route mapping data
    Then expected return status code 404
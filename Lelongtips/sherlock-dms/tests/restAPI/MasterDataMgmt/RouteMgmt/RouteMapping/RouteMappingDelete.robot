*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteMappingPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteMappingGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteMappingDelete.py

Test Setup      user creates prerequisite for route mapping

*** Test Cases ***

1 - Able to delete mapped route and return 200
    [Documentation]    To delete mapped route and return 200 via api
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user maps random route to supervisor route
    Then expected return status code 200
    When user deletes created route mapping data
    Then expected return status code 200

2 - Unable to delete invalid mapped route and return 404
    [Documentation]    Unable to delete invalid route mapping id and return 404
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user deletes invalid route mapping data
    Then expected return status code 404

3 - Unable to delete deleted route mapping and return 404
    [Documentation]    Unable to delete invalid route mapping id and return 404
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user maps random route to supervisor route
    Then expected return status code 200
     When user deletes created route mapping data
    Then expected return status code 200
    When user deletes deleted route mapping data
    Then expected return status code 404
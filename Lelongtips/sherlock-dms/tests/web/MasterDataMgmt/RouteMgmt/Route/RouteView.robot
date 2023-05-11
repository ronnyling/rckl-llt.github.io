*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/Route/RouteListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/Route/RouteAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/Route/RouteEditPage.py

*** Test Cases ***
1 - Validate fields are disabled when viewing route
    [Documentation]    Validate fields are disabled when viewing route
    [Tags]     distadm
    Given user navigates to menu Master Data Management | Route Management | Route
    When user creates route using random data
    And user assigns geo value using random data
    Then route created successfully with message 'Record created'
    When user selects route to edit
    Then user validated fields are disabled and cant be edited
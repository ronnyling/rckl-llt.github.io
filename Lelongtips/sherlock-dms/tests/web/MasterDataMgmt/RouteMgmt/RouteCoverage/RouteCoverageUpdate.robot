*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoverageAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoverageEditPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoverageListingPage.py

Test Teardown     run keywords
...    user selects route coverage to delete
...    User Logouts And Closes Browser

*** Test Cases ***
1 - Able to update route coverage
    [Documentation]    Able to update route coverage
    [Tags]     distadm
    Given user navigates to menu Master Data Management | Route Management | Route Coverage
    When user creates route coverage using random data
    And user selects route coverage to edit
    When user updates the route coverage date
    Then route coverage updated successfully with message 'Record updated'
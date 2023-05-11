*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoverageAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoverageListingPage.py


*** Test Cases ***
1 - Able to create delete route coverage
    [Documentation]    Able to delete route coverage
    [Tags]     distadm
    Given user navigates to menu Master Data Management | Route Management | Route Coverage
    When user creates route coverage using random data
    Then route coverage created successfully with message 'Record created'
    When user selects route coverage to delete
    Then route coverage created successfully with message 'Record deleted'


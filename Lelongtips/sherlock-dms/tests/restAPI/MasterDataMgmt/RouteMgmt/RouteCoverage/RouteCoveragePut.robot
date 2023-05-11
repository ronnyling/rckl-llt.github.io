*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoveragePost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoveragePut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoverageDelete.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup    User sets the feature setup for telesales to on passing with 'telesales' value

*** Test Cases ***
1 - Able to PUT route coverage with random data
    [Documentation]    Able to create route coverage with random generated data via API
    [Tags]    hqadm    distadm    9.3
    Given user retrieves token access as ${user_role}
    When ${user_role} creates route coverage with random data
    Then expected return status code 201
    When ${user_role} updates route coverage with random data
    Then expected return status code 200
    When user deletes route coverage
    Then expected return status code 200
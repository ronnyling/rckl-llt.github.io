*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoverageGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoveragePost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoverageDelete.py


*** Test Cases ***
1 - Able to retrieve all route coverage
    [Documentation]    Able to retrieve all route coverage
    [Tags]    distadm    hqadm    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves all route coverage
    Then expected return status code 200

2 - Able to retrieve route coverage using valid ID
    [Documentation]    Able to retrieve route coverage using valid ID
    [Tags]    distadm    hqadm    9.3
    Given user retrieves token access as ${user_role}
    When ${user_role} creates route coverage with random data
    Then expected return status code 201
    When user retrieves route coverage by valid id
    Then expected return status code 200
    When user deletes route coverage
    Then expected return status code 200

3 - Unable to retrieve route coverage using invalid ID
    [Documentation]    Unable to retrieve route coverage using invalid ID
    [Tags]    distadm    hqadm    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves route coverage by invalid id
    Then expected return status code 404
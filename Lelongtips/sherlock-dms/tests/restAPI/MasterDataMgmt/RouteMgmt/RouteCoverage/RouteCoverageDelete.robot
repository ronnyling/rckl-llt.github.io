*** Settings ***
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoveragePost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteCoverage/RouteCoverageDelete.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to DELETE route coverage and get 200
    [Documentation]  To delete route coverage via API
    [Tags]    distadm    hqadm    9.3
    Given user retrieves token access as ${user_role}
    When ${user_role} creates route coverage with random data
    Then expected return status code 201
    When user deletes route coverage
    Then expected return status code 200

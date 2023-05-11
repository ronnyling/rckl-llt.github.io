*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberGet.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets route by using code 'Rchoon'

Test Teardown     run keywords
...    user deletes route transaction number
...    AND  expected return status code 200

*** Test Cases ***
1 - Able to Get all Route Transaction number
    [Documentation]    Able to retrieve all route transaction number
    [Tags]    distadm     9.4
    Given user retrieves token access as ${user_role}
    When user creates route transaction number with random data
    Then expected return status code 200
    When user retrieves all route transaction number
    Then expected return status code 200

2 - Able to Get Route Transaction number by using ID
    [Documentation]    Able to retrieve route transaction number by using ID
    [Tags]    distadm     9.4
    Given user retrieves token access as ${user_role}
    When user creates route transaction number with random data
    Then expected return status code 200
    When user retrieves route transaction number by ID
    Then expected return status code 200

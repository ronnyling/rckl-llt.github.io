*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberDelete.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets route by using code 'Rchoon'

Test Teardown     run keywords
...    user deletes route transaction number
...    AND    expected return status code 200

*** Test Cases ***
1 - Able to delete Route Transaction number
    [Documentation]    Able to delete route transaction number using created data
    [Tags]    distadm     9.4
    Given user retrieves token access as ${user_role}
    When user creates route transaction number with random data
    Then expected return status code 200

2 - Unable to DELETE Prime/Non-Prime Transaction Number using Hq access and get 403
    [Documentation]    Unable to delete route transaction number using hq access
    [Tags]    hquser   hqadm   sysimp     9.4
    Given user retrieves token access as distadm
    When user creates route transaction number with random data
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user deletes route transaction number
    Then expected return status code 403
    Given user retrieves token access as distadm

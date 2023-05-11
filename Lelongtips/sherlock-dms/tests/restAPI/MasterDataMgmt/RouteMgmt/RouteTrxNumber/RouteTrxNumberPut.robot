*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberPut.py



Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets route by using code 'Rchoon'

Test Teardown     run keywords
...    user deletes route transaction number
...    AND    expected return status code 200

*** Test Cases ***
1 - Able to update Route Transaction number with random data
    [Documentation]    Able to update route transaction number using random data
    [Tags]    distadm   9.4
    Given user retrieves token access as ${user_role}
    When user creates route transaction number with random data
    Then expected return status code 200
    When user updates route transaction number with random data
    Then expected return status code 200

2 - Able to updates Route Transaction number with given data
    [Documentation]    Able to updates route transaction number using given data
    [Tags]    distadm   9.4
    Given user retrieves token access as ${user_role}
    When user creates route transaction number with random data
    Then expected return status code 200
    ${route_trx_no_details}=   create dictionary
    ...    TXN_TYPE=RETURN
    ...    PREFIX=TRTN
    ...    START_NUM=${1001}
    ...    END_NUM=${2000}
    ...    TXN_NUMBERLEN=${5}
    ...    SUFFIX=IV
    set test variable    ${route_trx_no_details}
    When user updates route transaction number with fixed data
    Then expected return status code 200

3 - Unable to PUT Principal field in Transaction Number
    [Documentation]    Able to updates route transaction number using given data
    [Tags]    distadm      9.5
    ${route_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=PRIME
    set test variable    ${route_trx_no_details}
    Given user retrieves token access as ${user_role}
    When user creates route transaction number with fixed data
    Then expected return status code 200
    ${route_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    set test variable    ${route_trx_no_details}
    When user updates route transaction number with fixed data
    Then expected return status code 400

4 - Unable to PUT Non-Prime Transaction Number using Hq access
    [Documentation]    Unable to updates route transaction number using HQ access
    [Tags]    hqadm   hquser   sysimp    9.4
    ${route_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    set test variable    ${route_trx_no_details}
    Given user retrieves token access as distadm
    When user creates route transaction number with fixed data
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user updates route transaction number with fixed data
    Then expected return status code 403
    Given user retrieves token access as distadm

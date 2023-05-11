*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteTrxNumber/RouteTrxNumberDelete.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets route by using code 'Rchoon'

*** Test Cases ***
1 - Able to create Route Transaction number with random data
    [Documentation]    Able to create Route transaction number using random data
    [Tags]    distadm   9.4
    [Teardown]     run keywords
    ...    user deletes route transaction number
    ...    AND    expected return status code 200
    Given user retrieves token access as ${user_role}
    And user gets route by using code 'Rchoon'
    When user creates route transaction number with random data
    Then expected return status code 200

2 - Able to create Route Transaction number with given data
    [Documentation]    Able to create Route prime transaction number using given data
    [Tags]    distadm   9.4
    [Teardown]     run keywords
    ...    user deletes route transaction number
    ...    AND    expected return status code 200
    ${route_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=PRIME
    ...    TXN_TYPE=RETURN
    ...    PREFIX=NTIV
    ...    START_NUM=${1001}
    ...    END_NUM=${2000}
    ...    SUFFIX=IV
    ...    TXN_NUMBERLEN=${5}
    set test variable    ${route_trx_no_details}
    Given user retrieves token access as ${user_role}
    When user creates route transaction number with fixed data
    Then expected return status code 200

3 - Able to create Route Non Prime Transaction number with given data
    [Documentation]    Able to create Route non prime transaction number using given data
    [Tags]   distadm    9.4
    [Teardown]     run keywords
    ...    user deletes route transaction number
    ...    AND    expected return status code 200
    ${route_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    set test variable    ${route_trx_no_details}
    Given user retrieves token access as ${user_role}
    When user creates route transaction number with fixed data
    Then expected return status code 200

4 - Unable to create Route Transaction number with invalid data
    [Documentation]    Unable to create Route transaction number using invalid data
    [Tags]      distadm    9.4
    ${route_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    TXN_TYPE=SO      #correct sales order type should be SALES_ORDER
    set test variable    ${route_trx_no_details}
    Given user retrieves token access as ${user_role}
    When user creates route transaction number with fixed data
    Then expected return status code 400

5 - Unable to POST Prime Transaction Number using Hq access and get 403
    [Documentation]    Unable to create route transaction number using HQ access
    [Tags]    hqadm   hquser   sysimp    9.1     NRSZUANQ-30024
    ${route_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    set test variable    ${route_trx_no_details}
    Given user retrieves token access as hqadm
    When user creates route transaction number with fixed data
    Then expected return status code 403
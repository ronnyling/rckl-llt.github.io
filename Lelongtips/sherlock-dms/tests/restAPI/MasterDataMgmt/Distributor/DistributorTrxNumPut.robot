*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumDelete.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    AND    user gets distributor by using code 'DistEgg'

Test Teardown     run keywords
...    user deletes distributor transaction number
...    AND    expected return status code 200

*** Test Cases ***
1 - Able to update Distributor Transaction number with random data
    [Documentation]    Able to update Distributor transaction number using random data
    [Tags]    distadm   9.0    9.1    NRSZUANQ-30020
    Given user retrieves token access as ${user_role}
    When user creates distributor transaction number with random data
    Then expected return status code 201
    When user updates distributor transaction number with random data
    Then expected return status code 200

2 - Able to updates Distributor Transaction number with given data
    [Documentation]    Able to updates Distributor transaction number using given data
    [Tags]    distadm   9.0    9.1
    Given user retrieves token access as ${user_role}
    When user creates distributor transaction number with random data
    Then expected return status code 201
    ${dist_trx_no_details}=   create dictionary
    ...    TXN_TYPE=INVOICE
    ...    PREFIX=TINV
    ...    START_NUM=${1001}
    ...    END_NUM=${2000}
    ...    SUFFIX=IV
    set test variable    ${dist_trx_no_details}
    When user updates distributor transaction number with fixed data
    Then expected return status code 200

3 - Unable to PUT Principal field in Transaction Number
    [Documentation]    Able to updates Distributor transaction number using given data
    [Tags]    distadm      9.1    NRSZUANQ-30019
    ${dist_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=PRIME
    set test variable    ${dist_trx_no_details}
    Given user retrieves token access as ${user_role}
    When user creates distributor transaction number with fixed data
    Then expected return status code 201
    ${dist_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    set test variable    ${dist_trx_no_details}
    When user updates distributor transaction number with fixed data
    Then expected return status code 400

4 - Unable to PUT Non-Prime Transaction Number using Hq access
    [Documentation]    Unable to updates Distributor transaction number using HQ access
    [Tags]    hqadm   hquser   sysimp    9.1    NRSZUANQ-30025
    ${dist_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    set test variable    ${dist_trx_no_details}
    Given user retrieves token access as distadm
    When user creates distributor transaction number with fixed data
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user updates distributor transaction number with fixed data
    Then expected return status code 403
    Given user retrieves token access as distadm

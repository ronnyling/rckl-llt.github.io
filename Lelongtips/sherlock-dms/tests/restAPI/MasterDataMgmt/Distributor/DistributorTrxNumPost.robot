*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumDelete.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to create Distributor Transaction number with random data
    [Documentation]    Able to create Distributor transaction number using random data
    [Tags]    distadm   9.0    9.1
    [Teardown]     run keywords
    ...    user deletes distributor transaction number
    ...    AND    expected return status code 200
    Given user retrieves token access as ${user_role}
    When user creates distributor transaction number with random data
    Then expected return status code 201

2 - Able to create Distributor Prime Transaction number with given data
    [Documentation]    Able to create Distributor prime transaction number using given data
    [Tags]    distadm   9.1    NRSZUANQ-30017
    [Teardown]     run keywords
    ...    user deletes distributor transaction number
    ...    AND    expected return status code 200
    ${dist_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=PRIME
    ...    TXN_TYPE=INVOICE
    ...    PREFIX=TINV
    ...    START_NUM=${1001}
    ...    END_NUM=${2000}
    ...    SUFFIX=IV
    set test variable    ${dist_trx_no_details}
    Given user retrieves token access as ${user_role}
    When user creates distributor transaction number with fixed data
    Then expected return status code 201

3 - Able to create Distributor Non Prime Transaction number with given data
    [Documentation]    Able to create Distributor non prime transaction number using given data
    [Tags]   distadm    9.1    NRSZUANQ-30018
    [Teardown]     run keywords
    ...    user deletes distributor transaction number
    ...    AND    expected return status code 200
    ${dist_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    set test variable    ${dist_trx_no_details}
    Given user retrieves token access as ${user_role}
    When user creates distributor transaction number with fixed data
    Then expected return status code 201

4 - Unable to create Distributor Transaction number with invalid data
    [Documentation]    Unable to create Distributor transaction number using invalid data
    [Tags]      distadm    9.1
    ${dist_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    TXN_TYPE=SO      #correct sales order type should be SALES_ORDER
    set test variable    ${dist_trx_no_details}
    Given user retrieves token access as ${user_role}
    When user creates distributor transaction number with fixed data
    Then expected return status code 400

5 - Unable to POST Prime Transaction Number using Hq access and get 403
    [Documentation]    Unable to create Distributor transaction number using HQ access
    [Tags]    hqadm   hquser   sysimp    9.1     NRSZUANQ-30024
    ${dist_trx_no_details}=   create dictionary
    ...    PRIME_FLAG=NON_PRIME
    set test variable    ${dist_trx_no_details}
    Given user retrieves token access as ${user_role}
    When user creates distributor transaction number with fixed data
    Then expected return status code 403

6 - Able to create trxno for distributor
    [Documentation]    Able to create trxno for distributor
    [Tags]    hehehe        9.5
    Given user retrieves token access as ${user_role}
    When user creates random distributor trxno
    Then expected return status code 201



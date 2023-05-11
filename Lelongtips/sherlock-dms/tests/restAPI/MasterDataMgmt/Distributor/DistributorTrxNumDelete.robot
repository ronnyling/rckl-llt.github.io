*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumDelete.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    user gets distributor by using code 'DistEgg'

Test Teardown     run keywords
...    user deletes distributor transaction number
...    AND    expected return status code 200

*** Test Cases ***
1 - Able to delete Distributor Transaction number
    [Documentation]    Able to delete Distributor transaction number using created data
    [Tags]    distadm     9.0    9.1    NRSZUANQ-30022
    Given user retrieves token access as ${user_role}
    When user creates distributor transaction number with random data
    Then expected return status code 201

2 - Unable to DELETE Prime/Non-Prime Transaction Number using Hq access and get 403
    [Documentation]    Unable to delete Distributor transaction number using hq access
    [Tags]    hquser   hqadm   sysimp     9.0    9.1    NRSZUANQ-30027
    Given user retrieves token access as distadm
    When user creates distributor transaction number with random data
    Then expected return status code 201
    Given user retrieves token access as ${user_role}
    When user deletes distributor transaction number
    Then expected return status code 403
    Given user retrieves token access as distadm

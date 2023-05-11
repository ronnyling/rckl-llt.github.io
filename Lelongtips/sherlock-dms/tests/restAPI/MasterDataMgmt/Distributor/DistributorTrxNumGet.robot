*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorTrxNumDelete.py

*** Test Cases ***
1 - Able to Get all Distributor Transaction number
    [Documentation]    Able to retrieve all Distributor transaction number
    [Tags]    distadm     9.0    9.1
    [Teardown]  run keywords
    ...     user deletes distributor transaction number
    Given user retrieves token access as ${user_role}
    And user retrieves all distributors list
    When user creates random distributor trxno
    Then expected return status code 201
    When user retrieves all distributor transaction number
    Then expected return status code 200

2 - Able to Get Distributor Transaction number by using ID
    [Documentation]    Able to retrieve Distributor transaction number by using ID
    [Tags]    distadm     9.0    9.1    NRSZUANQ-30021    NRSZUANQ-30026
    [Teardown]  run keywords
    ...     user deletes distributor transaction number
    Given user retrieves token access as ${user_role}
    And user retrieves all distributors list
    When user creates random distributor trxno
    Then expected return status code 201
    When user retrieves all distributor transaction number
    And user retrieves distributor transaction number by ID
    Then expected return status code 200


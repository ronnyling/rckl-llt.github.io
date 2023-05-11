*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingDelete.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py


*** Test Cases ***
1 - Able to retrieve all Sampling
    [Documentation]    Able to retrieve all sampling
    [Tags]    distadm    hqadm    9.3    NRSZUANQ-52758
    Given user retrieves token access as ${user_role}
    When user retrieves all sampling
    Then expected return status code 200

2 - Able to retrieve sampling using valid ID
    [Documentation]    Able to retrieve sampling using valid ID
    [Tags]    distadm    hqadm    9.3     NRSZUANQ-52762
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    When user retrieves sampling by valid id
    Then expected return status code 200
    When user deletes sampling
    Then expected return status code 200

3 - Unable to retrieve sampling using invalid ID
    [Documentation]    Unable to retrieve sampling using invalid ID
    [Tags]    distadm    hqadm    9.3     NRSZUANQ-52762
    Given user retrieves token access as ${user_role}
    When user retrieves sampling by invalid id
    Then expected return status code 404
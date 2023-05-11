*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingProductAssignment.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup    User sets the feature setup for sampling to on passing with 'sampling' value

*** Test Cases ***
1 - Able to POST product assignment to created sampling with random data
    [Documentation]    Able to add product assignment to created sampling with random generated data via API
    [Tags]    hqadm    distadm    9.3    NRSZUANQ-52763
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    When user adds product assignment to sampling
    Then expected return status code 201
    When user deletes sampling
    Then expected return status code 200

2 - Able to GET sampling product assignment
    [Documentation]    Able to retrieve sampling product assignment data via API
    [Tags]    hqadm    distadm    9.3    NRSZUANQ-52763
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    When user adds product assignment to sampling
    Then expected return status code 201
    When user retrieves sampling product assignment
    Then expected return status code 200
    When user deletes sampling
    Then expected return status code 200

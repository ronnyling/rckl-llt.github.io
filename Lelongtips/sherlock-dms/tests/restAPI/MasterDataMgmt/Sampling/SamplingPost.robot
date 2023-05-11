*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingDelete.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup    User sets the feature setup for sampling to on passing with 'sampling' value

*** Test Cases ***
1 - Able to POST Sampling with random data
    [Documentation]    Able to create sampling with random generated data via API
    [Tags]    hqadm    distadm    9.3    NRSZUANQ-52762
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    When user deletes sampling
    Then expected return status code 200

2 - Able to POST Sampling with fixed data
    [Documentation]  Able to create valid sampling with fixed data via API
    [Tags]    hqadm    distadm    9.3    NRSZUANQ-52762
    ${sampling_details}=    create dictionary
    ...     SAMPLE_DESC=SamplingAuto
    ...     CLAIMABLE_IND=${TRUE}
    ...     CLAIMABLE_ENDDT=2070-01-01
    ...     CLAIM_TYPE_CODE=ClaimTypeBran
    ...     START_DT=2050-01-01
    ...     END_DT=2060-01-01
    ...     SAMPLE_STATUS=${TRUE}
    set test variable   &{sampling_details}
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with fixed data
    Then expected return status code 201
    When user deletes sampling
    Then expected return status code 200
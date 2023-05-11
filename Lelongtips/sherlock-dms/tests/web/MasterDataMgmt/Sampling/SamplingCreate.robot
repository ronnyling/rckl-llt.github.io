*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingAddPage.py


*** Test Cases ***
1 - User able to create new sampling with random data
    [Documentation]  To validate user able to create new sampling with random data
    [Tags]    hqadm    distadm    9.2
    Given user navigates to menu Master Data Management | Sampling
    When user creates sampling using random data
    Then sampling created successfully with message 'Record created successfully'
    When user selects sampling to delete
    Then sampling deleted successfully with message 'Record deleted'

2 - User able to create new sampling with fixed data
    [Documentation]  To validate user able to create new sampling with fixed data
    [Tags]    hqadm    distadm    9.2
    ${sampling_details}=    create dictionary
    ...    SAMPLING_DESC=Sampling Desc
    ...    START_DATE=2026-06-02
    ...    END_DATE=2026-06-03
    ...    CLAIMABLE=${True}
    ...    CLAIM_SUBMISSION_DEADLINE=2026-06-04
    ...    CLAIM_TYPE=Claim Type B04
    set test variable     &{sampling_details}
    Given user navigates to menu Master Data Management | Sampling
    When user creates sampling using fixed data
    Then sampling created successfully with message 'Record created successfully'
    When user selects sampling to delete
    Then sampling deleted successfully with message 'Record deleted'

*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingPost.py


*** Test Cases ***
1 - User able to update sampling with random data
    [Documentation]  To validate user able to update sampling with random data
    [Tags]    hqadm    distadm    9.2
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Sampling
    When user selects sampling to edit
    And user updates sampling using random data
    Then sampling updated successfully with message 'Record updated successfully'
    When user selects sampling to delete
    Then sampling deleted successfully with message 'Record deleted'

2 - User able to update sampling with fixed data
    [Documentation]  To validate user able to update sampling with fixed data
    [Tags]    hqadm    distadm    9.2
    ${sampling_details}=    create dictionary
    ...    SAMPLING_DESC=SamplingUpdate
    ...    START_DATE=2026-06-06
    ...    END_DATE=2026-06-07
    ...    CLAIMABLE=${True}
    ...    CLAIM_SUBMISSION_DEADLINE=2026-06-08
    ...    CLAIM_TYPE=Claim Type B04
    set test variable     &{sampling_details}
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Sampling
    When user selects sampling to edit
    And user updates sampling using fixed data
    Then sampling updated successfully with message 'Record updated successfully'
    When user selects sampling to delete
    Then sampling deleted successfully with message 'Record deleted'

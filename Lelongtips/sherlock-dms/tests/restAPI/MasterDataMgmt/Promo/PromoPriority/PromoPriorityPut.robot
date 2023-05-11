*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityDelete.py

*** Test Cases ***
1 - Able to update promotion sequence via API
    [Documentation]  This test is to update promotion sequence via API
    [Tags]      sysimp   hqadm   hquser    9.0
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using random data
    Then expected return status code 201
    ${PromoSeq}=    create dictionary
    ...    PROMO_SEQ_DESC=updated desc auto
    When user updates promotion sequence with update data
    Then expected return status code 200
    When user deletes promotion sequence
    Then expected return status code 200

2 - Unable to update promotion sequence using same priority via API
    [Documentation]  This test is unable to update promotion sequence using same priority to apply via API
    [Tags]      sysimp   hqadm   hquser    9.0
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves all promotion sequence
    Then expected return status code 200
    When user creates promotion sequence using random data
    Then expected return status code 201
    When user updates promotion sequence with updatePriority data
    Then expected return status code 409
    When user deletes promotion sequence
    Then expected return status code 200

3 - Unable to update promotion sequence using non existing promotion sequence code via API
    [Documentation]  This test is unable to update promotion sequence using non existing promotion sequence code via API
    [Tags]      sysimp   hqadm   hquser    9.0
    set test variable    ${sequence_id}     4a87983c:1e7e1d73-b756-451c-8483-097090cd0331
    set test variable      ${user_role}    hqadm
     Given user retrieves token access as ${user_role}
     When user updates promotion sequence with random data
     Then expected return status code 404

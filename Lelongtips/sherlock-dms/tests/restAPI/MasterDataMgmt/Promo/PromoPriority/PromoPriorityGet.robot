*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityDelete.py

*** Test Cases ***
1 - Able to retrieve all promotion sequence via API
    [Documentation]  This test is to retrieve all promotion sequence via API
    [Tags]      sysimp   hqadm   hquser    9.0
    [Teardown]   run keywords
    ...     user deletes promotion sequence
    ...     expected return status code 200
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using random data
    Then expected return status code 201
    When user retrieves all promotion sequence
    Then expected return status code 200

2 - Able to retrieve promotion sequence by ID via API
    [Documentation]  This test is to retrieve promotion sequence by ID via API
    [Tags]      sysimp   hqadm   hquser      9.0
    [Teardown]   run keywords
    ...     user deletes promotion sequence
    ...     expected return status code 200
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using random data
    Then expected return status code 201
    When user retrieves promotion sequence by id
    Then expected return status code 200

3 - Unable to retrieve promotion sequence using non existing promotion sequence code via API
    [Documentation]  This test is unable to retrieve promotion sequence using non existing promotion sequence code via API
    [Tags]     sysimp   hqadm   hquser    9.0
    set test variable  ${sequence_id}     4a87983c:1e7e1d73-b756-451c-8483-097090cd0330
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves promotion sequence by id
    Then expected return status code 404

4 - Unable to retrieve promotion sequence using invalid length of promotion sequence ID via API
    [Documentation]  This test is unable to retrieve promotion sequence using invalild length of promotion sequence id via API
    [Tags]      sysimp   hqadm   hquser    9.0
    set test variable  ${sequence_id}     4a87983c
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves promotion sequence by id
    Then expected return status code 404

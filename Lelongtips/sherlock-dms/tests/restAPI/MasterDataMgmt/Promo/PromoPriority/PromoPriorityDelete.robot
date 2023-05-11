*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityDelete.py

*** Test Cases ***
1 - Able to delete promotion sequence by ID via API
    [Documentation]  This test is to delete promotion sequence by ID via API
    [Tags]      sysimp   hqadm   hquser   9.0
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using random data
    Then expected return status code 201
    When user deletes promotion sequence
    Then expected return status code 200

2 - Unable to delete promotion sequence using non existing promotion sequence code via API
    [Documentation]  This test is unable to delete promotion sequence using non existing promotion sequence code via API
    [Tags]      sysimp   hqadm   hquser   9.0
    set test variable  ${sequence_id}     4a87983c:1e7e1d73-b756-451c-8483-097090cd0331
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user deletes promotion sequence
    Then expected return status code 404

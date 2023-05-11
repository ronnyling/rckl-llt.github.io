*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPriority/PromoPriorityDelete.py

*** Test Cases ***
1 - Able to create promotion sequence using fixed data via API
    [Documentation]  This test is to create promotion sequence using fixed data via API
    [Tags]    sysimp   hqadm   hquser    9.0
    [Teardown]   run keywords
    ...     user deletes promotion sequence
    ...     expected return status code 200
    ${PromoSeq}=    create dictionary
    ...    PROMO_SEQ_DESC=promo desc auto
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using fixed data
    Then expected return status code 201

2 - Able to create promotion sequence using random data via API
    [Documentation]  This test is to create promotion sequence using random data via API
    [Tags]    sysimp   hqadm   hquser  9.0
    [Teardown]   run keywords
    ...     user deletes promotion sequence
    ...     expected return status code 200
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using random data
    Then expected return status code 201

3 - Unable to create promotion sequence using Invalid Values via API
    [Documentation]  This test is unable to create promotion sequence using invalid values via API
    [Tags]  sysimp   hqadm   hquser   9.0
    ${PromoSeq}=    create dictionary
    ...    PROMO_SEQ_CD=@#$
    ...    PROMO_SEQ_DESC=@#$
    ...    PROMO_PRIORITY=abc
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using fixed data
    Then expected return status code 400

4 - Unable to create promotion sequence with characters more than maximum limit via API
    [Documentation]  This test is unable to create promotion sequence with characters more than maximum limit via API
    [Tags]     sysimp   hqadm   hquser   9.0
    ${PromoSeq}=    create dictionary
    ...    PROMO_SEQ_CD=abcdefgh1234567890123
    ...    PROMO_SEQ_DESC=I2X8V16O9WANJ4IX3JC8MOFADFR1Q6465NM0PRA4GT86Q5ZB2R2
    ...    PROMO_PRIORITY=12345678
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using fixed data
    Then expected return status code 400

5 - Unable to create promotion sequence using same code via API
    [Documentation]  This test is unable to create promotion sequence using same promotion sequence code via API
    [Tags]      sysimp   hqadm   hquser   9.0
    [Teardown]   run keywords
    ...     user deletes promotion sequence
    ...     expected return status code 200
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using random data
    Then expected return status code 201
    When user creates promotion sequence using existing data
    Then expected return status code 409

6 - Unable to create promotion sequence using deleted code via API
    [Documentation]  This test is unable to create promotion sequence using deleted promotion sequence code via API
    [Tags]    sysimp   hqadm   hquser    9.0
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using random data
    Then expected return status code 201
    When user deletes promotion sequence
    Then expected return status code 200
    When user creates promotion sequence using deleted data
    Then expected return status code 409

7 - Unable to create promotion sequence using same priority via API
    [Documentation]  This test is unable to create promotion sequence using same priority to apply via API
    [Tags]    sysimp   hqadm   hquser  9.0
    [Teardown]   run keywords
    ...     user deletes promotion sequence
    ...     expected return status code 200
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates promotion sequence using random data
    Then expected return status code 201
    When user creates promotion sequence using existingPriority data
    Then expected return status code 409

*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/Claim/ClaimGet.py


*** Test Cases ***
1 - Able to retrieve all claims
    [Documentation]    Able to retrieve all claims
    [Tags]        distadm     9.1.1
    Given user retrieves token access as ${user_role}
    When user retrieves all claim
    Then expected return status code 200

2 - Able to retrieve claims using ID
    [Documentation]    Able to retrieve claim using id
    [Tags]        distadm     hqadm     9.1.1    NRSZUANQ-42228
    Given user retrieves token access as ${user_role}
    When user retrieves claim by id
    Then expected return status code 200

3 - Able to retrieve claim using invalid ID and get 404
    [Documentation]    Unable to retrieve claim using invalid ID
    [Tags]        distadm     hqadm     9.1.1
    set test variable   ${claim_id}    C8A8CE55:D909C276-8882-88BF-BED7-7688D7741559
    Given user retrieves token access as ${user_role}
    When user retrieves claim by id
    Then expected return status code 404
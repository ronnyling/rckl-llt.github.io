*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteProduct/DebitNoteProductGet.py


*** Test Cases ***
1 - Able to retrieve all debit note product
    [Documentation]  Able to retrieve all debit note product
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all company debit note product
    Then expected return status code 200

2 - Able to retrieve debit note product by id
    [Documentation]  Able to retrieve debit note product by id
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves company debit note product by id
    Then expected return status code 200

3 - Unable to retrieve debit note product by invalid id
    [Documentation]  Able to retrieve debit note product by id
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    set test variable   ${sdnp_id}      00A000A0:AABB1A2B-0000-0000-0000-AA0000000000
    When user retrieves company debit note product by id
    Then expected return status code 404

4 - Unable to retrieve all debit note product using HQ access and get 403
    [Documentation]  Able to retrieve all debit note product using other than distributor user
    [Tags]    hqadm
    Given user retrieves token access as hqadm
    When user retrieves all company debit note product
    Then expected return status code 403

5 - Unable to retrieve debit note product by id using HQ access and get 403
    [Documentation]  Able to retrieve debit note product by id using other than distributor user
    [Tags]    hqadm
    Given user retrieves token access as hqadm
    When user retrieves company debit note product by id
    Then expected return status code 403
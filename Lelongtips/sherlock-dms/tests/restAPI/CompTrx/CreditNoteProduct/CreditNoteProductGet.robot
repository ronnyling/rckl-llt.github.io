*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CreditNoteProduct/CreditNoteProductGet.py


*** Test Cases ***
1 - Able to retrieve all credit note product
    [Documentation]  Able to retrieve all credit note product
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all company credit note product
    Then expected return status code 200

2 - Able to retrieve credit note product by valid id
    [Documentation]  Able to retrieve credit note product by valid id
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves company credit note product by id
    Then expected return status code 200

3 - Unable to retrieve credit note product by invalid id
    [Documentation]  Able to retrieve credit note product by invalid id
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    set test variable   ${scnp_id}      32D316B7:CECF2E0C-9DCD-4667-B7AA-CD8EDBB3B000
    When user retrieves company credit note product by id
    Then expected return status code 404

4 - Unable to retrieve all credit note product using HQ access and get 403
    [Documentation]  Unable to retrieve all credit note product using other than distributor user
    [Tags]    hqadm
    Given user retrieves token access as hqadm
    When user retrieves all company credit note product
    Then expected return status code 403

5 - Unable to retrieve credit note product by valid id using HQ access and get 403
    [Documentation]  Unble to retrieve credit note product by valid id using other than distributor user
    [Tags]    hqadm
    Given user retrieves token access as hqadm
    When user retrieves company credit note product by id
    Then expected return status code 403
*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CreditNoteNonProduct/CreditNoteNonProductGet.py

*** Test Cases ***
1 - Able to retrieve all credit note non product
    [Documentation]  Able to retrieve all credit note non product
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all company credit note non product
    Then expected return status code 200

2 - Able to retrieve credit note non product by id
    [Documentation]  Able to retrieve credit note non product by id
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves company credit note non product by id
    Then expected return status code 200

3 - Unable to retrieve credit note non product by invalid id
    [Documentation]  Unable to retrieve credit note non product by invalid id
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    set test variable   ${scnnp_id}      32D316B7:CECF2E0C-9DCD-4667-B7AA-CD8EDBB3B000
    When user retrieves company credit note non product by id
    Then expected return status code 404

4 - Unable to retrieve all credit note non product using HQ access and get 403
    [Documentation]  Unable to retrieve all credit note non product using other than distributor user
    [Tags]    hqadm
    Given user retrieves token access as hqadm
    When user retrieves all company credit note non product
    Then expected return status code 403

5 - Unable to retrieve credit note non product by id using HQ access and get 403
    [Documentation]  Unable to retrieve credit note non product by id using other than distributor user
    [Tags]    hqadm
    Given user retrieves token access as hqadm
    When user retrieves company credit note non product by id
    Then expected return status code 403
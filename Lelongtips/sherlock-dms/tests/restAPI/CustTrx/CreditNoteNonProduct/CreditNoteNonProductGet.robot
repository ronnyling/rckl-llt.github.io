*** Settings ***
Library         String
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/CreditNoteNonProduct/CreditNoteNonProductGet.py



*** Test Cases ***
1 - Able to retrieve all Credit Note Non Product
    [Documentation]    Able to retrieve all credit note
    [Tags]    distadm    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves all credit note non product
    Then expected return status code 200

2 - Able to retrieve Credit Note Non Product by id
    [Documentation]    Able to retrieve credit note using id
    [Tags]    distadm    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves all credit note non product
    Then expected return status code 200
    When user retrieves credit note non product by id
    Then expected return status code 200

3 - Unable to retrieve Credit Note Non Product by invalid id
    [Documentation]    Unable to retrieve credit note using invalid id
    [Tags]    distadm    9.1   BUG:NRSZUANQ-51866
    Given user retrieves token access as ${user_role}
    set test variable   ${rand_cn_selection}      375C4A78:AF5FD26D-BAE6-48B0-AEFD-AB3E2B6CF333
    When user retrieves credit note non product by id
    Then expected return status code 404

4 - Unable to retrieve all Credit Note Non Product using HQ access and get 403
    [Documentation]    Unable to retrieve credit note using other than distributor user
    [Tags]    hqadm    9.1
    Given user retrieves token access as hqadm
    When user retrieves all credit note non product
    Then expected return status code 403

5 - Unable to retrieve Credit Note Non Product by ID using HQ access and get 403
    [Documentation]    Unable to retrieve credit note using other than distributor user
    [Tags]    hqadm    9.1
    Given user retrieves token access as hqadm
    When user retrieves credit note non product by id
    Then expected return status code 403
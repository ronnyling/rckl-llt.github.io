*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/CreditNoteNonProduct/CreditNoteNonProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/CreditNoteNonProduct/CreditNoteNonProductPut.py

Test Setup     user get PRIME credit note non product prerequisite

*** Test Cases ***
1 - Able to put non prime credit note and return 201
    [Documentation]    Able to update non-taxable credit note non product
    [Tags]    distadm    9.1     test
    ${cn_np_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user creates credit note non product with fixed data
    Then expected return status code 201
    When user updates credit note non product with fixed data
    Then expected return status code 201

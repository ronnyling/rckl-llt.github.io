*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CreditNoteProduct/CreditNoteProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CreditNoteProduct/CreditNoteProductProcess.py

*** Test Cases ***
1 - Able to confirm created credit note product
    [Documentation]  Able to confirm created credit note product
    [Tags]    distadm    9.2
    ${cnp_details}=    create dictionary
    ...    SUPPLIER=hqtax
    ...    PRD_CD=TP001
    ...    WHS=whtt
    ...    QUANTITY=1
    ...    PRICE=10
    ...    REASON=CreditNoteTest
    set test variable  &{cnp_details}
    Given user retrieves token access as ${user_role}
    When user creates credit note product using fixed data
    Then expected return status code 201
    When user confirms created credit note product
    Then expected return status code 200
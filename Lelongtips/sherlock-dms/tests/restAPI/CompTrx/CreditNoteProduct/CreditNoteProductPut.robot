*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CreditNoteProduct/CreditNoteProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CreditNoteProduct/CreditNoteProductPut.py

*** Test Cases ***
1 - Able to PUT credit note product
    [Documentation]  Able to edit credit note product
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
    ${cnp_details}=    create dictionary
    ...    SUPPLIER=hqtax
    ...    PRD_CD=TP001
    ...    WHS=whtt
    ...    QUANTITY=2
    ...    PRICE=15
    ...    REASON=CreditNoteTest
    When user updates created credit note product using fixed data
    Then expected return status code 200

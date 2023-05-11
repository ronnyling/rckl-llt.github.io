*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteProduct/DebitNoteProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteProduct/DebitNoteProductPut.py

*** Test Cases ***
1 - Able to PUT debit note product
    [Documentation]  Able to edit debit note product
    [Tags]    distadm    9.2
    ${dnp_details}=    create dictionary
    ...    SUPPLIER=hqtax
    ...    PRD_CD=TP001
    ...    QUANTITY=1
    ...    PRICE=10
    ...    REASON=DebitNoteTesting
    set test variable  &{dnp_details}
    Given user retrieves token access as ${user_role}
    When user creates debit note product using fixed data
    Then expected return status code 201
    ${dnp_details}=    create dictionary
    ...    SUPPLIER=hqtax
    ...    PRD_CD=TP001
    ...    QUANTITY=2
    ...    PRICE=15
    ...    REASON=DebitNoteTesting
    set test variable  &{dnp_details}
    When user updates created debit note product using fixed data
    Then expected return status code 200

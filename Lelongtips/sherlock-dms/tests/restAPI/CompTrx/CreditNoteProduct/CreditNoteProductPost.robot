*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CreditNoteProduct/CreditNoteProductPost.py

*** Test Cases ***
1 - Able to POST credit note product
    [Documentation]  Able to create credit note product in Open status
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

2 - Able to POST & confirm credit note product
    [Documentation]  Able to create credit note product in Confirm status
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
    When user confirms credit note product using fixed data
    Then expected return status code 201

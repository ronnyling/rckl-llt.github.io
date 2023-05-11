*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteProduct/DebitNoteProductPost.py

*** Test Cases ***
1 - Able to POST debit note product
    [Documentation]  Able to create debit note product in Open status
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

2 - Able to POST & confirm debit note product
    [Documentation]  Able to create debit note product in Confirm status
    [Tags]    distadm    9.2
    ${dnp_details}=    create dictionary
    ...    SUPPLIER=hqtax
    ...    PRD_CD=TP001
    ...    QUANTITY=1
    ...    PRICE=10
    ...    REASON=DebitNoteTesting
    set test variable  &{dnp_details}
    Given user retrieves token access as ${user_role}
    When user confirms debit note product using fixed data
    Then expected return status code 201

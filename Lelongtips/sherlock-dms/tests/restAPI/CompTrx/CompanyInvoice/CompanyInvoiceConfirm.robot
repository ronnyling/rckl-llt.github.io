*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CompanyInvoice/CompanyInvoicePost.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CompanyInvoice/CompanyInvoicePut.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CompanyInvoice/CompanyInvoiceConfirm.py

*** Test Cases ***
1 - Able to confirm company invoice
    [Documentation]  Able to confirm company invoice
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    ${inv_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=whtt
    ...    PRD_CD=TP001
    ...    QUANTITY=1
    ...    AMOUNT=10
    set test variable  &{inv_details}
    When user creates company invoice using fixed data
    Then expected return status code 201
    When user confirms company invoice
    Then expected return status code 201


*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CompanyInvoice/CompanyInvoicePost.py

*** Test Cases ***
1 - Able to create company invoice
    [Documentation]  Able to create company invoice
    [Tags]    distadm    9.2
    ${inv_details}=    create dictionary
    ...    DIST=DistEgg
    ...    WHS=whtt
    ...    PRD_CD=TP001
    ...    QUANTITY=1
    ...    AMOUNT=10
    set test variable  &{inv_details}
    Given user retrieves token access as ${user_role}
    When user creates company invoice using fixed data
    Then expected return status code 201

*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CompanyInvoice/CompanyInvoiceGet.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CompanyInvoice/CompanyInvoicePost.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CompanyInvoice/CompanyInvoiceConfirm.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CompanyInvoice/CompanyInvoiceDelete.py

*** Test Cases ***
1 - Able to deletes company invoice
    [Documentation]  Able to deletes company invoice
    [Tags]    distadm
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
    When user deletes company invoice
    Then expected return status code 200
    When user retrieves company invoice by id
    Then expected return status code 404

2 - Unable to deletes Confirm company invoice
    [Documentation]  Unable to deletes company invoice other than Open status
    [Tags]    distadm
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
    When user deletes company invoice
    Then expected return status code 400


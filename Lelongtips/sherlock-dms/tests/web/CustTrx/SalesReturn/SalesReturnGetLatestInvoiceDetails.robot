*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnGetLatestInvoiceDetails.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py


*** Test Cases ***
1. Able to retrieve the latest invoice based on product selected in product level
    [Documentation]    To retrieve the latest invoice based on product selected in product level
    [Tags]    distadm    9.3    NRSZUANQ-54646
     ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    And user creates invoice with fixed data
    ${return_details}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    ROUTE=Rchoon
    ...    TYPE=Good Return
    ...    PRODUCT=CNPD001
    set test variable   &{return_details}
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Sales Return
    Then user retrieves latest invoice
*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library           ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnGetLatestInvoiceDetails.py

*** Test Cases ***
1 - Able to get the latest Invoice and details for the given product and customer
    [Documentation]    To get the latest Invoice and details for the given product and customer via API
    [Tags]    distadm    9.3    NRSZUANQ-54646
     ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    And user creates invoice with fixed data
     ${invoice_details}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PRD_CD=CNPD001
    ...    ROUTE_CD=Rchoon
    set test variable   &{invoice_details}
    When user retrieves invoice details by data
    Then expected return status code 200

2 - Able to get the Invoice details for the given Product, Customer & Invoice
    [Documentation]    To get the Invoice details for the given Product, Customer & Invoice via API
    [Tags]    distadm    9.3    NRSZUANQ-54646
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    And user creates invoice with fixed data
     ${invoice_details}=    create dictionary
    ...    INV_NO=yes
    ...    CUST_NAME=CXTESTTAX
    ...    PRD_CD=CNPD001
    ...    ROUTE_CD=Rchoon
    set test variable   &{invoice_details}
    When user retrieves invoice details by data
    Then expected return status code 200

3 - Able to return list of Invoices that are associated with the given Product, Customer, and time period
    [Documentation]    To return list of Invoices that are associated with the given Product, Customer, and time period via API
    [Tags]    distadm    9.3    NRSZUANQ-54646
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    And user creates invoice with fixed data
     ${invoice_details}=    create dictionary
    ...    FROM_DATE=2021-06-08
    ...    TO_DATE=2021-09-06
    ...    CUST_NAME=CXTESTTAX
    ...    PRD_CD=CNPD001
    ...    ROUTE_CD=Rchoon
    set test variable   &{invoice_details}
    When user retrieves invoice details by data
    Then expected return status code 200

4 - Able to get the Latest Invoice details for the given Products( List of Products) & Customer.
    [Documentation]    To get the Latest Invoice details for the given Products( List of Products) & Customer via API
    [Tags]    distadm    9.3    NRSZUANQ-54646
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    And user intends to insert product 'CNPD002' with uom 'EA:5'
    And user creates invoice with fixed data
     ${invoice_details}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PRD_CD=CNPD001,CNPD002
    set test variable   &{invoice_details}
    When user retrieves invoice details by data
    Then expected return status code 200
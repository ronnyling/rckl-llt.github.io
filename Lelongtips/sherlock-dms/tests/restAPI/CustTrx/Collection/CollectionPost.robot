*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py


*** Test Cases ***
1 - Able to POST Collection with random data
    [Documentation]    Able to create collection with random generated data via API
    [Tags]  distadm    9.2    NRSZUANQ-44444
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    When user creates collection with random data
    Then expected return status code 202

2 - Able to POST Collection with fixed data
    [Documentation]    Able to create collection with fixed data via API
    [Tags]  distadm    9.2    NRSZUANQ-44444
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${collection_details}=    create dictionary
    ...     CASH_AMT=${2}
    set test variable   &{collection_details}
    ${payment_details}=    create dictionary
    ...     OTHER_PYMT_METHOD=W
    ...     CHEQUE_AMT=${100}
    ...     CHEQUE_DATE=2021-01-12
    ...     DRAWEE_BANK_ID=D860BF7A:A58172FE-1187-4004-A857-6776084B872C
    set test variable   &{payment_details}
    When user creates collection with fixed data
    Then expected return status code 202

3 - Able to POST Collection with cash payment only
    [Documentation]    Able to create collection with cash payment only via API
    [Tags]  distadm    9.2    NRSZUANQ-44444
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${collection_details}=    create dictionary
    ...     CASH_AMT=${3}
    ...     OTHER_PYMTS=[]
    set test variable   &{collection_details}
    When user creates collection with fixed data
    Then expected return status code 202

4 - Able to POST Collection with cash and multiple payment method
    [Documentation]    Able to create collection with cash and multiple payment method via API
    [Tags]  distadm    9.2    NRSZUANQ-44444
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${collection_details}=    create dictionary
    ...     CASH_AMT=${4}
    set test variable   &{collection_details}
    set test variable     ${other_payment}     Q=5,W=100,Q=10
    When user creates collection with fixed data
    Then expected return status code 202

5 - Unable to POST Collection with hq access
    [Documentation]    Unable to create Collection with hq access
    [Tags]      hqadm   9.2    NRSZUANQ-44444
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as distadm
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user creates collection with random data
    Then expected return status code 403
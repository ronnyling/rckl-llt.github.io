*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionPut.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py


*** Test Cases ***
1 - Able to PUT Collection with random data
    [Documentation]    Able to update collection with random generated data via API
    [Tags]     distadm   9.2    NRSZUANQ-44092
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
    When user updates collection with random data
    Then expected return status code 200

2 - Able to PUT Collection with fixed data
    [Documentation]    Able to create collection with fixed data via API
    [Tags]  distadm   9.2    NRSZUANQ-44092
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
    ${collection_details}=    create dictionary
    ...     ROUTE_ID=02C42079:9E8BB008-1D1A-4B6C-87C5-1931A32A9F1A
    ...     CUST_ID=81398E09:6C18037B-612C-4742-87A3-2E44FF229F85
    ...     CASH_AMT=${5}
    ...     PRIME_FLAG=PRIME
    set test variable   &{collection_details}
    ${payment_details}=    create dictionary
    ...     OTHER_PYMT_METHOD=B
    ...     CHEQUE_AMT=${10}
    ...     CHEQUE_DATE=2021-01-20
    ...     DRAWEE_BANK_ID=D860BF7A:A58172FE-1187-4004-A857-6776084B872C
    set test variable   &{payment_details}
    When user updates collection with fixed data
    Then expected return status code 200

3 - Able to PUT Collection with cash payment only
    [Documentation]    Able to update collection with cash payment only via API
    [Tags]  distadm  9.2    NRSZUANQ-44092
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
    ${collection_details}=    create dictionary
    ...     CASH_AMT=${3}
    ...     OTHER_PYMTS=[]
    set test variable   &{collection_details}
    When user updates collection with fixed data
    Then expected return status code 200

4 - Able to PUT Collection with cash and multiple payment method
    [Documentation]    Able to update collection with cash and multiple payment method via API
    [Tags]  distadm   9.2    NRSZUANQ-44092
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
    ${collection_details}=    create dictionary
    ...     CASH_AMT=${14}
    set test variable   &{collection_details}
    set test variable     ${other_payment}     Q=15,W=16,Q=17
    When user updates collection with fixed data
    Then expected return status code 200

5 - Unable to PUT Collection with hq access
    [Documentation]    Unable to update Collection with hq access
    [Tags]      hqadm   9.2    NRSZUANQ-44092
    Given user retrieves token access as distadm
    When user retrieves collection by STATUS = S
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user updates collection with random data
    Then expected return status code 403
